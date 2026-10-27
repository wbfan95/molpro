"""Merge translator JSONL output back into docs/locale/zh_CN po files.

Reads translate_work/<page>.out.jsonl ({i, msgstr}), maps i back to the
msgid from <page>.jsonl, validates markup balance, applies the same link
repair and CJK adjacency fixes as build_locale, then writes the po.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import polib

sys.path.insert(0, str(Path(__file__).parent))
import build_locale as bl  # noqa: E402
import convert_dokuwiki_to_sphinx as doku  # noqa: E402


def _is_explanation(literal: str) -> bool:
    """Explanation literals (with spaces or CJK text) may be translated;
    identifier literals (``THREN``) must survive unchanged."""
    return bool(re.search(r"\s", literal)) or bool(re.search(r"[\u4e00-\u9fff]", literal))


def markup_issues(msgid: str, msgstr: str) -> list[str]:
    """Structural checks. Link targets and :math: contents must survive
    translation unchanged. Identifier-like literals (no whitespace, e.g.
    ``THREN``) must survive too; explanation literals (with spaces, e.g.
    ``Default: THREN=1.0d-7.``) may be translated, so only their presence
    count is checked."""
    issues = []

    def parts(s: str) -> tuple[Counter, Counter]:
        literals = re.findall(r"``([^`\n]+)``", s)
        strict = Counter(
            re.findall(r"<[^<>\n]+>", s)
            + re.findall(r":math:`([^`]*)`", s)
            + re.findall(r":doc:`[^`]*<([^>]*)>`", s)
            + [lit for lit in literals if not _is_explanation(lit)]
        )
        free = Counter(lit for lit in literals if _is_explanation(lit))
        return strict, free

    strict_id, free_id = parts(msgid)
    strict_st, free_st = parts(msgstr)
    missing = strict_id - strict_st
    if missing:
        issues.append(f"invariants missing={list(missing)[:2]}")
    if free_id and sum(free_st.values()) < sum(free_id.values()) - 1:
        issues.append("free literals collapsed")
    if msgstr.count("`") % 2:
        issues.append("odd backticks")
    if "\\|" in msgid and "\\|" not in msgstr:
        issues.append("lost | escape")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gettext-dir", default="docs/_build/gettext", type=Path)
    parser.add_argument("--work", default="translate_work", type=Path)
    parser.add_argument("--locale", default="docs/locale/zh_CN/LC_MESSAGES", type=Path)
    parser.add_argument("--pages-dir", default="pages/2026-06-05", type=Path)
    args = parser.parse_args()

    doku.build_page_aliases(sorted(args.pages_dir.glob("*.txt")))
    applied = rejected = 0
    for out_path in sorted(args.work.glob("*.out.jsonl")):
        page = out_path.name[: -len(".out.jsonl")]
        src_path = args.work / f"{page}.jsonl"
        id_to_msgid = {
            e["i"]: e["msgid"]
            for e in (json.loads(l) for l in src_path.read_text(encoding="utf-8").splitlines() if l.strip())
        }
        translations: dict[str, str] = {}
        for line in out_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            msgid = id_to_msgid.get(rec["i"])
            msgstr = rec.get("msgstr", "").strip()
            if not msgid or not msgstr:
                continue
            if markup_issues(msgid, msgstr):
                rejected += 1
                continue
            translations[msgid] = bl.fix_cjk_adjacency(bl.repair_dangling_refs(msgstr))

        po_path = args.locale / f"{page}.po"
        pot = polib.pofile(args.gettext_dir / f"{page}.pot")
        if po_path.exists():
            po = polib.pofile(po_path)
            by_msgid = {e.msgid: e for e in po}
        else:
            po = polib.POFile()
            po.metadata = {
                "Project-Id-Version": "Molpro Manual 1.0",
                "Language": "zh_CN",
                "Content-Type": "text/plain; charset=utf-8",
                "Content-Transfer-Encoding": "8bit",
                "Plural-Forms": "nplurals=1; plural=0;",
            }
            by_msgid = {}
        for entry in pot:
            if entry.msgid in translations:
                msgstr = translations[entry.msgid]
                if entry.msgid in by_msgid:
                    by_msgid[entry.msgid].msgstr = msgstr
                else:
                    po.append(polib.POEntry(msgid=entry.msgid, msgstr=msgstr))
                applied += 1
        po.save(po_path)
    print(f"applied: {applied}, rejected by markup check: {rejected}")


if __name__ == "__main__":
    main()
