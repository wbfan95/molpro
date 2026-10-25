"""Convert the crawled DokuWiki text pages to Sphinx/reStructuredText."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import unicodedata
from pathlib import Path, PurePosixPath


HEADING_CHARS = {
    6: "=",
    5: "-",
    4: "~",
    3: "^",
    2: '"',
}

PAGE_ALIASES: dict[str, str] = {}
ANCHOR_ALIASES: dict[str, set[str]] = {}

# Wiki playground/experiment pages that should not enter the manual.
SKIP_STEMS = {"table_of_contents_idx_playground", "table_of_contents_idx_wiki"}

# DokuWiki interwiki links, e.g. {{vimeo>12345|label}}.
INTERWIKI = {"vimeo": "https://vimeo.com/{}"}

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".webp"}

# media_id (any spelling) -> posix path of the copied file under docs/media.
MEDIA_ALIASES: dict[str, str] = {}

# Characters docutils allows immediately before/after inline markup.
PRE_MARKUP_OK = set(" \t'\"([{<-/:\\")
POST_MARKUP_OK = set(" \t'\"')]}>-/:;!?\\,.")


def page_stem(path: Path) -> str:
    return path.stem


def normalize_lookup_key(value: str) -> str:
    value = clean_nowiki(value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.strip().lower()
    value = value.replace("/", " ")
    value = re.sub(r"[_\s]+", " ", value)
    value = re.sub(r"[^0-9a-z]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def docname_for_stem(stem: str) -> str:
    stem = stem.strip().lower()
    stem = re.sub(r"[^0-9a-z_.-]+", "_", stem).strip("_")
    if stem == "index":
        return "manual_index"
    return stem


def page_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^=+\s*(.*?)\s*=+\s*$", line)
        if match:
            return match.group(1).strip()
    return fallback.replace("_", " ").title()


def slugify_anchor(text: str) -> str:
    text = re.sub(r"``([^`]+)``", r"\1", text)
    text = re.sub(r"[:`*_\\]", "", text)
    text = re.sub(r"[^0-9A-Za-z]+", "-", text.lower()).strip("-")
    return text or "section"


def resolve_docname(page: str, current_doc: str = "") -> str:
    key = normalize_lookup_key(page)
    if not key:
        return current_doc
    return PAGE_ALIASES.get(key, docname_for_stem(re.sub(r"\s+", "_", page.strip().lower())))


def normalize_target(raw: str, current_doc: str = "") -> tuple[str, str]:
    raw = raw.strip().replace("_", " ")
    if "#" in raw:
        page, anchor = raw.split("#", 1)
    else:
        page, anchor = raw, ""
    stem = resolve_docname(page, current_doc)
    anchor = slugify_anchor(anchor) if anchor else ""
    return stem, anchor


def rst_heading(title: str, level: int) -> list[str]:
    char = HEADING_CHARS.get(level, '"')
    return [title, char * max(len(title), 3), ""]


def clean_nowiki(text: str) -> str:
    return text.replace("%%", "")


def load_media_map(source_dir: Path) -> None:
    """Index the crawled media tree so {{...}} refs can resolve to real files."""
    MEDIA_ALIASES.clear()
    manifest_path = source_dir / "meta" / "manifest.json"
    if not manifest_path.exists():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for item in manifest.get("media", []):
        rel = item.get("relative_path", "")
        if not rel.startswith("media/"):
            continue
        target = rel[len("media/"):]
        if not (source_dir / "media" / target).is_file():
            continue
        media_id = item.get("media_id", "")
        for key in {media_id, media_id.lstrip(":")}:
            key = key.strip().lower()
            if key:
                MEDIA_ALIASES.setdefault(key, target)


def media_basename(ref: str) -> str:
    return re.split(r"[:/]", ref.strip().lstrip(":"))[-1]


def convert_image_ref(target: str, label: str, block: bool) -> str:
    """Convert one DokuWiki media reference ({{...}} inner text) to reST."""
    target = clean_nowiki(target.strip())
    size = ""
    sized = re.match(r"^(.+?)\?(\d+)(?:x\d+)?$", target)
    if sized:
        target, size = sized.group(1), sized.group(2)

    if ">" in target:
        prefix, _, ident = target.partition(">")
        url_template = INTERWIKI.get(prefix.strip().lower())
        if url_template:
            url = url_template.format(ident.strip())
            shown = label or f"{prefix.strip().lower()}.com/{ident.strip()}"
            return f"`{shown} <{url}>`__"

    if re.match(r"^[a-z][a-z0-9+.-]*://", target, flags=re.I):
        shown = label or target
        return f"`{shown} <{target}>`__"

    key = target.lstrip(":").lower()
    path = MEDIA_ALIASES.get(key) or MEDIA_ALIASES.get(media_basename(target))
    shown = label or media_basename(target)
    if path is None:
        return f"``{shown}``"
    ext = PurePosixPath(path).suffix.lower()
    if block and ext in IMAGE_EXTS:
        out = [f".. image:: /media/{path}", f"   :alt: {shown}"]
        if size:
            out.append(f"   :width: {size}px")
        return "\n".join(out)
    return f"`{shown} <media/{path}>`__"


def has_unbalanced_markup(text: str) -> bool:
    probe = re.sub(r"\bhttps?://\S*", "", text)
    probe = re.sub(r"\[\[.*?\]\]|\{\{.*?\}\}|<[^>\n]+>", "", probe)
    return any(probe.count(tok) % 2 for tok in ("''", "//", "**"))


def is_external_target(target: str) -> bool:
    target = target.strip()
    if not target:
        return False
    if target.startswith("//"):
        return True
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target))


def strip_doku_markup(text: str) -> str:
    text = clean_nowiki(text)
    text = re.sub(r"\[\[\s*([^|\]]+?)\s*\|\s*(.*?)\s*\]\]", r"\2", text)
    text = re.sub(r"\[\[\s*([^|\]]+?)\s*\]\]", r"\1", text)
    text = re.sub(r"\{\{\s*([^|}]+?)\s*\|\s*(.*?)\s*\}\}", r"\2", text)
    text = re.sub(r"\{\{\s*([^|}]+?)\s*\}\}", r"\1", text)
    text = text.replace("''", "").replace("**", "").replace("//", "")
    return text


def is_standalone_code_markup(line: str) -> bool:
    stripped = line.strip()
    if "''" not in stripped:
        return False
    if "[[" in stripped or "{{" in stripped:
        return False
    prose = re.search(r"\b(the|and|or|with|from|to|in|of|is|are)\b", stripped, flags=re.I)
    return not prose or stripped.startswith("''")


def convert_inline(text: str, current_doc: str = "") -> str:
    text = text.rstrip()
    text = text.replace("\\\\", "")
    store: list[str] = []

    def keep(value: str) -> str:
        store.append(value)
        return f"\x00K{len(store) - 1}\x00"

    def literal_repl(match: re.Match[str]) -> str:
        return keep(f"``{clean_nowiki(match.group('lit')).strip()}``")

    def math_repl(match: re.Match[str]) -> str:
        body = match.group("math").strip().replace("`", r"\`")
        return keep(f":math:`{body}`" if body else "")

    # Protect finished constructs in one left-to-right scan so overlapping
    # syntax (math containing '', literals containing $) resolves by position.
    combined = re.compile(
        r"(?<!\\)\$(?P<math>[^$\n]+?)(?<!\\)\$"
        r"|''(?P<lit>.*?)''"
        r"|<sub>(?P<sub>.*?)</sub>"
        r"|<sup>(?P<sup>.*?)</sup>"
        r"|\[\[\s*(?P<ltarget>[^|\]]+?)\s*\|\s*(?P<llabel>.*?)\s*\]\]"
        r"|\[\[\s*(?P<target2>[^|\]]+?)\s*\]\]"
        r"|\{\{\s*(?P<media>[^}|]+?)\s*(?:\|\s*(?P<mlabel>.*?)\s*)?\}\}"
    )

    def protect_repl(match: re.Match[str]) -> str:
        if match.group("lit") is not None:
            return literal_repl(match)
        if match.group("math") is not None:
            return math_repl(match)
        if match.group("sub") is not None:
            return keep(f":sub:`{match.group('sub').strip()}`")
        if match.group("sup") is not None:
            return keep(f":sup:`{match.group('sup').strip()}`")
        if match.group("ltarget") is not None:
            return keep(convert_link(match.group("ltarget"), match.group("llabel"), current_doc))
        if match.group("target2") is not None:
            return keep(convert_link(match.group("target2"), match.group("target2"), current_doc))
        return keep(convert_image_ref(match.group("media"), match.group("mlabel") or "", block=False))

    text = combined.sub(protect_repl, text)
    text = clean_nowiki(text)

    def bold_repl(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        if re.fullmatch(r"\x00K\d+\x00", body):
            return body  # bold wrapping only a literal: keep the literal bare
        inner = escape_and_emphasize(body)
        # docutils accepts tokens glued directly to the strong delimiters but
        # rejects an escaped space before the closing ``**``, so the outer
        # edges ("/" is an always-allowed neighbour) stay separator-free.
        return keep(f"**{separate_tokens(inner, edge_before='/', edge_after='/')}**")

    def escape_and_emphasize(fragment: str) -> str:
        # Raw asterisks are literal text; //...// is DokuWiki italics.
        fragment = fragment.replace("*", r"\*")

        def italic_repl(match: re.Match[str]) -> str:
            body = match.group(1).strip()
            if re.fullmatch(r"\x00K\d+\x00", body):
                return body  # italics around one token: role/literal stands alone
            return keep(f"*{body}*")

        return re.sub(r"//([^/\n][^/]*?)//", italic_repl, fragment)

    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = escape_and_emphasize(text)
    # A bare pipe would open a substitution reference in reST.
    text = text.replace("|", "\\|")
    text = separate_tokens(text)

    # Restore latest-created placeholders first: outer wrappers (created last)
    # may embed tokens of their inner content (created earlier).
    for i in range(len(store) - 1, -1, -1):
        text = text.replace(f"\x00K{i}\x00", store[i])
    return text


PLACEHOLDER_RE = re.compile(r"\x00K\d+\x00")


def separate_tokens(text: str, edge_before: str = "", edge_after: str = "") -> str:
    """Insert escaped spaces where finished markup tokens violate docutils
    adjacency rules.  While tokens are still placeholders there is no
    asterisk/backtick ambiguity, so boundaries can be fixed reliably."""
    result: list[str] = []
    pos = 0
    for match in PLACEHOLDER_RE.finditer(text):
        result.append(text[pos:match.start()])
        context = "".join(result)
        before = context[-1] if context else edge_before
        if before and before not in PRE_MARKUP_OK:
            result.append("\\ ")
        result.append(match.group(0))
        end = match.end()
        after = text[end] if end < len(text) else edge_after
        if after and after not in POST_MARKUP_OK and after != "*" and after != "\x00":
            result.append("\\ ")
        pos = end
    result.append(text[pos:])
    return "".join(result)


def convert_link(target: str, label: str, current_doc: str = "") -> str:
    target = clean_nowiki(target.strip())
    label = clean_nowiki(label.strip() or target)
    interwiki = re.match(r"^([a-z]+)>(.*)$", target, flags=re.I)
    if interwiki:
        url_template = INTERWIKI.get(interwiki.group(1).lower())
        if url_template:
            return f"`{label} <{url_template.format(interwiki.group(2).strip())}>`__"
    if re.match(r"^[a-z][a-z0-9+.-]*://", target, flags=re.I):
        target = target.replace("<", "%3C").replace(">", "%3E")
        return f"`{label} <{target}>`__"
    if target.startswith("mailto:"):
        return f"`{label} <{target}>`__"
    stem, anchor = normalize_target(target, current_doc)
    if not stem:
        return label
    if anchor:
        return f"`{label} <{stem}.html#{anchor}>`__"
    return f":doc:`{label} <{stem}>`"


def split_table_row(line: str) -> tuple[str, list[str]]:
    marker = line[0]
    body = line[1:]
    if body.endswith(marker):
        body = body[:-1]
    stash: list[str] = []

    def protect(match: re.Match[str]) -> str:
        stash.append(match.group(0))
        return f"\x00P{len(stash) - 1}\x00"

    # {{media|label}} and [[page|label]] contain pipes that must not split cells.
    body = re.sub(r"\{\{[^}|]*\|[^}]*\}\}|\[\[[^]|]*\|[^]]*\]\]", protect, body)
    cells = []
    for cell in body.split(marker):
        for i, value in enumerate(stash):
            cell = cell.replace(f"\x00P{i}\x00", value)
        cells.append(cell.strip())
    return marker, cells


def convert_table(lines: list[str], current_doc: str = "") -> list[str]:
    rows = [split_table_row(line) for line in lines]
    width = max(len(cells) for _, cells in rows)
    normalized = [cells + [""] * (width - len(cells)) for _, cells in rows]
    header_rows = sum(1 for marker, _ in rows if marker == "^")
    header_rows = header_rows if header_rows and header_rows < len(rows) else 0

    out = [".. list-table::"]
    if header_rows:
        out.append(f"   :header-rows: {header_rows}")
    out.append("")
    for cells in normalized:
        converted = [convert_inline(cell, current_doc) for cell in cells]
        out.append(f"   * - {converted[0]}")
        for cell in converted[1:]:
            out.append(f"     - {cell}")
    out.append("")
    return out


def is_table_line(line: str) -> bool:
    return bool(line) and line[0] in {"|", "^"}


def is_indented_code_line(line: str) -> bool:
    return bool(re.match(r"^(?: +|\t)", line)) and convert_list_line(line) is None


def is_punctuation_only(line: str) -> bool:
    return bool(re.match(r"^[.=~^`'\"#*-]{3,}\s*$", line.strip()))


def convert_list_line(line: str, current_doc: str = "") -> str | None:
    match = re.match(r"^(\s+)([*-])\s+(.*)$", line)
    if not match:
        return None
    spaces, marker, body = match.groups()
    depth = max((len(spaces) // 2) - 1, 0)
    bullet = "*" if marker == "*" else "-"
    return f"{'  ' * depth}{bullet} {convert_inline(body, current_doc)}"


def convert_block_math(first_line: str, following: list[str], start: int, consume_first: bool = True) -> tuple[list[str], int, str]:
    if "$$" not in first_line:
        return [], start, first_line
    body = first_line.split("$$", 1)[1]
    consumed = start + 1 if consume_first else start
    math_lines: list[str] = []
    suffix = ""
    if "$$" in body:
        before, suffix = body.split("$$", 1)
        math_lines.append(before)
    else:
        math_lines.append(body)
        while consumed < len(following):
            line = following[consumed]
            consumed += 1
            if "$$" in line:
                before, suffix = line.split("$$", 1)
                math_lines.append(before)
                break
            math_lines.append(line)
    meaningful = [line.rstrip() for line in math_lines if line.strip() and line.strip() not in {",", ".", ",."}]
    if not meaningful:
        return [], consumed, suffix
    out = [".. math::", ""]
    out.extend(f"   {line}" for line in meaningful)
    out.append("")
    return out, consumed, suffix


def convert_page(source: Path, docname: str) -> str:
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    previous_was_list = False
    heading_index = 0
    last_list_depth = 0
    label_counts: dict[str, int] = {}

    for anchor in sorted(ANCHOR_ALIASES.get(docname, set())):
        out.extend([".. raw:: html", "", f'   <span id="{anchor}"></span>', ""])

    def ensure_blank() -> None:
        if out and out[-1] != "":
            out.append("")

    # Map each heading (in order of appearance) onto a nesting-consistent
    # reST level: a section may be at most one level deeper than the open
    # parent, even if the wiki source jumps levels.
    level_seq: list[int] = []
    open_stack: list[int] = []
    for ln in lines:
        m = re.match(r"^(={2,6})\s*(.*?)\s*\1\s*$", ln)
        if not m:
            continue
        doku = len(m.group(1))
        while open_stack and open_stack[-1] >= doku:
            open_stack.pop()
        open_stack.append(doku)
        level_seq.append(min(len(open_stack), 5))

    while i < len(lines):
        line = lines[i].rstrip("\n")

        code_start = re.match(r"^<code(?:\s+-\s+([^>]+))?>\s*$", line)
        if code_start:
            if previous_was_list:
                out.append("")
                previous_was_list = False
            ensure_blank()
            caption = code_start.group(1)
            if caption:
                out.extend([f".. code-block:: text", f"   :caption: {caption.strip()}", ""])
            else:
                out.extend([".. code-block:: text", ""])
            in_code = True
            i += 1
            continue

        if line.strip() == "</code>":
            out.append("")
            in_code = False
            i += 1
            continue

        if in_code:
            out.append(f"   {line}")
            i += 1
            continue

        heading = re.match(r"^(={2,6})\s*(.*?)\s*\1\s*$", line)
        if heading:
            if previous_was_list:
                out.append("")
                previous_was_list = False
            ensure_blank()
            level = 7 - level_seq[heading_index]
            heading_index += 1
            title = clean_nowiki(heading.group(2).strip())
            # docutils reads a leading "•" as a bullet marker, and raw "*" as
            # emphasis, so strip/escape before the title reaches reST.
            title = re.sub(r"^[•‣⁃]\s*", "", title)
            title = title.replace("*", r"\*").replace("|", r"\|").replace("`", r"\`")
            anchor = slugify_anchor(title)
            count = label_counts.get(anchor, 0)
            label_counts[anchor] = count + 1
            label = f"{docname}--{anchor}" if count == 0 else f"{docname}--{anchor}-{count}"
            out.extend([f".. _{label}:", ""])
            out.extend(rst_heading(title, level))
            i += 1
            continue

        block_image = re.match(r"^\s*\{\{\s*([^}]+?)\s*\}\}\s*$", line)
        if block_image:
            if previous_was_list:
                out.append("")
                previous_was_list = False
            ensure_blank()
            inner = block_image.group(1)
            if "|" in inner:
                image_target, image_label = inner.split("|", 1)
            else:
                image_target, image_label = inner, ""
            out.extend(convert_image_ref(image_target, image_label, block=True).splitlines())
            out.append("")
            i += 1
            continue

        if "$$" in line:
            if previous_was_list:
                out.append("")
                previous_was_list = False
            prefix = line.split("$$", 1)[0]
            if prefix.strip():
                out.append(convert_inline(prefix.strip(), docname))
                ensure_blank()
            converted, i, suffix = convert_block_math(line, lines, i)
            out.extend(converted)
            suffix_iterations = 0
            while "$$" in suffix:
                suffix_iterations += 1
                if suffix_iterations > 20:
                    out.append(convert_inline(suffix.strip(), docname))
                    suffix = ""
                    break
                previous_suffix = suffix
                previous_i = i
                prefix = suffix.split("$$", 1)[0]
                if prefix.strip():
                    out.append(convert_inline(prefix.strip(), docname))
                    ensure_blank()
                converted, i, suffix = convert_block_math(suffix, lines, i, consume_first=False)
                out.extend(converted)
                if i == previous_i and suffix == previous_suffix:
                    out.append(convert_inline(suffix.strip(), docname))
                    suffix = ""
                    break
            if suffix.strip():
                out.append(convert_inline(suffix.strip(), docname))
            continue

        if is_table_line(line):
            if previous_was_list:
                out.append("")
                previous_was_list = False
            ensure_blank()
            table_lines = []
            while i < len(lines) and is_table_line(lines[i]):
                table_lines.append(lines[i].rstrip())
                i += 1
            out.extend(convert_table(table_lines, docname))
            continue

        list_line = convert_list_line(line, docname)
        if list_line is not None:
            indent = len(line) - len(line.lstrip())
            depth = max(indent // 2 - 1, 0)
            if previous_was_list:
                # docutils needs a blank line before a deeper nested list.
                if depth > last_list_depth:
                    out.append("")
            elif out and out[-1] != "":
                out.append("")
            out.append(list_line)
            previous_was_list = True
            last_list_depth = depth
            i += 1
            continue

        if is_indented_code_line(line):
            if previous_was_list:
                out.append("")
                previous_was_list = False
            ensure_blank()
            out.extend([".. code-block:: text", ""])
            while i < len(lines) and (is_indented_code_line(lines[i]) or not lines[i].strip()):
                out.append(f"   {lines[i].rstrip()}" if lines[i].strip() else "")
                i += 1
            out.append("")
            continue

        if is_standalone_code_markup(line):
            if previous_was_list:
                out.append("")
                previous_was_list = False
            out.append(f"``{strip_doku_markup(line).strip()}``")
            i += 1
            continue

        if not line.strip():
            out.append("")
            previous_was_list = False
        elif is_punctuation_only(line):
            if previous_was_list:
                out.append("")
                previous_was_list = False
            out.append("\\" + line.strip())
        else:
            if previous_was_list:
                out.append("")
                previous_was_list = False
            # DokuWiki markup may span line breaks; reST inline markup may not,
            # so append continuation lines until the markup is balanced.
            text_line = line.strip()
            while has_unbalanced_markup(text_line) and i + 1 < len(lines):
                nxt = lines[i + 1]
                if (
                    not nxt.strip()
                    or is_table_line(nxt)
                    or convert_list_line(nxt, docname) is not None
                    or re.match(r"^(={2,6})\s", nxt)
                    or "<code" in nxt
                    or "$$" in nxt
                ):
                    break
                # indented continuation lines are still part of the
                # paragraph when markup is unbalanced (multi-line math)
                text_line += " " + nxt.strip()
                i += 1
            out.append(convert_inline(text_line, docname))
        i += 1

    rendered = "\n".join(out)
    rendered = re.sub(r"\n{3,}", "\n\n", rendered).strip() + "\n"
    return rendered


def write_csv_index(pages: list[Path], source_dir: Path, dest: Path) -> None:
    with dest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["source", "rst", "title"])
        for page in pages:
            rel = page.relative_to(source_dir).as_posix()
            writer.writerow([rel, f"{docname_for_stem(page_stem(page))}.rst", page_title(page.read_text(encoding="utf-8"), page_stem(page))])


def build_index(pages: list[Path], source_dir: Path, dest: Path) -> None:
    titles = {docname_for_stem(page_stem(page)): page_title(page.read_text(encoding="utf-8"), page_stem(page)) for page in pages}
    toc = ["Molpro Manual", "=============", "", ".. toctree::", "   :maxdepth: 2", "   :caption: Contents", ""]

    preferred = ["how_to_read_this_manual", "introduction_to_molpro", "installation_guide", "general_program_structure"]
    ordered_stems = []
    for stem in preferred:
        if stem in titles:
            ordered_stems.append(stem)
    ordered_stems.extend(stem for stem in sorted(titles) if stem not in ordered_stems and stem != "manual_index")
    if "manual_index" in titles:
        ordered_stems.append("manual_index")

    toc.extend(f"   {stem}" for stem in ordered_stems)
    toc.append("")
    dest.write_text("\n".join(toc), encoding="utf-8")


def build_page_aliases(pages: list[Path]) -> None:
    PAGE_ALIASES.clear()
    for page in pages:
        stem = page_stem(page)
        docname = docname_for_stem(stem)
        title = page_title(page.read_text(encoding="utf-8"), stem)
        aliases = {
            stem,
            stem.replace("_", " "),
            stem.replace("-", " "),
            title,
            re.sub(r"\s*\([^)]*\)\s*", " ", title),
        }
        for alias in aliases:
            key = normalize_lookup_key(alias)
            if key:
                PAGE_ALIASES[key] = docname


def collect_anchor_aliases(pages: list[Path]) -> None:
    ANCHOR_ALIASES.clear()
    for page in pages:
        current_doc = docname_for_stem(page_stem(page))
        text = page.read_text(encoding="utf-8")
        for match in re.finditer(r"\[\[\s*([^|\]]+?)\s*(?:\|.*?)?\]\]", text):
            target = clean_nowiki(match.group(1).strip())
            if is_external_target(target) or "#" not in target:
                continue
            docname, anchor = normalize_target(target, current_doc)
            if docname and anchor:
                ANCHOR_ALIASES.setdefault(docname, set()).add(anchor)


def remove_previous_conversion(docs_dir: Path) -> None:
    source_map = docs_dir / "source-map.csv"
    if not source_map.exists():
        return

    docs_root = docs_dir.resolve()
    with source_map.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rst_path = row.get("rst")
            if not rst_path:
                continue
            target = (docs_dir / rst_path).resolve()
            try:
                target.relative_to(docs_root)
            except ValueError:
                continue
            if target.suffix == ".rst" and target.is_file():
                target.unlink()


def convert(source_dir: Path, docs_dir: Path) -> None:
    docs_dir.mkdir(parents=True, exist_ok=True)
    remove_previous_conversion(docs_dir)
    for stem in SKIP_STEMS:
        stale = docs_dir / f"{docname_for_stem(stem)}.rst"
        if stale.exists():
            stale.unlink()

    load_media_map(source_dir)
    media_dest = docs_dir / "media"
    if (source_dir / "media").is_dir():
        if media_dest.exists():
            shutil.rmtree(media_dest)
        shutil.copytree(source_dir / "media", media_dest)

    pages = sorted(
        p
        for p in source_dir.glob("*.txt")
        if docname_for_stem(page_stem(p)) not in SKIP_STEMS
    )
    build_page_aliases(pages)
    collect_anchor_aliases(pages)
    for page in pages:
        docname = docname_for_stem(page_stem(page))
        (docs_dir / f"{docname}.rst").write_text(convert_page(page, docname), encoding="utf-8")

    build_index(pages, source_dir, docs_dir / "index.rst")
    write_csv_index(pages, source_dir, docs_dir / "source-map.csv")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="pages/2026-06-05", type=Path)
    parser.add_argument("--docs", default="docs", type=Path)
    args = parser.parse_args()
    convert(args.source, args.docs)


if __name__ == "__main__":
    main()
