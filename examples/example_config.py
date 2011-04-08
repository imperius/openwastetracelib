"""
This file holds various configuration options used for all of the examples.
You will need to change the values below to match your test account.
"""
import os
import sys
from openwastetracelib.config import OWTConfig

# Change these values to match your account credentials.
#CONFIG_OBJ = OWTConfig(certificate = "/tmp/Certificate.cer",
#                       privatekey="/tmp/Private.pem",
#                       dbstring = "mysql+mysqldb://root:mysql@localhost/openwastetrace",
#                       wsdl="https://sisssl.sistri.it/SIS/services/SIS?wsdl")

CONFIG_OBJ = OWTConfig(certificate = "/home/paulox/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Certificato.cer",
                        privatekey = "/home/paulox/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Private.pem",
                        dbstring = "mysql+mysqldb://root:mysql@192.168.1.3:3306/openwastetrace?charset=utf8&use_unicode=0",
                        wsdl = "http://213.92.79.43:9090/intranet/pubblica/wsdl.xml")
from suds.client import Client
from openwastetracelib.https_cert import HttpAuthUsingCert
transport = HttpAuthUsingCert(CONFIG_OBJ.certificate,CONFIG_OBJ.privatekey)
client = Client(CONFIG_OBJ.wsdl, transport=transport)
from openwastetracelib import objects
from openwastetracelib import storage
from openwastetracelib.storage import OWTStorage
STORAGE_OBJ = OWTStorage()
from openwastetracelib import storage
from openwastetracelib import objects
