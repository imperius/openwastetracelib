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

from https_cert import HttpAuthUsingCert
from suds.client import Client
from db_mapper import *
import config
import cataloghi
from cataloghi import Stati_scheda_sistri

dbengine = create_engine(config.DB_STRING, echo=True)
meta=MetaData()
meta.bind = dbengine
Session = sessionmaker(bind=dbengine)
session=Session()

transport = HttpAuthUsingCert(config.CER_PATH, config.PEM_PATH)
client = Client(config.WSDL_URL, transport=transport)
elencocataloghi = client.service.GetElencoCataloghi(config.USER_ID)

descrittorecatalogo = elencocataloghi[0]
table = session.query(descrittorecatalogo.catalogo.__repr__().capitalize()).first()
table = session.query(Stati_scheda_sistri).first()

for descrittorecatalogo in elencocataloghi:
#    Catalogo=descrittorecatalogo.catalogo.__repr__()
#    Versione=int(descrittorecatalogo.versione)
#    Descrizione=descrittorecatalogo.descrizione.__repr__()
#    CataloghiElencoObject(Catalogo,Versione,Descrizione)
    print descrittorecatalogo
    table = session.query(StatiSchedaSistri).first()
    catalogo = client.service.GetCatalogo(config.USER_ID,descrittorecatalogo.catalogo)
    print catalogo.encode("utf-8")
