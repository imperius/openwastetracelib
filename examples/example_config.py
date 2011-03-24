"""
This file holds various configuration options used for all of the examples.
You will need to change the values below to match your test account.
"""
import os
import sys
from openwastetracelib.config import OWTConfig

# Change these values to match your account credentials.
#CONFIG_OBJ =  OWTConfig(certificate="/tmp/Certificate.cer",
#                        privatekey="/tmp/Private.pem",
#                        wsdl="https://sisssl.sistri.it/SIS/services/SIS?wsdl")
CONFIG_OBJ =  OWTConfig(certificate="/home/melpao/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Certificato.cer",
                        privatekey="/home/melpao/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Private.pem",
                        wsdl="http://213.92.79.43:9090/intranet/pubblica/wsdl.xml")
