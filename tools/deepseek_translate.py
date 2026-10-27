"""Translate translate_work/*.jsonl via the DeepSeek API (openai-compatible).

Same output contract as the subagent flow: <page>.out.jsonl with
{"i": <n>, "msgstr": "<chinese>"}. Resumable: per-page, skips entries whose
i is already present in the output file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path

from openai import OpenAI

RULES = """You translate gettext entries of the Molpro quantum-chemistry manual (Sphinx reStructuredText) from English to Simplified Chinese.
Rules:
1. Preserve reST markup EXACTLY: ``code`` (contents unchanged), :math:`...` (LaTeX byte-identical), *italic*, **bold**, `label <target>`__ (translate ONLY the label, never the target), :doc:`x <y>`, escapes like \\* \\| \\_.
2. Acronyms/program names (Molpro, CCSD(T), CASSCF, MRCI, DFT, SCF, MP2, CASPT2, B3LYP, KS-RPA ...) stay in English. Person names stay.
3. Literature citations (authors + journal like "J. Chem. Phys." + volume/year) -> return msgid unchanged.
4. Entries that are pure code, numbers or symbols -> return msgid unchanged.
5. Simplified Chinese, technical documentation register, full-width punctuation （，。：；、（））, no extra spaces around CJK or markup.
6. Apply the glossary strictly when given.
Return STRICT JSON: {"t": [{"i": <n>, "msgstr": "<chinese>"}, ...]} covering every input item, same i values."""


def load_glossary(path: Path) -> list[tuple[str, str]]:
    rows = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0] and parts[1]:
            rows.append((parts[0], parts[1]))
    return rows


def select_glossary(text: str, glossary: list[tuple[str, str]]) -> str:
    lower = text.lower()
    hits = [f"{en} => {zh}" for en, zh in glossary if en in lower]
    return "\n".join(hits[:40])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work", default="translate_work", type=Path)
    parser.add_argument("--glossary", default="translate_work/glossary.tsv", type=Path)
    parser.add_argument("--batch-size", type=int, default=30)
    parser.add_argument("--pages", default="", help="comma-separated page stems to process (default: all)")
    parser.add_argument("--model", default="deepseek-chat")
    args = parser.parse_args()

    client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
    glossary = load_glossary(args.glossary)
    only = set(args.pages.split(",")) if args.pages else None

    for src in sorted(args.work.glob("*.jsonl")):
        if src.name == "batches.txt" or src.stem == "glossary" or src.stem.endswith(".out"):
            continue
        page = src.stem
        if only and page not in only:
            continue
        out_path = args.work / f"{page}.out.jsonl"
        records = [json.loads(l) for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
        done: dict[int, str] = {}
        if out_path.exists():
            for l in out_path.read_text(encoding="utf-8").splitlines():
                if l.strip():
                    rec = json.loads(l)
                    done[rec["i"]] = rec["msgstr"]
        todo = [r for r in records if r["i"] not in done and re.search(r"[A-Za-z]{3,}", r["msgid"])]
        # pure symbol/code entries: copy without API
        for r in records:
            if r["i"] not in done and not re.search(r"[A-Za-z]{3,}", r["msgid"]):
                done[r["i"]] = r["msgid"]
        print(f"{page}: {len(records)} entries, {len(done)} already done, {len(todo)} to translate", flush=True)
        if not todo:
            if done:
                _save(out_path, records, done)
            continue

        for start in range(0, len(todo), args.batch_size):
            chunk = todo[start : start + args.batch_size]
            items = [{"i": r["i"], "msgid": r["msgid"]} for r in chunk]
            blob = "\n".join(r["msgid"] for r in chunk)
            terms = select_glossary(blob, glossary)
            user_msg = RULES + (f"\n\nGlossary (strict):\n{terms}" if terms else "") + "\n\nEntries (JSON array):\n" + json.dumps(items, ensure_ascii=False)
            for attempt in range(4):
                try:
                    resp = client.chat.completions.create(
                        model=args.model,
                        messages=[{"role": "user", "content": user_msg}],
                        response_format={"type": "json_object"},
                        temperature=1.0,
                    )
                    data = json.loads(resp.choices[0].message.content)
                    for item in data.get("t", []):
                        i, s = item.get("i"), (item.get("msgstr") or "").strip()
                        if isinstance(i, int) and s:
                            done[i] = s
                    break
                except Exception as exc:
                    print(f"  attempt {attempt + 1} failed: {exc}", flush=True)
                    time.sleep(5 * (attempt + 1))
            _save(out_path, records, done)
            print(f"  {min(start + args.batch_size, len(todo))}/{len(todo)}", flush=True)
            time.sleep(0.3)
        _save(out_path, records, done)


def _save(out_path: Path, records: list[dict], done: dict[int, str]) -> None:
    lines = [json.dumps({"i": r["i"], "msgstr": done[r["i"]]}, ensure_ascii=False) for r in records if r["i"] in done]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
