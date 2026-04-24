# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IPerSense Workshop Series'
copyright = '2026 Cyber-Physical Mobility Group'
author = 'Simon Schäfer'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['sphinx_rtd_theme', 'sphinx_copybutton', 'sphinx.ext.autosummary']
extensions = ['sphinxawesome_theme', 'sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', 'public']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'IPerSense'

# html_theme = 'sphinx_rtd_theme' 
html_theme = 'sphinxawesome_theme'

html_permalinks = False

# Set via environment in CI/CD to generate absolute social/canonical links.
# Example: DOCS_BASEURL=https://example.org
html_baseurl = os.environ.get('DOCS_BASEURL', 'https://bassamlab.github.io/IPerSys/')

html_static_path = ['_static']
html_css_files = ['custom.css']

html_context = {
  'social_description': 'IPerSense Workshop Series on infrastructure-based and integrated perception for intelligent mobility.',
  'social_image': 'images/cover.png',
}

_baseurl = html_baseurl.rstrip('/')
_nav_itsc = f"{_baseurl}/workshops/itsc_2026.html"
_nav_about = f"{_baseurl}/about.html"

html_theme_options = {
    "show_breadcrumbs": True,
    "awesome_external_links": True,       
    "main_nav_links": {
        "ITSC 2026 Workshop": _nav_itsc,
        "The Organizers": _nav_about,
   },
   "show_prev_next": False,
   "show_scrolltop": False,
   "logo_light": "images/logo-01.svg",
   "logo_dark": "images/logo-02.svg",
}

html_sidebars = {
  "**": ["sidebar_main_nav_links.html"]
}
