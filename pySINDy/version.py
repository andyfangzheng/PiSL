# pylint: skip-file

from __future__ import absolute_import, division, print_function
from os.path import join

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 2
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "PySINDy: a Python project on Sparse Identification of Nonlinear Dynamics"
# Long description will go up on the pypi page
long_description = """
PySINDy
========
PySINDy is a a Python project on Sparse Identification of Nonlinear Dynamics.
It contains software implementations of SINDy-related algorithms which are used 
 for system identification and mainly developed by Steve Brunton & Nathan Kutz. 
 But more importantly, it contains infrastructure for testing, documentation,
continuous integration and deployment, which can be easily adapted
to use in other projects.
To get started using these components in your own software, please go to the
repository README https://github.com/luckystarufo/pySINDy/blob/master/README.md


License
=======
pySINDy is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
All trademarks referenced herein are property of their respective holders.
Copyright (c) 2018--, Yuying Liu, The University of Washington Applied Mathematics
Department.
"""

NAME = "PySINDy"
MAINTAINER = "Yuying Liu"
MAINTAINER_EMAIL = "liuyuyingufo@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/luckystarufo/pySINDy"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Yuying Liu"
AUTHOR_EMAIL = "liuyuyingufo@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'pySINDy': [join('data', '*')]}
REQUIRES = ["numpy", "findiff"]
