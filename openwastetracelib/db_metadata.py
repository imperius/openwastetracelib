# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation,either version 3 of the License,or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not,see <http://www.gnu.org/licenses/>.

"""
The I{db metadata} module provides database initialization.
"""

from sqlalchemy import  *
from sqlalchemy.orm import *
import config

# TODO: echo =True e da elimnare in un ambiente di produzione
dbengine = create_engine(config.DB_STRING, echo=True)
meta = MetaData()
meta.bind = dbengine
Session = sessionmaker(bind=dbengine)
session = Session()

# INFO: sqlalchemy.exc.InvalidRequestError: VARCHAR requires a length when rendered on MySQL

# elencocataloghi
elencocataloghi=Table('elencocataloghi',meta,
                Column('ceid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('catalogo',String(255),nullable=False,index=True),
                Column('versione',Numeric,nullable=False),
                Column('descrizione',String(255),nullable=True),
                )

# stati_scheda_sistri
stati_scheda_sistri=Table('stati_scheda_sistri',meta,
                Column('sssid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_stato_scheda_sistri',String(255),nullable=False,index=True),
                Column('stato_scheda_sistri',String(255),nullable=False),
                )

# stati_fisici_rifiuto
stati_fisici_rifiuto=Table('stati_fisici_rifiuto',meta,
                Column('sfrid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_stato_fisico_rifiuto',String(255),nullable=False,index=True),
                Column('descr_stato_fisico_rifiuto',String(255),nullable=False),
                Column('codice_stato_fisico',String(255),nullable=False),
                )

# forme_giuridiche
forme_giuridiche=Table('forme_giuridiche',meta,
                Column('fgid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_forma_giuridica',String(255),nullable=False,index=True),
                Column('descrizione_forma_giuridica',String(255),nullable=False),
                )

# tipi_reg_cronologico
tipi_reg_cronologico=Table('tipi_reg_cronologico',meta,
                Column('trcid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_reg_cronologico',String(255),nullable=False,index=True),
                Column('descrizione_tipo_reg_crono',String(255),nullable=False),
                Column('macro_categoria',String(255),nullable=False),
                )

# operazioni_impianti
operazioni_impianti=Table('operazioni_impianti',meta,
                Column('oiid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_operazione_impianto',String(255),nullable=False,index=True),
                Column('id_tipo_operazione_impianto',String(255),nullable=False),
                Column('operazione_impianto',String(255),nullable=False),
                Column('ordinamento',Integer,nullable=False),
                )

# categorie_raee
categorie_raee=Table('categorie_raee',meta,
                Column('crid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_categoria_raee',String(255),nullable=False,index=True),
                Column('descrizione_categoria_raee',String(255),nullable=False),
                )

# tipi_veicolo
tipi_veicolo=Table('tipi_veicolo',meta,
                Column('tvid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_veicolo',String(255),nullable=False,index=True),
                Column('descrizione',String(255),nullable=False),
                Column('codice_tipo_veicolo',Integer,nullable=False),
                Column('flag_rimorchio',Integer,nullable=False),
                )

# tipi_sede
tipi_sede=Table('tipi_sede',meta,
                Column('tsid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_sede',String(255),nullable=False,index=True),
                Column('descrizione',String(255),nullable=False),
                )

# tipi_registrazioni_crono
tipi_registrazioni_crono=Table('tipi_registrazioni_crono',meta,
                Column('trcid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_registrazione_crono',String(255),nullable=False,index=True),
                Column('descr_tipo_reg_crono',String(255),nullable=False),
                )

# numeri_onu
numeri_onu=Table('numeri_onu',meta,
                Column('noid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_numero_onu',String(255),nullable=False,index=True),
                Column('descrizione_numero_onu',String(255),nullable=False),
                )

# localita_estere
localita_estere=Table('localita_estere',meta,
                Column('leid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_localita',Integer,nullable=False,index=True),
                Column('nazione',String(255),nullable=False),
                Column('sigla_nazione',String(255),nullable=False),
                )

# associazioni_categoria
associazioni_categoria=Table('associazioni_categoria',meta,
                Column('acid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_associazione_categoria',Integer,nullable=False,index=True),
                Column('ass_categoria_nome',String(255),nullable=False),
                Column('id_accordo',String(255),nullable=False),
                Column('sigla_provincia',String(255),nullable=False),
                Column('sigla_cciaa',String(255),nullable=False),
                )

# stati_registro_cronologico
stati_registro_cronologico=Table('stati_registro_cronologico',meta,
                Column('srcid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_stato_registro_cronologico',String(255),nullable=False,index=True),
                Column('descrizione_stato_reg_crono',String(255),nullable=False),
                )

# tipi_imballaggi
tipi_imballaggi=Table('tipi_imballaggi',meta,
                Column('tiid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_imballaggio',Integer,nullable=False,index=True),
                Column('tipo_imballaggio',String(255),nullable=False),
                Column('codice_imballaggio',String(255),nullable=False),
                )

# sottocategorie_star
sottocategorie_star=Table('sottocategorie_star',meta,
                Column('ssid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_sottocategoria_star',String(255),nullable=False,index=True),
                Column('id_categoria_star',String(255),nullable=False),
                Column('descrizione_sottocategoria',String(255),nullable=False),
                )

# tipi_documento
tipi_documento=Table('tipi_documento',meta,
                Column('ssid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_documento',String(255),nullable=False,index=True),
                Column('descrizione',String(255),nullable=False),
                )

# classi_adr
classi_adr=Table('classi_adr',meta,
                Column('caid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_classe_adr',String(255),nullable=False,index=True),
                Column('descrizione_classe_adr',String(255),nullable=False),
                )

# ruoli_aziendali
ruoli_aziendali=Table('ruoli_aziendali',meta,
                Column('raid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_ruolo_aziendale',String(255),nullable=False,index=True),
                Column('ruolo_aziendale',String(255),nullable=False),
                )

# stati_utente_idm
stati_utente_idm=Table('stati_utente_idm',meta,
                Column('suid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_stato_utente_idm',String(255),nullable=False,index=True),
                )

# camere_commercio
camere_commercio=Table('camere_commercio',meta,
                Column('ccid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_camera_commercio',Integer,nullable=False,index=True),
                Column('indirizzo',String(255),nullable=False,index=True),
                Column('numero_civico',String(255),nullable=False,index=True),
                Column('cap',String(255),nullable=False,index=True),
                Column('nome_persona_riferimento',String(255),nullable=False,index=True),
                Column('cognome_persona_riferimento',String(255),nullable=False,index=True),
                Column('email_persona_riferimento',String(255),nullable=False,index=True),
                Column('telefono_persona_riferimento',String(255),nullable=False,index=True),
                Column('sigla_cciaa',String(255),nullable=False,index=True),
                )

# tipi_esito_trasporto
tipi_esito_trasporto=Table('tipi_esito_trasporto',meta,
                Column('tetid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_esito_trasporto',String(255),nullable=False,index=True),
                Column('descr_esito_trasporto',String(255),nullable=False,index=True),
                )

# stati_veicolo
stati_veicolo=Table('stati_veicolo',meta,
                Column('svid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_stato_veicolo',String(255),nullable=False,index=True),
                Column('descrizione_stato_veicolo',String(255),nullable=False,index=True),
                )

# cod_rec_1013
cod_rec_1013=Table('cod_rec_1013',meta,
                Column('crid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_cod_rec_1013',String(255),nullable=False,index=True),
                Column('descrizione_cod_rec',String(255),nullable=False,index=True),
                )

# stati_registrazioni_crono
stati_registrazioni_crono=Table('stati_registrazioni_crono',meta,
                Column('srcid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_stato_registrazione_crono',String(255),nullable=False,index=True),
                Column('descrizione_stato_reg_crono',String(255),nullable=False,index=True),
                )

# tipi_trasporto
tipi_trasporto=Table('tipi_trasporto',meta,
                Column('ttid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_trasporto',Integer,nullable=False,index=True),
                Column('descrizione_tipo_trasporto',String(255),nullable=False,index=True),
                )

# tipologie_raee
tipologie_raee=Table('tipologie_raee',meta,
                Column('trid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipologia_raee',String(255),nullable=False,index=True),
                Column('descrizione_tipologia_raee',String(255),nullable=False,index=True),
                )

# codici_cer_iii_livello
codici_cer_iii_livello=Table('codici_cer_iii_livello',meta,
                Column('cclid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_codice_cer_iii_livello',String(255),nullable=False,index=True),
                Column('escrizione_iii_livello',String(255),nullable=False,index=True),
                Column('flag_pericoloso',Integer,nullable=False,index=True),
                Column('flag_attivo',Integer,nullable=False,index=True),
                )

# tipi_stato_impresa
tipi_stato_impresa=Table('tipi_stato_impresa',meta,
                Column('tsilid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_tipo_stato_impresa',String(255),nullable=False,index=True),
                )

# caratteristiche_pericolo
caratteristiche_pericolo=Table('caratteristiche_pericolo',meta,
                Column('cpid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_caratteristica_pericolo',String(255),nullable=False,index=True),
                Column('descr_car_pericolo',String(255),nullable=False,index=True),
                )

# sottotipi_veicolo
sottotipi_veicolo=Table('sottotipi_veicolo',meta,
                Column('svid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('id_sottotipo_veicolo',String(255),nullable=False,index=True),
                Column('descrizione',String(255),nullable=False,index=True),
                Column('codice_sottotipo_veicolo',Integer,nullable=False,index=True),
                )



#################################################
#   Anagrafiche                                                                                                #
#################################################

# Azienda
metadataAzienda=Table('azienda',meta,
                Column('Aid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('ragioneSociale',String(255),nullable=False,index=True),
                Column('cognome',String(255),nullable=True),
                Column('nome',String(255),nullable=True),
                Column('formaGiuridica',String(255),nullable=True),
                Column('formaGiuridicaDescr',String(255),nullable=True),
                Column('tipoStatoImpresa',String(255),nullable=True),
                Column('tipoStatoImpresaDescr',String(255),nullable=True),
                Column('codiceFiscale',String(25),nullable=False,index=True),
                Column('pIva',String(11),nullable=True,index=True),
                Column('numeroIscrizioneAlbo',String(255),nullable=True),
                Column('cciaaRea',String(255),nullable=True),
                Column('numeroIscrizioneRea',String(255),nullable=True),
                Column('codiceIstatAttPrincipale',String(255),nullable=True),
                Column('dataIscrizioneStar',DateTime,nullable=True),
                Column('codiceAtecoAttPrincipale',String(255),nullable=True),
                Column('descrizioneAttPrincipale',String(255),nullable=True),
                Column('versione',Integer,nullable=False),
                Column('idSIS',String(255),nullable=False),
                )

# SedeLegale
metadataSedeLegale=Table('SedeLegale',meta,
                Column('Slid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('tipoSede',String(255),nullable=False),
                Column('tipoSedeDescr',String(255),nullable=False),
                Column('nomeSede',String(255),nullable=False),
                Column('codiceIstatLocalita',String(255),nullable=False),
                Column('codiceCatastale',String(255),nullable=False),
                Column('nazione',String(255),nullable=False),
                Column('siglaNazione',String(255),nullable=False),
                Column('indirizzo',String(255),nullable=False),
                Column('nrCivico',String(255),nullable=False),
                Column('cap',String(255),nullable=False),
                Column('versione',Integer,nullable=False),
                Column('idSIS',String(255),nullable=False),
                ) #fixme: sottocategorie

# Sede
metadataSede=Table('Sede',meta,
                Column('Slid',Integer,nullable=False,primary_key=True,autoincrement=True),
                Column('tipoSede',String(255),nullable=False),
                Column('tipoSedeDescr',String(255),nullable=False),
                Column('nomeSede',String(255),nullable=False),
                Column('codiceIstatLocalita',String(255),nullable=False),
                Column('codiceCatastale',String(255),nullable=False),
                Column('nazione',String(255),nullable=False),
                Column('siglaNazione',String(255),nullable=False),
                Column('indirizzo',String(255),nullable=False),
                Column('nrCivico',String(255),nullable=True),
                Column('cap',String(255),nullable=True),
                Column('telefono',String(255),nullable=True),
                Column('fax',String(255),nullable=True),
                Column('numeroAddetti',Integer,nullable=True),
                Column('cameraCommercio',String(255),nullable=True),
                Column('cameraCommercioDescr',String(255),nullable=True),
                Column('associazioneCategoria',String(255),nullable=True),
                Column('associazioneCategoriaDescr',String(255),nullable=True),
                Column('codiceIstatAttPrincipale',String(255),nullable=True),
                Column('codiceAtecoAttPrincipale',String(255),nullable=True),
                Column('descrizioneAttPrincipale',String(255),nullable=True),
                Column('numeroIscrizioneRea',String(255),nullable=True),
                Column('numeroUla',Float,nullable=True),
                Column('latitudine',String,nullable=True),
                Column('longitudine',String,nullable=True),
                Column('versione',Integer,nullable=False),
                Column('idSIS',String(255),nullable=False),
                ) #fixme: sottocategorie


meta.create_all()
