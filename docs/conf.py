import os
import sys

sys.path.insert(0, os.path.abspath('..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FixitPy'
copyright = '2026, Michael MacMullen'
author = 'Michael MacMullen'
release = '0.2.21'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    "sphinx_design",
    "sphinx_design_elements",
]

html_theme_options = {
    'logo': 'logo.png',
    'github_user': 'voldgalf',
    'github_repo': 'FixitPy',
    'description': "FixitPy is a uncomplicated Python library for interfacing with iFixit's API. Allowing repair guides to be programmatically retrieved."
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

