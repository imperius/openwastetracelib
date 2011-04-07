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
CONFIG_OBJ = OWTConfig(certificate = "~/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Certificato.cer",
                        privatekey = "~/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Private.pem",
                        dbstring = "mysql+mysqldb://root:mysql@192.168.1.2:3306/openwastetrace?charset=utf8&use_unicode=0",
                        wsdl = "http://213.92.79.43:9090/intranet/pubblica/wsdl.xml")
