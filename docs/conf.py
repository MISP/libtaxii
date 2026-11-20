# Copyright (c) 2017, The MITRE Corporation
# For license information, see the LICENSE.txt file

import sys
from pathlib import Path

import libtaxii

sys.path.insert(0, str(Path(__file__).resolve().parent))

project = u'libtaxii'
copyright = u'2017, The MITRE Corporation'
version = libtaxii.__version__
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'render_api',
]

source_suffix = '.rst'
root_doc = 'index'
html_permalinks = False

exclude_patterns = [
    '_build',
    '_book',
]
