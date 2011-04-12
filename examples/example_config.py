#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre <paolo.melchiorre@madec.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This file holds various configuration options used for all of the examples.
You will need to change the values below to match your test account.
"""

from openwastetracelib.config import OWTConfig

# Change these values to match your account credentials.
CONFIG_OBJ = OWTConfig(certificate = "/tmp/Certificate.cer",
                       privatekey = "/tmp/Private.pem",
                       dbstring = "sqlite:///:memory:",
                       wsdl = "https://sisssl.sistri.it/SIS/services/SIS?wsdl")
