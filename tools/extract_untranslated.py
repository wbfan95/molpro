"""Extract untranslated pot entries into per-page JSONL work files.

Output: translate_work/<page>.jsonl with {"i": <n>, "msgid": "<text>"} lines,
numbered per page. Translators write sibling <page>.out.jsonl files with
{"i": <n>, "msgstr": "<text>"}.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import polib


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gettext-dir", default="docs/_build/gettext", type=Path)
    parser.add_argument("--locale", default="docs/locale/zh_CN/LC_MESSAGES", type=Path)
    parser.add_argument("--work", default="translate_work", type=Path)
    args = parser.parse_args()

    args.work.mkdir(exist_ok=True)
    total = extracted = 0
    for pot_path in sorted(args.gettext_dir.glob("*.pot")):
        po_path = args.locale / (pot_path.stem + ".po")
        existing: dict[str, str] = {}
        if po_path.exists():
            po = polib.pofile(po_path)
            existing = {e.msgid: e.msgstr for e in po if e.msgstr}
        pot = polib.pofile(pot_path)
        entries = []
        i = 0
        for entry in pot:
            if not entry.msgid or entry.msgid in existing:
                continue
            entries.append({"i": i, "msgid": entry.msgid})
            i += 1
        total += len([e for e in pot if e.msgid])
        extracted += len(entries)
        if entries:
            (args.work / f"{pot_path.stem}.jsonl").write_text(
                "\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n",
                encoding="utf-8",
            )
    print(f"total pot entries: {total}, untranslated extracted: {extracted}")


if __name__ == "__main__":
    main()
