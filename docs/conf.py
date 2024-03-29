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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "BioTeam Sphinx Demo"
copyright ="BioTeam Inc"
author = "Jordan Ramsdell"
github_user = "jramsdell"
github_repo_name = "sphinx-documentation-demo"  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/docs/" # with leading and trailing slash

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    "sphinx_design"
]

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
nb_execution_mode = "cache"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
]


# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme" # To install a new theme, you have to pip install it first

html_theme_options = {
  "use_edit_page_button": False,
  "show_toc_level": 4,


  # SHOW_NAV_LEVEL: Normally for the left sidebar, deeply nested items are collapsed.
  #                 We can change the defualt maximum depth by changing the nav level
  "show_nav_level": 2,
#   "navbar_center": ["navbar-nav"],

  # LOGO: This determines the text (and icon, if you have one) that you see
  #       in the upper left-hand corner of the page
  "logo": {
      "text": "BioTeam Sphinx Demo"
  }
}
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]


# HTML context:
from os.path import basename, dirname, realpath


# html_sidebars = {
#     "**": ["globaltoc.html"]
# }

html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

