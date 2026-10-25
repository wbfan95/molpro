# Molpro Manual

Sphinx build of the Molpro manual, converted from the DokuWiki source.

- Live site (GitHub Pages): https://wbfan95.github.io/molpro/
- Read the Docs: to be connected (import this repository at readthedocs.org)

## Layout

- `docs/` — Sphinx sources (`rst`), `conf.py`, and `media/` assets
- `tools/convert_dokuwiki_to_sphinx.py` — DokuWiki → reST converter used to
  produce `docs/*.rst` from the crawled wiki pages
- `requirements-docs.txt` — build dependencies

## Build locally

```bash
pip install -r requirements-docs.txt
sphinx-build -b html docs docs/_build/html
```

The build is warning-free; new content should keep it that way.

## Regenerating from the wiki crawl

```bash
python tools/convert_dokuwiki_to_sphinx.py --source pages/<snapshot> --docs docs
```

(The `pages/` crawl snapshots are not committed.)
