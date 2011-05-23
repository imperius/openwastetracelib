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
The I{objects} module provides objects definition.
"""


#XXX: Cataloghi (ordine alafabetico)
class Associazioni_categoria(object):
    """ """
    def __init__(self, id_associazione_categoria, **kwargs):
        self.id_associazione_categoria = id_associazione_categoria
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Camere_commercio(object):
    """ """
    def __init__(self, id_camera_commercio, **kwargs):
        self.id_camera_commercio = id_camera_commercio
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Caratteristiche_pericolo(object):
    """ """
    def __init__(self, id_caratteristica_pericolo, **kwargs):
        self.id_caratteristica_pericolo = id_caratteristica_pericolo
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Categorie_raee(object):
    """ """
    def __init__(self, id_categoria_raee, **kwargs):
        self.id_categoria_raee = id_categoria_raee
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Causali_mov(object):
    """ """
    def __init__(self, id_causale_mov, **kwargs):
        self.id_causale_mov = id_causale_mov
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Causali_reg(object):
    """ """
    def __init__(self, id_causale_reg, **kwargs):
        self.id_causale_reg = id_causale_reg
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Causali_scheda(object):
    """ """
    def __init__(self, id_causale_sch, **kwargs):
        self.id_causale_sch = id_causale_sch
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Classi_adr(object):
    """ """
    def __init__(self, id_classe_adr, **kwargs):
        self.id_classe_adr = id_classe_adr
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Codici_cer_iii_livello(object):
    """ """
    def __init__(self, id_codice_cer_iii_livello, **kwargs):
        self.id_codice_cer_iii_livello = id_codice_cer_iii_livello
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Cod_rec_1013(object):
    """ """
    def __init__(self, id_cod_rec_1013, **kwargs):
        self.id_cod_rec_1013 = id_cod_rec_1013
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Forme_giuridiche(object):
    """ """
    def __init__(self, id_tipo_forma_giuridica, **kwargs):
        self.id_tipo_forma_giuridica = id_tipo_forma_giuridica
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Localita_estere(object):
    """ """
    def __init__(self, id_localita, **kwargs):
        self.id_localita = id_localita
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Numeri_onu(object):
    """ """
    def __init__(self, id_numero_onu, **kwargs):
        self.id_numero_onu = id_numero_onu
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Operazioni_impianti(object):
    """ """
    def __init__(self, id_operazione_impianto, **kwargs):
        self.id_operazione_impianto = id_operazione_impianto
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Ruoli_aziendali(object):
    """ """
    def __init__(self, id_ruolo_aziendale, **kwargs):
        self.id_ruolo_aziendale = id_ruolo_aziendale
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Sottocategorie_star(object):
    """ """
    def __init__(self, id_sottocategoria_star, **kwargs):
        self.id_sottocategoria_star = id_sottocategoria_star
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Sottotipi_veicolo(object):
    """ """
    def __init__(self, id_sottotipo_veicolo, **kwargs):
        self.id_sottotipo_veicolo = id_sottotipo_veicolo
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Stati_fisici_rifiuto(object):
    """ """
    def __init__(self, id_stato_fisico_rifiuto, **kwargs):
        self.id_stato_fisico_rifiuto = id_stato_fisico_rifiuto
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Stati_registrazioni_crono(object):
    """ """
    def __init__(self, id_stato_registrazione_crono, **kwargs):
        self.id_stato_registrazione_crono = id_stato_registrazione_crono
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Stati_registro_cronologico(object):
    """ """
    def __init__(self, id_stato_registro_cronologico, **kwargs):
        self.id_stato_registro_cronologico = id_stato_registro_cronologico
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Stati_scheda_sistri(object):
    """ """
    def __init__(self, id_stato_scheda_sistri, **kwargs):
        self.id_stato_scheda_sistri = id_stato_scheda_sistri
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Stati_utente_idm(object):
    """ """
    def __init__(self, id_stato_utente_idm, **kwargs):
        self.id_stato_utente_idm = id_stato_utente_idm
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Stati_veicolo(object):
    """ """
    def __init__(self, id_stato_veicolo, **kwargs):
        self.id_stato_veicolo = id_stato_veicolo
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_documento(object):
    """ """
    def __init__(self, id_tipo_documento, **kwargs):
        self.id_tipo_documento = id_tipo_documento
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_esito_trasporto(object):
    """ """
    def __init__(self, id_esito_trasporto, **kwargs):
        self.id_esito_trasporto = id_esito_trasporto
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_imballaggi(object):
    """ """
    def __init__(self, id_tipo_imballaggio, **kwargs):
        self.id_tipo_imballaggio = id_tipo_imballaggio
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_registrazioni_crono(object):
    """ """
    def __init__(self, id_tipo_registrazione_crono, **kwargs):
        self.id_tipo_registrazione_crono = id_tipo_registrazione_crono
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_reg_cronologico(object):
    """ """
    def __init__(self, id_tipo_reg_cronologico, **kwargs):
        self.id_tipo_reg_cronologico = id_tipo_reg_cronologico
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_sede(object):
    """ """
    def __init__(self, id_tipo_sede, **kwargs):
        self.id_tipo_sede = id_tipo_sede
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_stato_impresa(object):
    """ """
    def __init__(self, id_tipo_stato_impresa, **kwargs):
        self.id_tipo_stato_impresa = id_tipo_stato_impresa
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_trasporto(object):
    """ """
    def __init__(self, id_tipo_trasporto, **kwargs):
        self.id_tipo_trasporto = id_tipo_trasporto
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipi_veicolo(object):
    """ """
    def __init__(self, id_tipo_veicolo, **kwargs):
        self.id_tipo_veicolo = id_tipo_veicolo
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tipologie_raee(object):
    """ """
    def __init__(self, id_tipologia_raee, **kwargs):
        self.id_tipologia_raee = id_tipologia_raee
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


#XXX: Oggetti (ordine alafabetico)
class Azienda(object):
    """ Azienda object with idSIS."""
    def __init__(self, ragioneSociale, codiceFiscale, versione, idSIS,
                    **kwargs):
        self.ragioneSociale = ragioneSociale
        self.codiceFiscale = codiceFiscale
        self.versione = versione
        self.idSIS = idSIS
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class DescrittoreCatalogo(object):
    """ """
    def __init__(self, catalogo, versione, descrizione):
        self.catalogo = catalogo
        self.versione = versione
        self.descrizione = descrizione


class Movimentazione(object):
    """ Movimentazione object with idSIS."""
    def __init__(self, idSIS, idSISTRI, versione, movimentazioneNumeroSerie,
                    dataMovimentazione, **kwargs):
        self.idSIS = idSIS
        self.idSISTRI = idSISTRI
        self.versione = versione
        self.movimentazioneNumeroSerie = movimentazioneNumeroSerie
        self.dataMovimentazione = dataMovimentazione
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class RegistroCronologico(object):
    """ RegistroCronologico object with idSIS. """
    def __init__(self, idSIS, codiceRegistroCronologico, versione,
                    ultimoNumero, dataUltimoNumero, sottocategoria=None,
                    statoRegistroCronologico=None, tipoRegCronologico=None,
                    **kwargs):
        self.idSIS = idSIS
        self.codiceRegistroCronologico = codiceRegistroCronologico
        self.versione = versione
        self.ultimoNumero = ultimoNumero
        self.dataUltimoNumero = dataUltimoNumero
        self.statoRegistroCronologico = statoRegistroCronologico
        self.tipoRegCronologico = tipoRegCronologico
        self.sottocategoria = sottocategoria
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Sede(object):
    """ Sede object with idSIS. """
    def __init__(self, nomeSede, codiceIstatLocalita, codiceCatastale, nazione,
                    siglaNazione, indirizzo, versione, idSIS, tipoSede=None,
                    **kwargs):
        self.nomeSede = nomeSede
        self.codiceIstatLocalita = codiceIstatLocalita
        self.codiceCatastale = codiceCatastale
        self.nazione = nazione
        self.siglaNazione = siglaNazione
        self.indirizzo = indirizzo
        self.versione = versione
        self.tipoSede = tipoSede
        self.idSIS = idSIS
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Tratta_base(object):
    """ Tratta_base object with idSIS."""
    def __init__(self, idTratta, progressivo,
            idSISSede_trasportatore, flagOperatoreLogistico, **kwargs):
        self.idTratta = idTratta
        self.progressivo = progressivo
        self.idSISSede_trasportatore = idSISSede_trasportatore
        self.flagOperatoreLogistico = flagOperatoreLogistico
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


class Veicolo(object):
    """ Veicolo object with idSIS. """
    def __init__(self, targa, **kwargs):
        self.targa = targa
        for key in kwargs:
            self.__setattr__(key, kwargs[key])
