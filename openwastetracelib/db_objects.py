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
The I{db object} module provides objects initialization.
"""


from sqlalchemy import  *
from sqlalchemy.orm import *
import config

dbengine = create_engine(config.DB_STRING, echo=True)
# TODO: echo =True e da elimnare in un ambiente di produzione
meta=MetaData()
meta.bind = dbengine
# Collega la sessione
Session = sessionmaker(bind=dbengine)
session=Session()

# CATALOGHI_ELENCO
# CataloghiElenco
class CataloghiElencoObject(object):

    def __init__ (self, Catalogo, Versione, Descrizione):
        # CEID
        self.Catalogo = Catalogo
        self.Versione = Versione
        self.Descrizione = Descrizione
        session.add(self)
        session.commit()

# STATI_SCHEDA_SISTRI
# StatiSchedaSistri
class StatiSchedaSistriObject(object):

    def __init__ (self, ID_STATO_SCHEDA_SISTRI, STATO_SCHEDA_SISTRI):
        # SSSID
        self.ID_STATO_SCHEDA_SISTRI = ID_STATO_SCHEDA_SISTRI
        self.STATO_SCHEDA_SISTRI = STATO_SCHEDA_SISTRI
        session.add(self)
        session.commit()

# STATI_FISICI_RIFIUTO
# StatiFisiciRifiuto
class StatiFisiciRifiutoObject(object):

    def __init__ (self, ID_STATO_FISICO_RIFIUTO, DESCR_STATO_FISICO_RIFIUTO, CODICE_STATO_FISICO):
        # SFRID
        self.ID_STATO_FISICO_RIFIUTO = ID_STATO_FISICO_RIFIUTO
        self.DESCR_STATO_FISICO_RIFIUTO = DESCR_STATO_FISICO_RIFIUTO
        self.CODICE_STATO_FISICO = CODICE_STATO_FISICO
        session.add(self)
        session.commit()

# FORME_GIURIDICHE
# FormeGiuridiche
class FormeGiuridicheObject(object):

    def __init__ (self, ID_TIPO_FORMA_GIURIDICA, DESCRIZIONE_FORMA_GIURIDICA):
        # FGID
        self.ID_TIPO_FORMA_GIURIDICA = ID_TIPO_FORMA_GIURIDICA
        self.DESCRIZIONE_FORMA_GIURIDICA = DESCRIZIONE_FORMA_GIURIDICA
        session.add(self)
        session.commit()

# TIPI_REG_CRONOLOGICO
# TipiRegCronologico
class TipiRegCronologicoObject(object):

    def __init__ (self,ID_TIPO_REG_CRONOLOGICO,DESCRIZIONE_TIPO_REG_CRONO,MACRO_CATEGORIA):
        # TRCID
        self.ID_TIPO_REG_CRONOLOGICO = ID_TIPO_REG_CRONOLOGICO
        self.DESCRIZIONE_TIPO_REG_CRONO = DESCRIZIONE_TIPO_REG_CRONO
        self.MACRO_CATEGORIA = MACRO_CATEGORIA
        session.add(self)
        session.commit()

##OPERAZIONI_IMPIANTI
# OperazioniImpianti
class OperazioniImpiantiObject(object):

    def __init__ (self,ID_OPERAZIONE_IMPIANTO,ID_TIPO_OPERAZIONE_IMPIANTO,OPERAZIONE_IMPIANTO,ORDINAMENTO):
        # OIID
        self.ID_OPERAZIONE_IMPIANTO = ID_OPERAZIONE_IMPIANTO
        self.ID_TIPO_OPERAZIONE_IMPIANTO = ID_TIPO_OPERAZIONE_IMPIANTO
        self.OPERAZIONE_IMPIANTO = OPERAZIONE_IMPIANTO
        self.ORDINAMENTO = ORDINAMENTO
        session.add(self)
        session.commit()

##CATEGORIE_RAEE
# CategorieRaee
class CategorieRaeeObject(object):

    def __init__ (self,ID_CATEGORIA_RAEE,DESCRIZIONE_CATEGORIA_RAEE):
        # CRID
        self.ID_CATEGORIA_RAEE = ID_CATEGORIA_RAEE
        self.DESCRIZIONE_CATEGORIA_RAEE = DESCRIZIONE_CATEGORIA_RAEE
        session.add(self)
        session.commit()


## TIPI_VEICOLO
# TipiVeicoli
class TipiVeicoliObject(object):

    def __init__ (self,ID_TIPO_VEICOLO,CODICE_TIPO_VEICOLO,FLAG_RIMORCHIO):
        # TVID
        self.ID_TIPO_VEICOLO = ID_TIPO_VEICOLO
        self.DESCRIZIONE = DESCRIZIONE
        self.CODICE_TIPO_VEICOLO = CODICE_TIPO_VEICOLO
        self.FLAG_RIMORCHIO = FLAG_RIMORCHIO
        session.add(self)
        session.commit()

# TIPI_SEDE
# TipiSede
class TipiSedeObject(object):

    def __init__ (self,ID_TIPO_SEDE,DESCRIZIONE):
        # TSID
        self.ID_TIPO_SEDE = ID_TIPO_SEDE
        self.DESCRIZIONE = DESCRIZIONE
        session.add(self)
        session.commit()


## TIPI_REGISTRAZIONI_CRONO
# TipiRegistrazioniCrono
class TipiRegistrazioniCronoObject(object):

    def __init__ (self,ID_TIPO_REGISTRAZIONE_CRONO,DESCR_TIPO_REG_CRONO):
        # TRCID
        self.ID_TIPO_REGISTRAZIONE_CRONO = ID_TIPO_REGISTRAZIONE_CRONO
        self.DESCR_TIPO_REG_CRONO = DESCR_TIPO_REG_CRONO
        session.add(self)
        session.commit()


## NUMERI_ONU
# NumeriOnu
class NumeriOnuObject(object):

    def __init__ (self,ID_NUMERO_ONU,DESCRIZIONE_NUMERO_ONU):
        # NOID
        self.ID_NUMERO_ONU = ID_NUMERO_ONU
        self.DESCRIZIONE_NUMERO_ONU = DESCRIZIONE_NUMERO_ONU
        session.add(self)
        session.commit()

# LOCALITA_ESTERE
# LocalitaEstere
class LocalitaEstereObject(object):

    def __init__ (self,ID_LOCALITA,NAZIONE,SIGLA_NAZIONE):
        # LEID
        self.ID_LOCALITA = ID_LOCALITA
        self.NAZIONE = NAZIONE
        self.SIGLA_NAZIONE = SIGLA_NAZIONE
        session.add(self)
        session.commit()

# ASSOCIAZIONI_CATEGORIA
# AssociazioniCategoria
class AssociazioniCategoriaObject(object):

    def __init__ (self,ID_ASSOCIAZIONE_CATEGORIA,ASS_CATEGORIA_NOME,ID_ACCORDO,SIGLA_PROVINCIA,SIGLA_CCIAA):
        # ACID
        self.ID_ASSOCIAZIONE_CATEGORIA = ID_ASSOCIAZIONE_CATEGORIA
        self.ASS_CATEGORIA_NOME = ASS_CATEGORIA_NOME
        self.ID_ACCORDO = ID_ACCORDO
        self.SIGLA_PROVINCIA = SIGLA_PROVINCIA
        self.SIGLA_CCIAA = SIGLA_CCIAA
        session.add(self)
        session.commit()

# STATI_REGISTRO_CRONOLOGICO
# StatiRegistrioCronologico
class StatiRegistrioCronologicoObject(object):

    def __init__ (self,ID_STATO_REGISTRO_CRONOLOGICO,DESCRIZIONE_STATO_REG_CRONO):
        # SRCID
        self.ID_STATO_REGISTRO_CRONOLOGICO = ID_STATO_REGISTRO_CRONOLOGICO
        self.DESCRIZIONE_STATO_REG_CRONO = DESCRIZIONE_STATO_REG_CRONO
        session.add(self)
        session.commit()

# TIPI_IMBALLAGGI
# TipiImballaggi
class TipiImballaggiObject(object):

    def __init__ (self,ID_TIPO_IMBALLAGGIO,TIPO_IMBALLAGGIO,CODICE_IMBALLAGGIO):
        # TIID
        self.ID_TIPO_IMBALLAGGIO = ID_TIPO_IMBALLAGGIO
        self.TIPO_IMBALLAGGIO = TIPO_IMBALLAGGIO
        self.CODICE_IMBALLAGGIO = CODICE_IMBALLAGGIO
        session.add(self)
        session.commit()

# SOTTOCATEGORIE_STAR
# SottoCategorieStar
class SottoCategorieStarObject(object):

    def __init__ (self,ID_SOTTOCATEGORIA_STAR,ID_CATEGORIA_STAR,DESCRIZIONE_SOTTOCATEGORIA):
        # SSID
        self.ID_SOTTOCATEGORIA_STAR = ID_SOTTOCATEGORIA_STAR
        self.ID_CATEGORIA_STAR = ID_CATEGORIA_STAR
        self.DESCRIZIONE_SOTTOCATEGORIA = DESCRIZIONE_SOTTOCATEGORIA
        session.add(self)
        session.commit()

# TIPI_DOCUMENTO
# TipoDocumento
class TipoDocumentoObject(object):

    def __init__ (self,ID_TIPO_DOCUMENTO,DESCRIZIONE):
        # SSID
        self.ID_TIPO_DOCUMENTO = ID_TIPO_DOCUMENTO
        self.DESCRIZIONE = DESCRIZIONE
        session.add(self)
        session.commit()

# CLASSI_ADR
# ClassiADR
class ClassiADRObject(object):

    def __init__ (self,ID_CLASSE_ADR,DESCRIZIONE_CLASSE_ADR):
        # CAID
        self.ID_CLASSE_ADR = ID_CLASSE_ADR
        self.DESCRIZIONE_CLASSE_ADR = DESCRIZIONE_CLASSE_ADR
        session.add(self)
        session.commit()

# RUOLI_AZIENDALI
# RuoliAziendali
class RuoliAziendaliObject(object):

    def __init__ (self,ID_RUOLO_AZIENDALE,RUOLO_AZIENDALE):
        # RAID
        self.ID_RUOLO_AZIENDALE = ID_RUOLO_AZIENDALE
        self.RUOLO_AZIENDALE = RUOLO_AZIENDALE
        session.add(self)
        session.commit()

# STATI_UTENTE_IDM
# StatiUtente
class StatiUtenteObject(object):

    def __init__ (self,ID_STATO_UTENTE_IDM):
        # SUID
        self.ID_STATO_UTENTE_IDM = ID_STATO_UTENTE_IDM
        session.add(self)
        session.commit()

# CAMERE_COMMERCIO
# CamereCommercio
class CamereCommercioObject(object):

    def __init__ (self,ID_CAMERA_COMMERCIO,INDIRIZZO,NUMERO_CIVICO,CAP,NOME_PERSONA_RIFERIMENTO,COGNOME_PERSONA_RIFERIMENTO,EMAIL_PERSONA_RIFERIMENTO,TELEFONO_PERSONA_RIFERIMENTO,SIGLA_CCIAA):
        # CCID
        self.ID_CAMERA_COMMERCIO = ID_CAMERA_COMMERCIO
        self.INDIRIZZO = INDIRIZZO
        self.NUMERO_CIVICO = NUMERO_CIVICO
        self.CAP = CAP
        self.NOME_PERSONA_RIFERIMENTO = NOME_PERSONA_RIFERIMENTO
        self.COGNOME_PERSONA_RIFERIMENTO = COGNOME_PERSONA_RIFERIMENTO
        self.EMAIL_PERSONA_RIFERIMENTO = EMAIL_PERSONA_RIFERIMENTO
        self.TELEFONO_PERSONA_RIFERIMENTO = TELEFONO_PERSONA_RIFERIMENTO
        self.SIGLA_CCIAA = SIGLA_CCIAA
        session.add(self)
        session.commit()

# TIPI_ESITO_TRASPORTO
# TipoEsitoTrasporto
class TipoEsitoTrasportoObject(object):

    def __init__ (self,ID_ESITO_TRASPORTO,DESCR_ESITO_TRASPORTO):
        # TETID
        self.ID_ESITO_TRASPORTO = ID_ESITO_TRASPORTO
        self.DESCR_ESITO_TRASPORTO = DESCR_ESITO_TRASPORTO
        session.add(self)
        session.commit()

# STATI_VEICOLO
# StatiVeicolo
class StatiVeicoloObject(object):

    def __init__ (self,ID_STATO_VEICOLO,DESCRIZIONE_STATO_VEICOLO):
        # SVID
        self.ID_STATO_VEICOLO = ID_STATO_VEICOLO
        self.DESCRIZIONE_STATO_VEICOLO = DESCRIZIONE_STATO_VEICOLO
        session.add(self)
        session.commit()

# COD_REC_1013
# CodRec1013
class CodRec1013Object(object):

    def __init__ (self,ID_COD_REC_1013,DESCRIZIONE_COD_REC):
        # CRID
        self.ID_COD_REC_1013 = ID_COD_REC_1013
        self.DESCRIZIONE_COD_REC = DESCRIZIONE_COD_REC
        session.add(self)
        session.commit()

# STATI_REGISTRAZIONI_CRONO
# StatiRegistrazioniCrono
class StatiRegistrazioniCronoObject(object):

    def __init__ (self,ID_STATO_REGISTRAZIONE_CRONO,DESCRIZIONE_STATO_REG_CRONO):
        # SRCID
        self.ID_STATO_REGISTRAZIONE_CRONO = ID_STATO_REGISTRAZIONE_CRONO
        self.DESCRIZIONE_STATO_REG_CRONO = DESCRIZIONE_STATO_REG_CRONO
        session.add(self)
        session.commit()

# TIPI_TRASPORTO
# TipiTrasporto
class TipiTrasportoObject(object):

    def __init__ (self,ID_TIPO_TRASPORTO,DESCRIZIONE_TIPO_TRASPORTO):
        # TTID
        self.ID_TIPO_TRASPORTO = ID_TIPO_TRASPORTO
        self.DESCRIZIONE_TIPO_TRASPORTO = DESCRIZIONE_TIPO_TRASPORTO
        session.add(self)
        session.commit()


## TIPOLOGIE_RAEE
# TipologieRaee
class TipologieRaeeObject(object):

    def __init__ (self,ID_TIPOLOGIA_RAEE,DESCRIZIONE_TIPOLOGIA_RAEE):
        # TRID
        self.ID_TIPOLOGIA_RAEE = ID_TIPOLOGIA_RAEE
        self.DESCRIZIONE_TIPOLOGIA_RAEE = DESCRIZIONE_TIPOLOGIA_RAEE
        session.add(self)
        session.commit()

# CODICI_CER_III_LIVELLO
# CodiciCerIIILievello
class CodiciCerIIILievelloObject(object):

    def __init__ (self,ID_CODICE_CER_III_LIVELLO,ESCRIZIONE_III_LIVELLO,FLAG_PERICOLOSO,FLAG_ATTIVO):
        # CCLID
        self.ID_CODICE_CER_III_LIVELLO = ID_CODICE_CER_III_LIVELLO
        self.ESCRIZIONE_III_LIVELLO = ESCRIZIONE_III_LIVELLO
        self.FLAG_PERICOLOSO = FLAG_PERICOLOSO
        self.FLAG_ATTIVO = FLAG_ATTIVO
        session.add(self)
        session.commit()

# TIPI_STATO_IMPRESA
# TipiStatoImpresa
class TipiStatoImpresaObject(object):

    def __init__ (self,ID_TIPO_STATO_IMPRESA):
        # TSILID
        self.ID_TIPO_STATO_IMPRESA = ID_TIPO_STATO_IMPRESA
        session.add(self)
        session.commit()

# CARATTERISTICHE_PERICOLO
# CaratteristichePericolo
class CaratteristichePericoloObject(object):

    def __init__ (self,ID_CARATTERISTICA_PERICOLO,DESCR_CAR_PERICOLO):
        # CPID
        self.ID_CARATTERISTICA_PERICOLO = ID_CARATTERISTICA_PERICOLO
        self.DESCR_CAR_PERICOLO = DESCR_CAR_PERICOLO
        session.add(self)
        session.commit()

# SOTTOTIPI_VEICOLO
# SottotipiVeicolo
class SottotipiVeicoloObject(object):

    def __init__ (self,ID_SOTTOTIPO_VEICOLO,DESCRIZIONE,CODICE_SOTTOTIPO_VEICOLO):
        # SVID
        self.ID_SOTTOTIPO_VEICOLO = ID_SOTTOTIPO_VEICOLO
        self.DESCRIZIONE = DESCRIZIONE
        self.CODICE_SOTTOTIPO_VEICOLO = CODICE_SOTTOTIPO_VEICOLO
        session.add(self)
        session.commit()
