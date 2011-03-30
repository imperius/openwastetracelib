##!/usr/bin/env python
## -*- coding: utf-8 -*-

## OpenWasteTrace
## Copyright (C) 2011 Paolo Melchiorre
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

#"""
#The I{cataloghi} module provides connection to GetElencoCataloghi method.
#"""

#import __builtin__

#from xml.etree import cElementTree as ElementTree

#from https_cert import HttpAuthUsingCert
#from suds.client import Client

#from sqlalchemy import *
#from sqlalchemy.orm import sessionmaker, scoped_session

#import config
#import db_objects
#from db_objects import *
#import db_metadata
#from db_metadata import *
#from db_mapper import *
#import db_mapper
##import cataloghi
##from cataloghi import *

### TODO: echo =True e da elimnare in un ambiente di produzione
#dbengine = create_engine(config.DB_STRING, echo=False)
#meta = MetaData()
#meta.bind = dbengine
#Session = sessionmaker(bind=dbengine)
#session = Session()

## Connessione al Web services
#transport = HttpAuthUsingCert(config.CER_PATH, config.PEM_PATH)
#client = Client(config.WSDL_URL, transport=transport)

## Recupero dell'elenco cataloghi
#elencocataloghiresult = client.service.GetElencoCataloghi(config.USER_ID)

## ImportaElencoCataloghi
## ======================
## Importazione dell'elenco dei cataloghi.

## Ciclo su ogni DescrittoreCatalogo della lista
#for descrittorecatalogo in elencocataloghiresult:
## Recupero le variabili di ogni DescrittoreCatalogo
#    catalogo=descrittorecatalogo.catalogo.__repr__()
#    versione=int(descrittorecatalogo.versione)
#    descrizione=descrittorecatalogo.descrizione.__repr__()
## Memorizzazione dell'elenco cataloghi
#    nuovoDescrittoreCatalogo=DescrittoreCatalogo(catalogo,versione,descrizione)
#    session.add(nuovoDescrittoreCatalogo)
#session.commit()

## ImportaCataloghi
## ================
## Importazione dei valori dei cataloghi

## Ciclo su ogni DescrittoreCatalogo della lista
#for descrittorecatalogo in elencocataloghiresult:
## Recupero le variabili di ogni DescrittoreCatalogo
#    catalogonome=descrittorecatalogo.catalogo.__repr__()
## Recupero il nome della classe relaitva al DescrittoreCatalogo
#    catalogoclasse=catalogonome.capitalize()
## Metodi equivalenti per recuperare un oggetto avendo il suo nome come testo
## http://stackoverflow.com/questions/1650338
## http://docs.python.org/library/functions.html
##    classe=globals()[nomeclasse]
##    classe=getattr(globals()['cataloghi'],nomeclasse)
#    classe=getattr(db_objects,catalogoclasse)
## Recupero il catalogo in formato xml e lo mostro
#    catalogoxml = client.service.GetCatalogo(config.USER_ID,
#                                             catalogonome).encode("utf-8")
#    xmltree = ElementTree.XML(catalogoxml)
#    records=xmltree.find('records')
#    for record in records.findall('record'):
#        fields=record.findall('field')
#        emptyvariables=[u'' for i in range(len(fields))]
#        classenuova=classe(*emptyvariables)
#        for field in fields:
#            nome=field.findtext('nome').lower()
#            valore=field.findtext('valore')
##            tipo=getattr(__builtin__,field.findtext('tipo')[:3].lower())
#            tipo=field.findtext('tipo')[:3].lower()
#            if tipo=='int':
#                valore=int(valore)
##            classenuova.__setattr__(nome,tipo(valore))
#            classenuova.__setattr__(nome,valore)
#        session.add(classenuova)
#    session.commit()
