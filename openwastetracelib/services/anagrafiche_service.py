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
from .. objects import Azienda
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
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(), WHICH RESIDES
            ON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        # Fire off the query.
        import pdb; pdb.set_trace()
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    codiceFiscaleAzienda=self.codiceFiscaleAzienda)
        aziendaS=client.service.GetAzienda(**parm)
        try:
            az=Azienda(ragioneSociale= aziendaS.ragioneSociale.__repr__(),
                       cognome=aziendaS.cognome.__repr__(),
                       nome=aziendaS.nome.__repr__(),
                       formaGiuridica=aziendaS.formaGiuridica.idCatalogo.__repr__(),
                       formaGiuridicaDescr=aziendaS.formaGiuridica.description.__repr__(),
                       tipoStatoImpresa=aziendaS.tipoStatoImpresa.idCatalogo.__repr__(),
                       tipoStatoImpresaDescr=aziendaS.tipoStatoImpresa.description.__repr__(),
                       codiceFiscale=aziendaS.codiceFiscale.__repr__(),
                       pIva=aziendaS.pIva.__repr__(),
                       numeroIscrizioneAlbo=aziendaS.numeroIscrizioneAlbo.__repr__(),
                       cciaaRea=aziendaS.cciaaRea.__repr__(),
                       numeroIscrizioneRea=aziendaS.numeroIscrizioneRea.__repr__(),
                       codiceIstatAttPrincipale=aziendaS.codiceIstatAttPrincipale.__repr__(),
                       dataIscrizioneStar=aziendaS.dataIscrizioneStar,   # nei campi datetime se c'e' la stringa none si incazza allora non faccio il repr
                       codiceAtecoAttPrincipale=aziendaS.codiceAtecoAttPrincipale.__repr__(),
                       descrizioneAttPrincipale=aziendaS.descrizioneAttPrincipale.__repr__(),
                       versione=2,   #fixme: aziendaS.versione.__repr__(), mi restituisce '2L' e non va bene
                       idSIS=aziendaS.idSIS.__repr__()
                       )
            self._config_obj.session.merge(az)
            self._config_obj.session.commit()
            response="Ok"
        except:
            response="Ko"
        return response
