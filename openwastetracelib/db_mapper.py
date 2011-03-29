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
The I{db mapper} module provides mapping for object and tables.
"""

from sqlalchemy.orm import mapper

from db_objects import *
from db_metadata import *

mapperElencoCataloghi=mapper(ElencoCataloghi, elencocataloghi)
mapperStati_scheda_sistri=mapper(Stati_scheda_sistri, stati_scheda_sistri)
mapperStati_fisici_rifiuto=mapper(Stati_fisici_rifiuto, stati_fisici_rifiuto)
mapperForme_giuridiche=mapper(Forme_giuridiche, forme_giuridiche)
mapperTipi_reg_cronologico=mapper(Tipi_reg_cronologico, tipi_reg_cronologico)
mapperOperazioni_impianti=mapper(Operazioni_impianti, operazioni_impianti)
mapperCategorie_raee=mapper(Categorie_raee, categorie_raee)
mapperTipi_veicolo=mapper(Tipi_veicolo, tipi_veicolo)
mapperTipi_sede=mapper(Tipi_sede, tipi_sede)
mapperTipi_registrazioni_crono=mapper(Tipi_registrazioni_crono, tipi_registrazioni_crono)
mapperNumeri_onu=mapper(Numeri_onu, numeri_onu)
mapperLocalita_estere=mapper(Localita_estere, localita_estere)
mapperAssociazioni_categoria=mapper(Associazioni_categoria, associazioni_categoria)
mapperStati_registro_cronologico=mapper(Stati_registro_cronologico, stati_registro_cronologico)
mapperTipi_imballaggi=mapper(Tipi_imballaggi, tipi_imballaggi)
mapperSottocategorie_star=mapper(Sottocategorie_star, sottocategorie_star)
mapperTipi_documento=mapper(Tipi_documento, tipi_documento)
mapperClassi_adr=mapper(Classi_adr, classi_adr)
mapperRuoli_aziendali=mapper(Ruoli_aziendali, ruoli_aziendali)
mapperStati_utente_idm=mapper(Stati_utente_idm, stati_utente_idm)
mapperCamere_commercio=mapper(Camere_commercio, camere_commercio)
mapperTipi_esito_trasporto=mapper(Tipi_esito_trasporto, tipi_esito_trasporto)
mapperStati_veicolo=mapper(Stati_veicolo, stati_veicolo)
mapperCod_rec_1013=mapper(Cod_rec_1013, cod_rec_1013)
mapperStati_registrazioni_crono=mapper(Stati_registrazioni_crono, stati_registrazioni_crono)
mapperTipi_trasporto=mapper(Tipi_trasporto, tipi_trasporto)
mapperTipologie_raee=mapper(Tipologie_raee, tipologie_raee)
mapperCodici_cer_iii_livello=mapper(Codici_cer_iii_livello, codici_cer_iii_livello)
mapperTipi_stato_impresa=mapper(Tipi_stato_impresa, tipi_stato_impresa)
mapperCaratteristiche_pericolo=mapper(Caratteristiche_pericolo, caratteristiche_pericolo)
mapperSottotipi_veicolo=mapper(Sottotipi_veicolo, sottotipi_veicolo)

#Anagrafiche
mapperAzienda=mapper(Azienda, metadataAzienda,
                     properties=dict(RelSedeLegale=relation(SedeLegale), RelSedi=relation(Sede) ),
                     )
mapperAziendaSedeLegale=mapper(SedeLegale, metadataSedeLegale )
mapperAziendaSede=mapper(Sede, metadataSede)