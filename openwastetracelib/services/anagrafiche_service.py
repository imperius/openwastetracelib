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
Cataloghi Service Module
========================
This package contains the cataloghi managment methods defined by Sistri.
For more details on each, refer to the respective class's documentation.
"""

import logging
from .. objects import Azienda,Forme_giuridiche,Tipi_stato_impresa
from .. objects import Sede
from .. base_service import OWTBaseService, OWTError

class OWTInvalidAzienda(OWTError):
    """
    Exception: Sent when a an error related invalid Azienda id.
    """
    pass

class GettingAziendaRequest(OWTBaseService):
    """
    This class allows you to get an Azienda object.
    By default, you can simply pass a identity string to the constructor.
    """
    def __init__(self,config_obj,*args,**kwargs):
        """
        Sends a get azienda request. The optional keyword args
        detailed on L{OWTBaseService} apply here as well.
        @type config_obj: L{OWTConfig}
        @param config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.codiceFiscaleAzienda = None
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingAziendaRequest,self).__init__(self._config_obj,
                                                    *args,**kwargs)

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
        # Fire off the query.
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    codiceFiscaleAzienda=self.codiceFiscaleAzienda)
        aziendaSistri=client.service.GetAzienda(**parm)
        try:
            formaGiuridica=Forme_giuridiche(
                id_tipo_forma_giuridica=\
                    aziendaSistri.formaGiuridica.idCatalogo.__repr__()
            )
            tipoStatoImpresa=Tipi_stato_impresa(
                id_tipo_stato_impresa=\
                    aziendaSistri.tipoStatoImpresa.idCatalogo.__repr__()
            )
            azienda=Azienda(
                ragioneSociale=\
                    aziendaSistri.ragioneSociale.__repr__(),
                cognome=\
                    aziendaSistri.cognome.__repr__(),
                nome=\
                    aziendaSistri.nome.__repr__(),
                codiceFiscale=\
                    aziendaSistri.codiceFiscale.__repr__(),
                pIva=\
                    aziendaSistri.pIva.__repr__(),
                numeroIscrizioneAlbo=\
                    aziendaSistri.numeroIscrizioneAlbo.__repr__(),
                cciaaRea=\
                    aziendaSistri.cciaaRea.__repr__(),
                numeroIscrizioneRea=\
                    aziendaSistri.numeroIscrizioneRea.__repr__(),
                codiceIstatAttPrincipale=\
                    aziendaSistri.codiceIstatAttPrincipale.__repr__(),
                dataIscrizioneStar=\
                    aziendaSistri.dataIscrizioneStar,
                codiceAtecoAttPrincipale=\
                    aziendaSistri.codiceAtecoAttPrincipale.__repr__(),
                descrizioneAttPrincipale=\
                    aziendaSistri.descrizioneAttPrincipale.__repr__(),
                versione=\
                    aziendaSistri.versione.long,
                idSIS=\
                    aziendaSistri.idSIS.__repr__(),
#                sedeLegale=\
#                    aziendaSistri.sedeLegale.idSIS.__repr__()
            )
            if session.query(Forme_giuridiche).filter(Forme_giuridiche.id_tipo_forma_giuridica==formaGiuridica.id_tipo_forma_giuridica).count()>0:
                formaGiuridica=session.query(Forme_giuridiche).filter(Forme_giuridiche.id_tipo_forma_giuridica==formaGiuridica.id_tipo_forma_giuridica).first()
            azienda.formaGiuridica=formaGiuridica
            if session.query(Tipi_stato_impresa).filter(Tipi_stato_impresa.id_tipo_stato_impresa==tipoStatoImpresa.id_tipo_stato_impresa).count()>0:
                tipoStatoImpresa=session.query(Tipi_stato_impresa).filter(Tipi_stato_impresa.id_tipo_stato_impresa==tipoStatoImpresa.id_tipo_stato_impresa).first()
            azienda.tipoStatoImpresa=tipoStatoImpresa
            session.merge(azienda)
            session.commit()
            response="Ok"
        except Exception,e:
            response=e
        return response

class GettingSedeRequest(OWTBaseService):
    """
    This class allows you to get an Sede object.
    By default, you can simply pass a identity string to the constructor.
    """
    def __init__(self,config_obj,*args,**kwargs):
        """
        Sends a get azienda request. The optional keyword args
        detailed on L{OWTBaseService} apply here as well.
        @type config_obj: L{OWTConfig}
        @param config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.idSIS = None
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingSedeRequest,self).__init__(self._config_obj,
                                                    *args,**kwargs)

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
        # Fire off the query.
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    idSIS=self.idSIS)
        sedeSistri=client.service.GetSede(**parm)
        try:
            sede=Sede(
                tipoSede=\
                    sedeSistri.tipoSede.idCatalogo.__repr__(),
                nomeSede=\
                    sedeSistri.nomeSede.__repr__(),
                codiceIstatLocalita=\
                    sedeSistri.codiceIstatLocalita.__repr__(),
                codiceCatastale=\
                    sedeSistri.codiceCatastale.__repr__(),
                nazione=\
                    sedeSistri.nazione.__repr__(),
                siglaNazione=\
                    sedeSistri.siglaNazione.__repr__(),
                indirizzo=\
                    sedeSistri.indirizzo.__repr__(),
                versione=\
                    sedeSistri.versione.long,
                idSIS=\
                    sedeSistri.idSIS.__repr__(),
            )
            session.merge(sede)
            session.commit()
            response="Ok"
        except Exception,e:
            response=e
        return response
