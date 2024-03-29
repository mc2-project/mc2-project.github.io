# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

curr_path = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))
libpath = os.path.join(curr_path, "../python-package/")
sys.path.insert(0, libpath)
sys.path.insert(0, curr_path)


# -- Project information -----------------------------------------------------

project = "MC<sup>2</sup>"
copyright = "2021, MC² Contributors"
author = "MC² Contributors"

# The full version, including alpha/beta/rc tags
#  release = "0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    #  "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinxarg.ext",
    "sphinx_copybutton",
    "sphinxcontrib.spelling",
    "sphinx-prompt",
    "sphinx_substitution_extensions"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#00B0FF",
        "color-brand-content": "#00B0FF",
        "color-admonition-background": "orange",
    },
    "sidebar_hide_name": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Path to logo
html_logo = "images/logo.png"

# Path to favicon
html_favicon = "images/favicon.png"

# Correctly spelled words to be ignored during spellcheck
spelling_word_list_filename = "spelling_wordlist.txt"

# Emit misspelling as Sphinx warning
spelling_warning = True

# -------- Substitutions ----------------------------
rst_prolog = """
.. |platform| replace:: MC\ :sup:`2`
.. |platform_uppercase| replace:: MC2
.. |github-org| replace:: mc2-project
.. |github-repo| replace:: mc2
.. |cmd| replace:: mc2
.. |python-package| replace:: mc2client
.. |python-package-short| replace:: mc2
.. |release_version| replace:: 0.1.3
.. |docker-org| replace:: mc2project
"""
