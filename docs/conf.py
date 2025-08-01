import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = 'MABAC Decision Support'
author = 'Laura Białobrzewska'
release = '0.1.0'

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
