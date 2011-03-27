# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre
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
The I{wsdl cataloghi} module provides connection to GetElencoCataloghi method.
"""

import __builtin__

from xml.etree import cElementTree as ElementTree

from https_cert import HttpAuthUsingCert
from suds.client import Client

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session

import config
from db_objects import *
from db_metadata import *
from db_mapper import *


#import cataloghi
#from cataloghi import *

## TODO: echo =True e da elimnare in un ambiente di produzione
dbengine = create_engine(config.DB_STRING, echo=False)
meta = MetaData()
meta.bind = dbengine
Session = sessionmaker(bind=dbengine)
session = Session()

# Connessione al Web services
transport = HttpAuthUsingCert(config.CER_PATH, config.PEM_PATH)
client = Client(config.WSDL_URL, transport=transport)

# Recupero dell'elenco cataloghi
aziendaS = client.service.GetAzienda(config.USER_ID,"","00090710690")
a1=Azienda(ragioneSociale= aziendaS.ragioneSociale,








           )

