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

from openwastetracelib.objects import Azienda
import unittest
import random


class TestAzienda(unittest.TestCase):
    """ Base test for Azienda object. """

    def setUp(self):
        """ Create basic Azienda object """
        ragioneSociale = "Ragione Sociale S.r.l."
#        codiceFiscale = "1234567890"
        codiceFiscale = str(random.random()).split(".")[1]
#        versione = 1
        versione = random.randint(1, 9)
#        idSIS = "12345"
        idSIS = str(random.random()).split(".")[1]
        self.azienda = Azienda(ragioneSociale, codiceFiscale, versione, idSIS)

    def test_extra_attribute(self):
        """ Test adding of attribute pIVA"""
#        self.azienda.pIva = "0987654321"
        self.azienda.pIva = str(random.random()).split(".")[1]

if __name__ == '__main__':
    unittest.main()
