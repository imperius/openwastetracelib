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
This package contains the cataloghi managment methods defined by Sistri.
For more details on each, refer to the respective class's documentation.
"""

from xml.etree import cElementTree as ElementTree
from .. import objects
from .. objects import Stati_scheda_sistri, Stati_fisici_rifiuto, \
    Forme_giuridiche, Tipi_reg_cronologico, Operazioni_impianti, \
    Categorie_raee, Tipi_veicolo, Tipi_sede, Tipi_registrazioni_crono, \
    Numeri_onu, Localita_estere, Associazioni_categoria, \
    Stati_registro_cronologico, Tipi_imballaggi, Sottocategorie_star, \
    Tipi_documento, Classi_adr, Ruoli_aziendali, Stati_utente_idm, \
    Camere_commercio, Tipi_esito_trasporto, Stati_veicolo, Cod_rec_1013, \
    Stati_registrazioni_crono, Tipi_trasporto, Tipologie_raee, \
    Codici_cer_iii_livello, Tipi_stato_impresa, Caratteristiche_pericolo, \
    Sottotipi_veicolo, DescrittoreCatalogo
from .. base_service import OWTBaseService, OWTError


class OWTInvalidCataloghi(OWTError):
    """
    Exception: Sent when a an error related cataloghi occurred.
    """
    pass


class UpdateCataloghiRequest(OWTBaseService):
    """
    This class allows you to updating all Cataloghi objects.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends an update cataloghi request. The optional keyword args
        detailed on L{OWTBaseService} apply here as well.
        @type config_obj: L{OWTConfig}
        @param config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        # Call the parent OWTBaseService class for basic setup work.
        super(UpdateCataloghiRequest, self).__init__(self._config_obj,
                                                        *args, **kwargs)

    def _check_response_for_request_errors(self):
        """
        Checks the response to see if there were any errors.
        """
#        if self.response.HighestSeverity == "ERROR":
#            for notification in self.response.Notifications:
#                if notification.Severity == "ERROR":
#                    if "Invalid tracking number" in notification.Message:
#                        raise FedexInvalidTrackingNumber(notification.Code,
#                                                         notification.Message)
#                    else:
#                        raise FedexError(notification.Code,
#                                         notification.Message)
        pass

    def _assemble_and_send_request(self):
        """
        Fires off the SISTRI request.
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        Importa Cataloghi
        =================
        1. Importazione dei valori dei cataloghi
        2. Ciclo su ogni DescrittoreCatalogo della lista
        3. Recupero le variabili di ogni DescrittoreCatalogo
        4. Recupero il nome della classe relaitva al DescrittoreCatalogo
        5. Metodi per recuperare un oggetto avendo il suo nome come testo
            http://stackoverflow.com/questions/1650338
            http://docs.python.org/library/functions.html
            classe=globals()[nomeclasse]
            classe=getattr(globals()['cataloghi'], nomeclasse)
        6. Recupero il catalogo in formato xml e lo mostro
        """
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity)
        elencocataloghi = None
        try:
            elencocataloghi = client.service.GetElencoCataloghi(**parm)
        except Exception, e:
            response = \
                e.fault.detail.GetElencoCataloghi_fault.errorMessage
        try:
            if elencocataloghi:
                for descrittorecatalogo in elencocataloghi:
                    catalogonome = descrittorecatalogo.catalogo.__repr__()
                    catalogoclasse = catalogonome.capitalize()
                    classe = getattr(objects, catalogoclasse)
                    catalogoxml = client.service.GetCatalogo(self.identity,
                        catalogonome).encode("utf-8")
                    xmltree = ElementTree.XML(catalogoxml)
                    records = xmltree.find('records')
                    for record in records.findall('record'):
                        fields = record.findall('field')
#                        emptyvariables = [u'' for i in range(len(fields))]
                        emptyvariables = [u'']
                        classenuova = classe(*emptyvariables)
                        for field in fields:
                            nome = field.findtext('nome').lower()
                            valore = field.findtext('valore')
                            tipo = field.findtext('tipo')[:3].lower()
                            if tipo == 'int':
                                valore = int(valore)
                            classenuova.__setattr__(nome, valore)
                        session.merge(classenuova)
            session.commit()
            response = "Ok"
        except Exception, e:
            response = e
        return response


class UpdateDescrittoriCataloghiRequest(OWTBaseService):
    """
    This class allows you to updating all DescrittoriCataloghi objects.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends an update cataloghi request. The optional keyword args
        detailed on L{OWTBaseService} apply here as well.
        @type config_obj: L{OWTConfig}
        @param config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        # Call the parent OWTBaseService class for basic setup work.
        super(UpdateDescrittoriCataloghiRequest, self).\
            __init__(self._config_obj, *args, **kwargs)

    def _check_response_for_request_errors(self):
        """
        Checks the response to see if there were any errors.
        """
#        if self.response.HighestSeverity == "ERROR":
#            for notification in self.response.Notifications:
#                if notification.Severity == "ERROR":
#                    if "Invalid tracking number" in notification.Message:
#                        raise FedexInvalidTrackingNumber(notification.Code,
#                                                         notification.Message)
#                    else:
#                        raise FedexError(notification.Code,
#                                         notification.Message)
        pass

    def _assemble_and_send_request(self):
        """
        Fires off the SISTRI request.
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity)
        elencocataloghi = None
        try:
            elencocataloghi = client.service.GetElencoCataloghi(**parm)
        except Exception, e:
            response = \
                e.fault.detail.GetElencoCataloghi_fault.errorMessage
        try:
            response = "Info:"
            if elencocataloghi:
                for descrittorecatalogo in elencocataloghi:
                    descrizione = None
                    if 'descrizione' in descrittorecatalogo:
                        descrizione = descrittorecatalogo.descrizione
                    if ('catalogo' and 'versione') in descrittorecatalogo:
                        catalogo = descrittorecatalogo.catalogo
                        versione = int(descrittorecatalogo.versione)
                        res = session.query(DescrittoreCatalogo).filter(
                            DescrittoreCatalogo.catalogo == catalogo)
                        if res.count() > 0:
                            vecchiaversione = res.first().versione
                            if versione != vecchiaversione:
                                response += " [" + catalogo + "] versione" + \
                                    " da " + str(vecchiaversione) + \
                                    " a " + str(versione)
                        nuovodescrittorecatalogo = DescrittoreCatalogo(
                            catalogo, versione, descrizione)
                        session.merge(nuovodescrittorecatalogo)
            response += " [OK]"
            session.commit()
        except Exception, e:
            response = e
        return response
