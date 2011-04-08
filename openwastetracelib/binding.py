#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpenWasteTrace
# Copyright (C) 2011 Paolo Melchiorre <paolo.melchiorre@madec.it>
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
The I{owt_binding} module provides mapping for objects and tables.
"""

from sqlalchemy.orm import mapper
from objects import *
from storage import *

class OWTBinding(object):
    """
    Base configuration class that is used for the binding.
    These are generally passed to the OWT request classes as arguments.
    """
    def __init__(self,storage):
        """
        @type storage: L{OWTStorage}
        @param storage: OWTStorage.
        """
        self.storage = storage
        """@ivar: OWTStorage."""
        self.mapperDescrittoreCatalogo=mapper(DescrittoreCatalogo,
                                        storage.metadata_descrittorecatalogo)
        self.mapperStati_scheda_sistri=mapper(Stati_scheda_sistri,
                                        storage.metadata_stati_scheda_sistri)
        self.mapperStati_fisici_rifiuto=mapper(Stati_fisici_rifiuto,
                                        storage.metadata_stati_fisici_rifiuto)
        self.mapperForme_giuridiche=mapper(Forme_giuridiche,
                                    storage.metadata_forme_giuridiche)
        self.mapperTipi_reg_cronologico=mapper(Tipi_reg_cronologico,
                                        storage.metadata_tipi_reg_cronologico)
        self.mapperOperazioni_impianti=mapper(Operazioni_impianti,
                                        storage.metadata_operazioni_impianti)
        self.mapperCategorie_raee=mapper(Categorie_raee,
                                    storage.metadata_categorie_raee)
        self.mapperTipi_veicolo=mapper(Tipi_veicolo,
                                storage.metadata_tipi_veicolo)
        self.mapperTipi_sede=mapper(Tipi_sede,
                            storage.metadata_tipi_sede)
        self.mapperTipi_registrazioni_crono=mapper(Tipi_registrazioni_crono,
                                    storage.metadata_tipi_registrazioni_crono)
        self.mapperNumeri_onu=mapper(Numeri_onu,
                                storage.metadata_numeri_onu)
        self.mapperLocalita_estere=mapper(Localita_estere,
                                    storage.metadata_localita_estere)
        self.mapperAssociazioni_categoria=mapper(Associazioni_categoria,
                            storage.metadata_associazioni_categoria)
        self.mapperStati_registro_cronologico=mapper(Stati_registro_cronologico,
                                storage.metadata_stati_registro_cronologico)
        self.mapperTipi_imballaggi=mapper(Tipi_imballaggi,
                                    storage.metadata_tipi_imballaggi)
        self.mapperSottocategorie_star=mapper(Sottocategorie_star,
                                        storage.metadata_sottocategorie_star)
        self.mapperTipi_documento=mapper(Tipi_documento,
                                    storage.metadata_tipi_documento)
        self.mapperClassi_adr=mapper(Classi_adr,
                                storage.metadata_classi_adr)
        self.mapperRuoli_aziendali=mapper(Ruoli_aziendali,
                                    storage.metadata_ruoli_aziendali)
        self.mapperStati_utente_idm=mapper(Stati_utente_idm,
                                    storage.metadata_stati_utente_idm)
        self.mapperCamere_commercio=mapper(Camere_commercio,
                                    storage.metadata_camere_commercio)
        self.mapperTipi_esito_trasporto=mapper(Tipi_esito_trasporto,
                                        storage.metadata_tipi_esito_trasporto)
        self.mapperStati_veicolo=mapper(Stati_veicolo,
                                storage.metadata_stati_veicolo)
        self.mapperCod_rec_1013=mapper(Cod_rec_1013,
                                storage.metadata_cod_rec_1013)
        self.mapperStati_registrazioni_crono=mapper(Stati_registrazioni_crono,
                                    storage.metadata_stati_registrazioni_crono)
        self.mapperTipi_trasporto=mapper(Tipi_trasporto,
                                    storage.metadata_tipi_trasporto)
        self.mapperTipologie_raee=mapper(Tipologie_raee,
                                    storage.metadata_tipologie_raee)
        self.mapperCodici_cer_iii_livello=mapper(Codici_cer_iii_livello,
                                    storage.metadata_codici_cer_iii_livello)
        self.mapperTipi_stato_impresa=mapper(Tipi_stato_impresa,
                                        storage.metadata_tipi_stato_impresa)
        self.mapperCaratteristiche_pericolo=mapper(Caratteristiche_pericolo,
                                    storage.metadata_caratteristiche_pericolo)
        self.mapperSottotipi_veicolo=mapper(Sottotipi_veicolo,
                                    storage.metadata_sottotipi_veicolo)
        self.mapperAzienda=mapper(Azienda,
                            storage.metadata_azienda)