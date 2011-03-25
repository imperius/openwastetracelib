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
The I{test} module provides code for testing.
"""

#CER_PATH = "/home/melpao/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Certificato.cer"
#PEM_PATH = "/home/melpao/Dropbox/Madec/GestioneEcologia/Sistri/Interoperabilita/Certificati/Private.pem"
#WSDL_URL = "http://213.92.79.43:9090/intranet/pubblica/wsdl.xml"
#USER_ID = "gabriele.dangelo8571"
#DB_STRING = "mysql+mysqldb://root:mysql@192.168.1.6:3306/openwastetrace"

# Test connessione
# ================
# 
#from sqlalchemy import  *
#from sqlalchemy.orm import *
#import config
#dbengine = create_engine(config.DB_STRING("echo=True)

# Test inserimento oggetti
# ========================
#
#from db_mapper import *
## AssociazioniCategoria
#CataloghiElencoObject("AssociazioniCategoria",1,"Elenco di tutti gli oggetti di tipo AssociazioniCategoria")
## CamereCommercio
#CataloghiElencoObject("CamereCommercio",1,"Elenco di tutti gli oggetti di tipo CamereCommercio")
## CaratteristichePericolo
#CataloghiElencoObject("CaratteristichePericolo",1,"Elenco di tutti gli oggetti di tipo CaratteristichePericolo")
## CategorieRaee
#CataloghiElencoObject("CategorieRaee",1,"Elenco di tutti gli oggetti di tipo CategorieRaee")
## ClassiADR
#CataloghiElencoObject("ClassiADR",1,"Elenco di tutti gli oggetti di tipo ClassiADR")
## CodRec1013
#CataloghiElencoObject("CodRec1013",1,"Elenco di tutti gli oggetti di tipo CodRec1013")
## CodiciCerIIILievello
#CataloghiElencoObject("CodiciCerIIILievello",1,"Elenco di tutti gli oggetti di tipo CodiciCerIIILievello")
## FormeGiuridiche
#CataloghiElencoObject("FormeGiuridiche",1,"Elenco di tutti gli oggetti di tipo FormeGiuridiche")
## LocalitaEstere
#CataloghiElencoObject("LocalitaEstere",1,"Elenco di tutti gli oggetti di tipo LocalitaEstere")
## NumeriOnu
#CataloghiElencoObject("NumeriOnu",1,"Elenco di tutti gli oggetti di tipo NumeriOnu")
## OperazioniImpianti
#CataloghiElencoObject("OperazioniImpianti",1,"Elenco di tutti gli oggetti di tipo OperazioniImpianti")
## RuoliAziendali
#CataloghiElencoObject("RuoliAziendali",1,"Elenco di tutti gli oggetti di tipo RuoliAziendali")
## SottoCategorieStar
#CataloghiElencoObject("SottoCategorieStar",1,"Elenco di tutti gli oggetti di tipo SottoCategorieStar")
## StatiFisiciRifiuto
#CataloghiElencoObject("StatiFisiciRifiuto",1,"Elenco di tutti gli oggetti di tipo StatiFisiciRifiuto")
## StatiRegistrazioniCrono
#CataloghiElencoObject("StatiRegistrazioniCrono",1,"Elenco di tutti gli oggetti di tipo StatiRegistrazioniCrono")
## StatiSchedaSistri
#CataloghiElencoObject("StatiSchedaSistri",1,"Elenco di tutti gli oggetti di tipo StatiSchedaSistri")
## StatiVeicolo
#CataloghiElencoObject("StatiVeicolo",1,"Elenco di tutti gli oggetti di tipo StatiVeicolo")
## TipiImballaggi
#CataloghiElencoObject("TipiImballaggi",1,"Elenco di tutti gli oggetti di tipo TipiImballaggi")
## TipiRegCronologico
#CataloghiElencoObject("TipiRegCronologico",1,"Elenco di tutti gli oggetti di tipo TipiRegCronologico")
## TipiRegistrazioniCrono
#CataloghiElencoObject("TipiRegistrazioniCrono",1,"Elenco di tutti gli oggetti di tipo TipiRegistrazioniCrono")
## TipiSede
#CataloghiElencoObject("TipiSede",1,"Elenco di tutti gli oggetti di tipo TipiSede")
## TipiStatoImpresa
#CataloghiElencoObject("TipiStatoImpresa",1,"Elenco di tutti gli oggetti di tipo TipiStatoImpresa")
## TipiTrasporto
#CataloghiElencoObject("TipiTrasporto",1,"Elenco di tutti gli oggetti di tipo TipiTrasporto")
## TipiVeicoli
#CataloghiElencoObject("TipiVeicoli",1,"Elenco di tutti gli oggetti di tipo TipiVeicoli")
## TipoDocumento
#CataloghiElencoObject("TipoDocumento",1,"Elenco di tutti gli oggetti di tipo TipoDocumento")
## TipoEsitoTrasporto
#CataloghiElencoObject("TipoEsitoTrasporto",1,"Elenco di tutti gli oggetti di tipo TipoEsitoTrasporto")
## TipologieRaee
#CataloghiElencoObject("TipologieRaee",1,"Elenco di tutti gli oggetti di tipo TipologieRaee")



# ====
# TEST
# ====

#import __builtin__
#import cataloghi
#catalogoclasse="Stati_scheda_sistri"
#classe=getattr(cataloghi,catalogoclasse)
#i=0
#tipo=getattr(__builtin__,'String'[:3].lower())
#nome='ID_STATO_SCHEDA_SISTRI'.lower()
#valore='aaa'
#nome2='STATO_SCHEDA_SISTRI'.lower()
#valore2='bbb'
#tipo2=getattr(__builtin__,'String'[:3].lower())
#nomi=[]
#tipi=[]
#valori=[]
#args=[]
#nomi.append(nome)
#nomi.append(nome2)
#tipi.append(tipo)
#tipi.append(tipo2)
#valori.append(valore)
#valori.append(valore2)
#args.append("")
#args.append("")
#i=2
#classevuota=classe(*args)
#classevuota.__setattr__(nome.lower(),tipo(valore))

##variabile=getattr(classe,nome.lower())
##variabile=tipo(valore)
##variabile2=getattr(classe,nome2.lower())
##variabile2=tipo2(valore2)
##variabili=[]
##variabili.append(variabile)
##variabili.append(variabile2)


#classe(variabile=tipo(valore),variabile2=tipo2(valore2))
#classe(stato_scheda_sistri="433646hjkdfs",id_stato_scheda_sistri="xcbc54")



#c=classe('','')

#t=classe('a','b')
#session.add(t)
#session.commit()

# Test GetCataloghi
#descrittorecatalogo = elencocataloghi[0]
#nomeclasse=descrittorecatalogo.catalogo.__repr__().capitalize()
## Metodi equivalenti per recuperare un oggetto avendo il suo nome come testo
## classe=globals()[nomeclasse]
## classe=getattr(globals()['cataloghi'],nomeclasse)
#classe=getattr(cataloghi,nomeclasse)
#table = session.query(classe).first()
##table = session.query(Stati_scheda_sistri).first()
#Catalogo=descrittorecatalogo.catalogo.__repr__()

# Test XML
#    for node in ElementTree.XML(catalogou):
#        if node.tag == "records":
#            record=[]
#            for record in node.getchildren():
#                for field in record.getchildren():
#                    nome=field.findtext('nome')
#                    valore=field.findtext('valore')
#                    tipo=field.findtext('tipo')

#<?xml version="1.0" encoding="UTF-8"?>
#<catalogo>
#	<identificativo>STATI_SCHEDA_SISTRI</identificativo>
#	<versione>1</versione>
#	<descrizione>null</descrizione>
#	<records>
#		<record>
#			<field>
#				<nome>ID_STATO_SCHEDA_SISTRI</nome>
#				<valore>MD</valore>
#				<tipo>string</tipo>
#			</field>
#			<field>
#				<nome>STATO_SCHEDA_SISTRI</nome>
#				<valore>MODIFICATA</valore>
#				<tipo>string</tipo>
#			</field>
#		</record>
#	</records>
#</catalogo>
