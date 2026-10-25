import os
import sys

project = "Molpro Manual"
author = "Molpro"
language = "en"

# The switcher must reflect the language actually being built, but -D
# overrides are applied after conf.py runs, so read them from the command
# line (sphinx-build is always the entry point, including on Read the Docs).
_cli_language = next(
    (arg.split("=", 1)[1] for arg in sys.argv if arg.startswith("language=")),
    "",
)
_effective = _cli_language or os.environ.get("SPHINX_LANGUAGE", "") or language
if _effective.startswith("zh"):
    html_context = {"language_switch_url": "../index.html", "language_switch_label": "English"}
else:
    html_context = {"language_switch_url": "zh_CN/index.html", "language_switch_label": "中文"}

extensions = ["sphinx.ext.mathjax"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_sidebars = {"**": ["sidebar-nav-bs.html"]}
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["language-switch", "theme-switcher"],
    "navigation_depth": 4,
    "show_toc_level": 2,
    "secondary_sidebar_items": ["page-toc"],
}
gettext_compact = False
locale_dirs = ["locale/"]
source_suffix = ".rst"
nitpicky = False
