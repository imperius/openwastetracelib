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
The L{config} module contains the L{OWTConfig} class, which is passed to
the SISTRI API calls. It stores useful information such as your Web Services
account private key and certificate.
It is strongly suggested that you create a single L{OWTConfig} object in
your project and pass that to the various API calls, rather than create new
L{OWTConfig} objects haphazardly. This is merely a design suggestion,
treat it as such.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from storage import OWTStorage
from binding import OWTBinding


class OWTConfig(object):
    """
    Base configuration class that is used for the different SISTRI SOAP calls.
    These are generally passed to the OWT request classes as arguments.
    You may instantiate a L{OWTConfig} object with the minimal C{certificate},
    C{privatekey} and C{dbstring} arguments and set the instance variables
    documented below at a later time if you must.
    """

    def __init__(self, certificate, privatekey, dbstring, wsdl=None):
        """
        @type certificate: L{str}
        @param certificate: Certificate.
        @type privatekey: L{str}
        @param privatekey: Private Key for your Web Systems account.
            This is generally sended to you after registration.
        @type dbstring: L{str}
        @param dbstring: Database connection string.
        @type engine: L{Engine}
        @param engine: Engine connected to database.
        @type session: L{Session}
        @param session: The session object.
        @type storage: L{Storage}
        @param storage: The storage object.
        @type binding: L{Binding}
        @param binding: The binding object.
        @type wsdl: L{str}
        @keyword wsdl: In the event that you want to override the url to
            your WSDL, do so with this argument.
        """
        self.certificate = certificate
        """@ivar: Certificate."""
        self.privatekey = privatekey
        """@ivar: Private key."""
        if wsdl == None:
            self.wsdl = "https://sisssl.sistri.it/SIS/services/SIS?wsdl"
        else:
            self.wsdl = wsdl
        """@ivar: WSDL url string."""
        self.dbstring = dbstring
        """@ivar: Database connection string."""
        self.engine = create_engine(self.dbstring, echo=False)
        """@ivar: Engine connected to database."""
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        """@ivar: The session object."""
        self.storage = OWTStorage(self.engine)
        """@ivar: The storage object."""
        self.binding = OWTBinding(self.storage)
        """@ivar: The binding object."""
