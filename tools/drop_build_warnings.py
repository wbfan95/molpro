"""Build-driven QC: rebuild zh, map each warning back to its po entry via pot
occurrences, drop those translations (English fallback). Repeat until clean.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import polib

ANSI = re.compile(r"\x1b\[[0-9;]*m")


def build_and_collect(docs: Path) -> list[str]:
    proc = subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "html", "-E", "-D", "language=zh_CN", str(docs), str(docs / "_build" / "html-zh")],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    out = []
    for line in (proc.stdout + proc.stderr).splitlines():
        line = ANSI.sub("", line)
        if "WARNING" in line or "ERROR" in line:
            out.append(line)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", default="docs", type=Path)
    parser.add_argument("--gettext-dir", default="docs/_build/gettext", type=Path)
    parser.add_argument("--locale", default="docs/locale/zh_CN/LC_MESSAGES", type=Path)
    parser.add_argument("--max-rounds", type=int, default=4)
    args = parser.parse_args()

    # page -> line -> [(po_path, msgid)]
    index: dict[str, dict[int, list[tuple[Path, str]]]] = {}
    for pot_path in args.gettext_dir.glob("*.pot"):
        pot = polib.pofile(pot_path)
        po_path = args.locale / f"{pot_path.stem}.po"
        if not po_path.exists():
            continue
        po = polib.pofile(po_path)
        by_msgid = {e.msgid: e for e in po}
        for entry in pot:
            target = by_msgid.get(entry.msgid)
            if target is None or not target.msgstr:
                continue
            for fname, lineno in entry.occurrences:
                page = Path(fname).stem
                index.setdefault(page, {}).setdefault(int(lineno), []).append((po_path, entry.msgid))

    total_dropped = 0
    for rnd in range(1, args.max_rounds + 1):
        warnings = build_and_collect(args.docs)
        if not warnings:
            print(f"round {rnd}: clean build, zero warnings (total dropped: {total_dropped})")
            return
        victims: dict[Path, set[str]] = {}
        unmatched = 0
        loc = re.compile(r"docs[/\\](?P<page>[^:]+?)\.rst:(?P<line>\d+):")
        for line in warnings:
            m = loc.search(line)
            if not m:
                unmatched += 1
                continue
            page, lineno = m.group("page"), int(m.group("line"))
            hits = index.get(page, {}).get(lineno, [])
            if not hits:
                unmatched += 1
                continue
            for po_path, msgid in hits:
                victims.setdefault(po_path, set()).add(msgid)
        if not victims:
            print(f"round {rnd}: {len(warnings)} warnings but no entries matched (unmatched {unmatched}); stopping")
            return
        for po_path, msgids in victims.items():
            po = polib.pofile(po_path)
            changed = 0
            for e in po:
                if e.msgid in msgids and e.msgstr:
                    e.msgstr = ""
                    changed += 1
            if changed:
                po.save(po_path)
        total_dropped += sum(len(m) for m in victims.values())
        print(f"round {rnd}: {len(warnings)} warnings, dropped {sum(len(m) for m in victims.values())} entries, unmatched {unmatched}")
    print(f"final check: {len(build_and_collect(args.docs))} warnings remain after {total_dropped} drops")


if __name__ == "__main__":
    main()
