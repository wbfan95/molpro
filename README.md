# Molpro Manual

Sphinx build of the Molpro manual, converted from the DokuWiki source.

- Live site (GitHub Pages): https://wbfan95.github.io/molpro/
  - Chinese: https://wbfan95.github.io/molpro/zh_CN/ (partial translation, untranslated parts fall back to English)
- Read the Docs: to be connected (import this repository at readthedocs.org)

## Layout

- `docs/` — Sphinx sources (`rst`), `conf.py`, `media/` assets, and
  `locale/zh_CN/LC_MESSAGES/` translations
- `tools/convert_dokuwiki_to_sphinx.py` — DokuWiki → reST converter used to
  produce `docs/*.rst` from the crawled wiki pages
- `tools/build_locale.py` — assembles the Chinese `po` catalogs from an
  earlier translated corpus (exact + normalized msgid matching)
- `requirements-docs.txt` — build dependencies

## Build locally

```bash
pip install -r requirements-docs.txt
sphinx-build -b html docs docs/_build/html                      # English
sphinx-build -b html -D language=zh_CN docs docs/_build/html-zh # Chinese
```

Both builds are warning-free; new content should keep it that way.

## Regenerating from the wiki crawl

```bash
python tools/convert_dokuwiki_to_sphinx.py --source pages/<snapshot> --docs docs
sphinx-build -b gettext docs docs/_build/gettext
python tools/build_locale.py
```

(The `pages/` crawl snapshots are not committed.)
