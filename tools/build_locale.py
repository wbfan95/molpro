"""Assemble docs/locale/zh_CN from the 2025 translated_po corpus.

Matches old po entries against the pot generated from the current rst:
1. exact msgid match          -> reuse translation verbatim
2. normalized match           -> reuse translation (markup drifted only in
                                 escaped-space separators / link spelling;
                                 old-style link targets in the translation are
                                 rewritten to the new ``page.html#slug`` form)

Unmatched entries are left untranslated (Sphinx falls back to English).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import polib

sys.path.insert(0, str(Path(__file__).parent))
import convert_dokuwiki_to_sphinx as doku  # noqa: E402


def norm(text: str) -> str:
    text = text.replace("\\ ", "")
    text = re.sub(r"<[^<>\n]+>", "", text)  # link/media targets differ between eras
    text = re.sub(r"[\s…,.]+", " ", text)
    return text.strip()


LINK_RE = re.compile(r"`([^`<>\n]+?)\s*<([^<>\n]+?)>`__")

# Inline markup tokens whose boundaries must obey docutils adjacency rules.
TOKEN_RE = re.compile(
    r"``[^`\n]+``"
    r"|:[A-Za-z][A-Za-z0-9+._-]*:`(?:[^`\n]|\\`)+`"
    r"|`[^`\n]+?`__"
    r"|\*\*[^*\n]+?\*\*"
    r"|\*[^*\n]+?\*"
)
PRE_MARKUP_OK = set(" \t'\"([{<-/:\\")
POST_MARKUP_OK = set(" \t'\"')]}>-/:;!?\\,.")


def fix_cjk_adjacency(text: str) -> str:
    """Chinese text abuts inline markup without spaces; docutils rejects
    non-ASCII neighbours, so insert escaped spaces (which render as nothing).
    A neighbouring ``*`` is left alone: markup glued to asterisk delimiters
    parses fine and an escaped space before ``**`` would be invalid."""

    def repair(match: re.Match[str]) -> str:
        start, end = match.span()
        before = text[start - 1] if start else ""
        after = text[end] if end < len(text) else ""
        token = match.group(0)
        prefix = "\\ " if before and before not in PRE_MARKUP_OK and before != "*" else ""
        suffix = "\\ " if after and after not in POST_MARKUP_OK and after != "*" else ""
        return f"{prefix}{token}{suffix}"

    return TOKEN_RE.sub(repair, text)


def modernize_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2).strip()
        if re.match(r"^[a-z][a-z0-9+.-]*://", target) or target.startswith(("mailto:", "media/")):
            return match.group(0)
        if "#" in target:
            page, anchor = target.split("#", 1)
            stem = doku.normalize_target(page)[0]
            slug = doku.slugify_anchor(anchor)
            return f"`{label} <{stem}.html#{slug}>`__"
        stem = doku.normalize_target(target)[0]
        return f"`{label} <{stem}.html>`__"

    return LINK_RE.sub(repl, text)


DANGLING_HASH_REF = re.compile(r"`([^`\n<]*#[^`\n<]*)>`__")
BARE_REF = re.compile(r"`([^`<>\n]+?)`__")


def repair_dangling_refs(text: str) -> str:
    """Fix translator-mangled references: `` `Page#Anchor>`__`` lost its
    ``label <`` half, and some bare `` `x`__`` refs never had a target."""

    def hash_repl(match: re.Match[str]) -> str:
        content = match.group(1).strip().rstrip(">").strip()
        page, _, anchor = content.partition("#")
        stem = doku.normalize_target(page)[0]
        slug = doku.slugify_anchor(anchor)
        return f"`{page.strip()} <{stem}.html#{slug}>`__"

    text = DANGLING_HASH_REF.sub(hash_repl, text)

    def bare_repl(match: re.Match[str]) -> str:
        content = match.group(1).strip()
        resolved = doku.PAGE_ALIASES.get(doku.normalize_lookup_key(content))
        if resolved:
            return f"`{content} <{resolved}.html>`__"
        return content  # no valid target anywhere: degrade to plain text

    return BARE_REF.sub(bare_repl, text)


def build_page(pot_path: Path, old_po_path: Path | None, dest_dir: Path) -> tuple[int, int]:
    pot = polib.pofile(pot_path)
    entries = [e for e in pot if e.msgid]
    old_by_exact: dict[str, str] = {}
    old_by_norm: dict[str, str] = {}
    used_norm: set[str] = set()
    if old_po_path and old_po_path.exists():
        old = polib.pofile(old_po_path)
        for e in old:
            if e.msgstr and not e.obsolete and e.msgid:
                old_by_exact.setdefault(e.msgid, e.msgstr)
                old_by_norm.setdefault(norm(e.msgid), e.msgstr)

    po = polib.POFile()
    po.metadata = {
        "Project-Id-Version": "Molpro Manual 1.0",
        "Language": "zh_CN",
        "Language-Team": "zh_CN",
        "MIME-Version": "1.0",
        "Content-Type": "text/plain; charset=utf-8",
        "Content-Transfer-Encoding": "8bit",
        "Plural-Forms": "nplurals=1; plural=0;",
    }
    exact = normalized = 0
    for entry in entries:
        msgstr = old_by_exact.get(entry.msgid)
        if msgstr is not None:
            exact += 1
        else:
            key = norm(entry.msgid)
            candidate = old_by_norm.get(key)
            if candidate is not None and key not in used_norm:
                msgstr = modernize_links(candidate)
                normalized += 1
        if msgstr:
            msgstr = fix_cjk_adjacency(repair_dangling_refs(msgstr))
            po.append(polib.POEntry(msgid=entry.msgid, msgstr=msgstr))
    dest = dest_dir / (pot_path.stem + ".po")
    po.save(dest)
    return exact, normalized


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gettext-dir", default="docs/_build/gettext", type=Path)
    parser.add_argument("--old-po-dir", default=r"D:\20250710 molpro manual\translated_po", type=Path)
    parser.add_argument("--pages-dir", default="pages/2026-06-05", type=Path)
    parser.add_argument("--dest", default="docs/locale/zh_CN/LC_MESSAGES", type=Path)
    args = parser.parse_args()

    doku.build_page_aliases(sorted(args.pages_dir.glob("*.txt")))
    args.dest.mkdir(parents=True, exist_ok=True)

    total = t_exact = t_norm = 0
    for pot_path in sorted(args.gettext_dir.glob("*.pot")):
        pot = polib.pofile(pot_path)
        n_entries = sum(1 for e in pot if e.msgid)
        exact, normalized = build_page(pot_path, args.old_po_dir / (pot_path.stem + ".po"), args.dest)
        total += n_entries
        t_exact += exact
        t_norm += normalized
    print(f"entries: {total}, exact: {t_exact}, normalized: {t_norm}, "
          f"translated: {(t_exact + t_norm) / total:.1%}")


if __name__ == "__main__":
    main()
