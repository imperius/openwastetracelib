#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 OpenWasteTrace
 Copyright (C) 2011 Paolo Melchiorre

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from distutils.core import setup
import os
import openwastetracelib

LONG_DESCRIPTION = \
"""A wrapper around Sistri's Web Services Soap API using Suds."""

CLASSIFIERS = [
                'Development Status :: 3 - Alpha',
                'Environment :: Console',
                'Environment :: Web Environment',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Natural Language :: Italian',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules' 
              ]

KEYWORDS = 'sistri soap suds wsdl wrapper'

setup(name = 'OpenWasteTrace',
      version = "0.4",
      description = 'Sistri Web Services Soap API wrapper.',
      long_description = LONG_DESCRIPTION,
      author = 'Paolo Melchiorre',
      author_email = 'paolo.melchiorre@madec.it',
      url = 'http://www.openwastetrace.it',
      download_url = 'http://download.openwastetrace.it',
      packages = ['openwastetracelib'],
      package_dir= {'openwastetracelib': 'openwastetracelib'},
      package_data = {'openwastetracelib': ['wsdl/*.wsdl']},
      platforms = ['Platform Independent'],
      license = 'GPLv3',
      classifiers = CLASSIFIERS,
      keywords = KEYWORDS,
      requires = ['suds'],
     )
