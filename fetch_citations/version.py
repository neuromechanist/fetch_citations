from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 4 - Beta",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "fetch_citations: a simple interface to Google Scholar to fetch citation numbers and lists."
# Long description will go up on the pypi page
long_description = """

fetch_citations
===============
fetch_citations is a simple interface to Google Scholar to fetch citation numbers and lists.

It is part of the NEMAR project, and is designed to be used in conjunction with the NEMAR database.
However, it can be used independently of the NEMAR project, with any list of queries for which you would like
to fetch citation numbers and lists.

It uses the `scholarly` package to interact with the Google Scholar API.
It also uses the `pandas` package to create and manipulate dataframes. You can install these packages using pip:

    ``` bash
    pip install scholarly pandas
    ```
For the best results, you should also initialize the proxy using the `get_working_proxy` function.
This function requires a paid API key. You can get a key from ScrapreAPI, and then use it to initialize the proxy.

The `get_citation_numbers` function retrieves the total number of citations for a given dataset.
The `get_citations` function retrieves the detailed citation information for a given dataset.

(c) 2024, Seyed Yahya Shirazi, Swartz Center for Computational Neuroscience, University of California, San Diego
"""

NAME = "fetch_citations"
MAINTAINER = "Seyed Yahya Shirazi"
MAINTAINER_EMAIL = "shirazi@ieee.org"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/neuromechanist/fetch_citations"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Seyed Yahya Shirazi"
AUTHOR_EMAIL = "shirazi@ieee.org"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'fetch_citations': [pjoin('data', '*')]}
REQUIRES = ["pandas", "scholarly"]
PYTHON_REQUIRES = ">= 3.9"
