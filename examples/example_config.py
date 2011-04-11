"""
This file holds various configuration options used for all of the examples.
You will need to change the values below to match your test account.
"""

from openwastetracelib.config import OWTConfig

# Change these values to match your account credentials.
#CONFIG_OBJ = OWTConfig(certificate = "/tmp/Certificate.cer",
#                       privatekey="/tmp/Private.pem",
#                       dbstring = "sqlite:///:memory:",
#                       wsdl="https://sisssl.sistri.it/SIS/services/SIS?wsdl")

CONFIG_OBJ=OWTConfig(certificate = "/home/melpao/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Certificato.cer",
                      privatekey = "/home/melpao/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Private.pem",
                        dbstring = "mysql+mysqldb://root:mysql@192.168.1.7:3306/openwastetrace?charset=utf8&use_unicode=0",
                            wsdl = "http://213.92.79.43:9090/intranet/pubblica/wsdl.xml")

#from suds.client import Client
#from https_cert import HttpAuthUsingCert
#transport = HttpAuthUsingCert(CONFIG_OBJ.certificate,CONFIG_OBJ.privatekey)
#client = Client(CONFIG_OBJ.wsdl, transport=transport)
