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

html_title = 'IPerSense Workshop Series'

# html_theme = 'sphinx_rtd_theme' 
html_theme = 'sphinxawesome_theme'

html_permalinks = False

html_theme_options = {
    "show_breadcrumbs": True,
    "awesome_external_links": True,       
}