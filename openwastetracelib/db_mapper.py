#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation,metadata_either version 3 of the License,metadata_or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not,metadata_see <http://www.gnu.org/licenses/>.

"""
The I{db mapper} module provides mapping for object and tables.
"""

from sqlalchemy.orm import mapper
from db_objects import *
from db_metadata import *

##########
#Cataloghi
##########

mapperDescrittoreCatalogo=mapper(DescrittoreCatalogo,metadata_descrittorecatalogo)
mapperStati_scheda_sistri=mapper(Stati_scheda_sistri,metadata_stati_scheda_sistri)
mapperStati_fisici_rifiuto=mapper(Stati_fisici_rifiuto,metadata_stati_fisici_rifiuto)
mapperForme_giuridiche=mapper(Forme_giuridiche,metadata_forme_giuridiche)
mapperTipi_reg_cronologico=mapper(Tipi_reg_cronologico,metadata_tipi_reg_cronologico)
mapperOperazioni_impianti=mapper(Operazioni_impianti,metadata_operazioni_impianti)
mapperCategorie_raee=mapper(Categorie_raee,metadata_categorie_raee)
mapperTipi_veicolo=mapper(Tipi_veicolo,metadata_tipi_veicolo)
mapperTipi_sede=mapper(Tipi_sede,metadata_tipi_sede)
mapperTipi_registrazioni_crono=mapper(Tipi_registrazioni_crono,metadata_tipi_registrazioni_crono)
mapperNumeri_onu=mapper(Numeri_onu,metadata_numeri_onu)
mapperLocalita_estere=mapper(Localita_estere,metadata_localita_estere)
mapperAssociazioni_categoria=mapper(Associazioni_categoria,metadata_associazioni_categoria)
mapperStati_registro_cronologico=mapper(Stati_registro_cronologico,metadata_stati_registro_cronologico)
mapperTipi_imballaggi=mapper(Tipi_imballaggi,metadata_tipi_imballaggi)
mapperSottocategorie_star=mapper(Sottocategorie_star,metadata_sottocategorie_star)
mapperTipi_documento=mapper(Tipi_documento,metadata_tipi_documento)
mapperClassi_adr=mapper(Classi_adr,metadata_classi_adr)
mapperRuoli_aziendali=mapper(Ruoli_aziendali,metadata_ruoli_aziendali)
mapperStati_utente_idm=mapper(Stati_utente_idm,metadata_stati_utente_idm)
mapperCamere_commercio=mapper(Camere_commercio,metadata_camere_commercio)
mapperTipi_esito_trasporto=mapper(Tipi_esito_trasporto,metadata_tipi_esito_trasporto)
mapperStati_veicolo=mapper(Stati_veicolo,metadata_stati_veicolo)
mapperCod_rec_1013=mapper(Cod_rec_1013,metadata_cod_rec_1013)
mapperStati_registrazioni_crono=mapper(Stati_registrazioni_crono,metadata_stati_registrazioni_crono)
mapperTipi_trasporto=mapper(Tipi_trasporto,metadata_tipi_trasporto)
mapperTipologie_raee=mapper(Tipologie_raee,metadata_tipologie_raee)
mapperCodici_cer_iii_livello=mapper(Codici_cer_iii_livello,metadata_codici_cer_iii_livello)
mapperTipi_stato_impresa=mapper(Tipi_stato_impresa,metadata_tipi_stato_impresa)
mapperCaratteristiche_pericolo=mapper(Caratteristiche_pericolo,metadata_caratteristiche_pericolo)
mapperSottotipi_veicolo=mapper(Sottotipi_veicolo,metadata_sottotipi_veicolo)

############
#Anagrafiche
############

mapperAzienda=mapper(Azienda,metadata_azienda,properties=dict(RelSedeLegale=relation(SedeLegale),RelSedi=relation(Sede)))
mapperSede=mapper(Sede,metadata_sede)
mapperSedeLegale=mapper(SedeLegale,metadata_sedelegale)
