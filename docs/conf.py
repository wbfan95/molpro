project = "Molpro Manual"
author = "Molpro"
language = "en"
extensions = ["sphinx.ext.mathjax"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_sidebars = {"**": ["sidebar-nav-bs.html"]}
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher"],
    "navigation_depth": 4,
    "show_toc_level": 2,
    "secondary_sidebar_items": ["page-toc"],
}
gettext_compact = False
locale_dirs = ["locale/"]
source_suffix = ".rst"
nitpicky = False
