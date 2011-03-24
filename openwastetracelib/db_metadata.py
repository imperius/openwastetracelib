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
The I{db metadata} module provides database initialization.
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

# INFO: sqlalchemy.exc.InvalidRequestError: VARCHAR requires a length when rendered on MySQL

# CATALOGHI_ELENCO
CataloghiElenco= Table('CataloghiElenco',meta,
                Column ('CEID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('Catalogo', String(255), nullable=False, index=True),
                Column ('Versione', Numeric, nullable=False),
                Column ('Descrizione', String(255), nullable=True),
                )

# STATI_SCHEDA_SISTRI
StatiSchedaSistri= Table('StatiSchedaSistri',meta,
                Column ('SSSID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_STATO_SCHEDA_SISTRI', String(255), nullable=False, index=True ),
                Column ('STATO_SCHEDA_SISTRI', String(255), nullable=False, ),
                )

# STATI_FISICI_RIFIUTO
StatiFisiciRifiuto= Table('StatiFisiciRifiuto',meta,
                Column ('SFRID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_STATO_FISICO_RIFIUTO', String(255), nullable=False, index=True ),
                Column ('DESCR_STATO_FISICO_RIFIUTO', String(255), nullable=False, ),
                Column ('CODICE_STATO_FISICO', String(255), nullable=False, ),
                )

# FORME_GIURIDICHE
FormeGiuridiche= Table('FormeGiuridiche',meta,
                Column ('FGID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_FORMA_GIURIDICA', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_FORMA_GIURIDICA', String(255), nullable=False, ),
                )

# TIPI_REG_CRONOLOGICO
TipiRegCronologico= Table('TipiRegCronologico',meta,
                Column ('TRCID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_REG_CRONOLOGICO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_TIPO_REG_CRONO', String(255), nullable=False, ),
                Column ('MACRO_CATEGORIA', String(255), nullable=False, ),
                )

# OPERAZIONI_IMPIANTI
OperazioniImpianti= Table('OperazioniImpianti',meta,
                Column ('OIID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_OPERAZIONE_IMPIANTO', String(255), nullable=False, index=True ),
                Column ('ID_TIPO_OPERAZIONE_IMPIANTO', String(255), nullable=False, ),
                Column ('OPERAZIONE_IMPIANTO', String(255), nullable=False, ),
                Column ('ORDINAMENTO', Integer, nullable=False, ),
                )

# CATEGORIE_RAEE
CategorieRaee= Table('CategorieRaee',meta,
                Column ('CRID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_CATEGORIA_RAEE', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_CATEGORIA_RAEE', String(255), nullable=False, ),
                )

# TIPI_VEICOLO
TipiVeicoli= Table('TipiVeicoli',meta,
                Column ('TVID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_VEICOLO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE', String(255), nullable=False, ),
                Column ('CODICE_TIPO_VEICOLO', Integer, nullable=False, ),
                Column ('FLAG_RIMORCHIO', Integer, nullable=False, ),
                )

# TIPI_SEDE
TipiSede= Table('TipiSede',meta,
                Column ('TSID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_SEDE', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE', String(255), nullable=False, ),
                )

# TIPI_REGISTRAZIONI_CRONO
TipiRegistrazioniCrono= Table('TipiRegistrazioniCrono',meta,
                Column ('TRCID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_REGISTRAZIONE_CRONO', String(255), nullable=False, index=True ),
                Column ('DESCR_TIPO_REG_CRONO', String(255), nullable=False, ),
                )

# NUMERI_ONU
NumeriOnu= Table('NumeriOnu',meta,
                Column ('NOID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_NUMERO_ONU', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_NUMERO_ONU', String(255), nullable=False, ),
                )

# LOCALITA_ESTERE
LocalitaEstere= Table('LocalitaEstere',meta,
                Column ('LEID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_LOCALITA', Integer, nullable=False, index=True ),
                Column ('NAZIONE', String(255), nullable=False, ),
                Column ('SIGLA_NAZIONE', String(255), nullable=False, ),
                )

# ASSOCIAZIONI_CATEGORIA
AssociazioniCategoria= Table('AssociazioniCategoria',meta,
                Column ('ACID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_ASSOCIAZIONE_CATEGORIA', Integer, nullable=False, index=True ),
                Column ('ASS_CATEGORIA_NOME', String(255), nullable=False, ),
                Column ('ID_ACCORDO', String(255), nullable=False, ),
                Column ('SIGLA_PROVINCIA', String(255), nullable=False, ),
                Column ('SIGLA_CCIAA', String(255), nullable=False, ),
                )

# STATI_REGISTRO_CRONOLOGICO
StatiRegistrioCronologico= Table('StatiRegistrioCronologico',meta,
                Column ('SRCID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_STATO_REGISTRO_CRONOLOGICO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_STATO_REG_CRONO', String(255), nullable=False, ),
                )

# TIPI_IMBALLAGGI
TipiImballaggi= Table('TipiImballaggi',meta,
                Column ('TIID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_IMBALLAGGIO', Integer, nullable=False, index=True ),
                Column ('TIPO_IMBALLAGGIO', String(255), nullable=False, ),
                Column ('CODICE_IMBALLAGGIO', String(255), nullable=False, ),
                )

# SOTTOCATEGORIE_STAR
SottoCategorieStar= Table('SottoCategorieStar',meta,
                Column ('SSID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_SOTTOCATEGORIA_STAR', String(255), nullable=False, index=True ),
                Column ('ID_CATEGORIA_STAR', String(255), nullable=False, ),
                Column ('DESCRIZIONE_SOTTOCATEGORIA', String(255), nullable=False, ),
                )

# TIPI_DOCUMENTO
TipoDocumento= Table('TipoDocumento',meta,
                Column ('SSID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_DOCUMENTO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE', String(255), nullable=False, ),
                )

# CLASSI_ADR
ClassiADR= Table('ClassiADR',meta,
                Column ('CAID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_CLASSE_ADR', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_CLASSE_ADR', String(255), nullable=False, ),
                )

# RUOLI_AZIENDALI
RuoliAziendali= Table('RuoliAziendali',meta,
                Column ('RAID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_RUOLO_AZIENDALE', String(255), nullable=False, index=True ),
                Column ('RUOLO_AZIENDALE', String(255), nullable=False, ),
                )

# STATI_UTENTE_IDM
StatiUtente= Table('StatiUtente',meta,
                Column ('SUID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_STATO_UTENTE_IDM', String(255), nullable=False, index=True ),
                )

# CAMERE_COMMERCIO
CamereCommercio= Table('CamereCommercio',meta,
                Column ('CCID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_CAMERA_COMMERCIO', Integer, nullable=False, index=True ),
                Column ('INDIRIZZO', String(255), nullable=False, index=True ),
                Column ('NUMERO_CIVICO', String(255), nullable=False, index=True ),
                Column ('CAP', String(255), nullable=False, index=True ),
                Column ('NOME_PERSONA_RIFERIMENTO', String(255), nullable=False, index=True ),
                Column ('COGNOME_PERSONA_RIFERIMENTO', String(255), nullable=False, index=True ),
                Column ('EMAIL_PERSONA_RIFERIMENTO', String(255), nullable=False, index=True ),
                Column ('TELEFONO_PERSONA_RIFERIMENTO', String(255), nullable=False, index=True ),
                Column ('SIGLA_CCIAA', String(255), nullable=False, index=True ),
                )

# TIPI_ESITO_TRASPORTO
TipoEsitoTrasporto= Table('TipoEsitoTrasporto',meta,
                Column ('TETID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_ESITO_TRASPORTO', String(255), nullable=False, index=True ),
                Column ('DESCR_ESITO_TRASPORTO', String(255), nullable=False, index=True ),
                )

# STATI_VEICOLO
StatiVeicolo= Table('StatiVeicolo',meta,
                Column ('SVID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_STATO_VEICOLO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_STATO_VEICOLO', String(255), nullable=False, index=True ),
                )

# COD_REC_1013
CodRec1013= Table('CodRec1013',meta,
                Column ('CRID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_COD_REC_1013', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_COD_REC', String(255), nullable=False, index=True ),
                )

# STATI_REGISTRAZIONI_CRONO
StatiRegistrazioniCrono= Table('StatiRegistrazioniCrono',meta,
                Column ('SRCID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_STATO_REGISTRAZIONE_CRONO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_STATO_REG_CRONO', String(255), nullable=False, index=True ),
                )

# TIPI_TRASPORTO
TipiTrasporto= Table('TipiTrasporto',meta,
                Column ('TTID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_TRASPORTO', Integer, nullable=False, index=True ),
                Column ('DESCRIZIONE_TIPO_TRASPORTO', String(255), nullable=False, index=True ),
                )

# TIPOLOGIE_RAEE
TipologieRaee= Table('TipologieRaee',meta,
                Column ('TRID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPOLOGIA_RAEE', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE_TIPOLOGIA_RAEE', String(255), nullable=False, index=True ),
                )

# CODICI_CER_III_LIVELLO
CodiciCerIIILievello= Table('CodiciCerIIILievello',meta,
                Column ('CCLID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_CODICE_CER_III_LIVELLO', String(255), nullable=False, index=True ),
                Column ('ESCRIZIONE_III_LIVELLO', String(255), nullable=False, index=True ),
                Column ('FLAG_PERICOLOSO', Integer, nullable=False, index=True ),
                Column ('FLAG_ATTIVO', Integer, nullable=False, index=True ),
                )

# TIPI_STATO_IMPRESA
TipiStatoImpresa= Table('TipiStatoImpresa',meta,
                Column ('TSILID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_TIPO_STATO_IMPRESA', String(255), nullable=False, index=True ),
                )

# CARATTERISTICHE_PERICOLO
CaratteristichePericolo= Table('CaratteristichePericolo',meta,
                Column ('CPID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_CARATTERISTICA_PERICOLO', String(255), nullable=False, index=True ),
                Column ('DESCR_CAR_PERICOLO', String(255), nullable=False, index=True ),
                )

# SOTTOTIPI_VEICOLO
SottotipiVeicolo= Table('SottotipiVeicolo',meta,
                Column ('SVID', Integer, nullable=False, primary_key=True, autoincrement=True ),
                Column ('ID_SOTTOTIPO_VEICOLO', String(255), nullable=False, index=True ),
                Column ('DESCRIZIONE', String(255), nullable=False, index=True ),
                Column ('CODICE_SOTTOTIPO_VEICOLO', Integer, nullable=False, index=True ),
                )

meta.create_all()
