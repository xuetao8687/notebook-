# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os


# -- Project information -----------------------------------------------------

project = u'Notebook' 
copyright = u'2021, RYAN'
author = u'<a href="https://example.com">RYAN</a>'
version = 'v 1.2.0'

master_doc = 'index'
language = 'zh_CN'
source_encoding = 'utf-8-sig'
source_suffix = ['.rst','.md']


# -- General configuration ------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('_exts'))

# Add any Sphinx extension module names here
# WARNING: Do not modify the order unless you know what will happen!!!
extensions = [
    'chinese_search',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'myst_nb',
    'sphinx_togglebutton',
    'sphinx_copybutton',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinxcontrib.mermaid',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    'sphinx_autodoc_typehints',
    'sphinx_panels',
    'sphinx_tabs.tabs',
    'sphinxcontrib.bibtex',
]


# -- Options for HTML output -------------------------------------------------

html_title = ''
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static'] # Contain custom static files (such as style sheets) here
html_css_files = ['css/custom.css',] # These paths are either relative to html_static_path or or fully qualified paths (eg. https://...)
html_sourcelink_suffix = '.rst'


# -- Options for LaTeX output ---------------------------------------------

# Comment this sentence when gernerating a HTML page package.
latex_engine = 'xelatex'

# Grouping the document tree into LaTeX files. List of tuples
latex_documents = [
    (master_doc,                # source_start_file
    'Notebook.tex',             # target_name
    'Notebook Documentation',   # title
    'RYAN',                     # author
    'manual'),                  # documentclass [howto, manual, or own class]
]

# To generate Chinese PDF, you need to add the following code.
latex_elements = {
    'preamble': r'''
    \usepackage[UTF8]{ctex}
    ''',
    'extraclassoptions': 'openany, oneside',
}


# -- Options for Extensions -------------------------------------------------

# Setting for sphinx.ext.autosummary to auto-generate single html pages
# Please makesure all api pages are stored in `/reference/api/` directory
# See `Makefile` for more detail.
autosummary_generate = True

# Setting for sphinx.ext.auotdoc
autodoc_default_options = {"member-order": "bysource"}
autoclass_content = "class"
autodoc_docstring_signature = True
autodoc_preserve_defaults = True
autodoc_mock_imports = ["mprop"]

# Setting for sphinx.ext.mathjax
# The path to the JavaScript file to include in the HTML files in order to load MathJax.
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# Setting for sphinxcontrib-mermaid
mermaid_version = "latest"  # from CDN unpkg.com

# Setting for sphinx.ext.intersphinx
# Useful for refenrece other projects, eg. :py:class:`zipfile.ZipFile`
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pytorch": ("https://pytorch.org/docs/stable/", None),
    "jb": ("https://jupyterbook.org/", None),
    "myst": ("https://myst-parser.readthedocs.io/en/latest/", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
    "nbclient": ("https://nbclient.readthedocs.io/en/latest", None),
    "nbformat": ("https://nbformat.readthedocs.io/en/latest", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
intersphinx_cache_limit = 5

# Setting for sphinx.ext.extlinks
# Can use the alias name as a new role, e.g. :issue:`123`
extlinks = {
    "src": ("https://github.com/zhyantao/readthedocs-with-github/blob/master/%s", ""),
    "docs": ("https://github.com/zhyantao/readthedocs-with-github/blob/master/%s", ""),
    "issue": ("https://github.com/zhyantao/readthedocs-with-github/issues/%s", "Issue #"),
    "pull": ("https://github.com/zhyantao/readthedocs-with-github/pull/%s", "Pull Requset #"),
    "duref": ("http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#%s", "",),
}

# Setting for sphinx_autodoc_typehints
typehints_fully_qualified = False

# Setting for sphinx_copybutton
copybutton_prompt_text = r">>> |\.\.\. |(?:\(.*\) )?\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Setting for sphinx_panels
panels_add_bootstrap_css = True

# Setting for myst_nb
suppress_warnings = ['myst.domains']
numfig = True
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]
panels_add_bootstrap_css = False

nb_custom_formats = {
  ".Rmd": ["jupytext.reads", {"fmt": "Rmd"}]
}

jupyter_execute_notebooks = "cache"
execution_show_tb = "READTHEDOCS" in os.environ
execution_timeout = 60  # Note: 30 was timing out on RTD

# Setting for PlantUML
CURRENT_DIR = os.path.abspath('.')
plantuml = f'java -jar {CURRENT_DIR}/_static/lib/plantuml.jar'
plantuml_output_format = 'svg'

# Setting for sphinxcontrib.bibtex
bibtex_bibfiles = ['refs.bib']
