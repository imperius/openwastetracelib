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
This package contains the schde managment methods defined by Sistri.
For more details on each, refer to the respective class's documentation.
"""

from .. objects import Causali_mov, Movimentazione
from .. base_service import OWTBaseService, OWTError


class OWTInvalidMovimentazione(OWTError):
    """
    Exception: Sent when a an error related invalid Movimentazione id.
    """
    pass


class GettingElencoMovimentazioniRequest(OWTBaseService):
    """
    This class allows you to get ElencoMovimentazioni object.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends a get ElencoMovimentazioni request. The optional keyword args
        detailed on OWTBaseService apply here as well.
        config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.parametriAggiuntivi = None
        self.filtroMovimentazioni = None
        self.startItemPosition = None
        super(GettingElencoMovimentazioniRequest, self).__init__(
            self._config_obj, *args, **kwargs)
        """
        Call the parent OWTBaseService class for basic setup work.
        """

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
        warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        session = self._config_obj.session
        longStartItemPosition = self.client.factory.create('LongNumber')
        longStartItemPosition.long = self.startItemPosition
        parm = dict(identity=self.identity,
                    parametriAggiuntivi=self.parametriAggiuntivi,
                    filtroMovimentazioni=self.filtroMovimentazioni,
                    startItemPosition=longStartItemPosition)
        elencoMovimentazioni = None
        try:
            elencoMovimentazioni = \
                client.service.GetElencoMovimentazioni(**parm)
        except Exception, e:
            response = \
                e.fault.detail.GetElencoMovimentazioni_fault.errorMessage
        try:
            if elencoMovimentazioni:
                if 'movimentazioni' in elencoMovimentazioni:
                    movimentazioniSistri = elencoMovimentazioni.movimentazioni
                    for movimentazioneSistri in movimentazioniSistri:
                        causaleFineMovimentazione = None
                        if 'causaleFineMovimentazione' in movimentazioneSistri:
                            causaleFineSistri = \
                                movimentazioneSistri.causaleFineMovimentazione
                            causaleFineMovimentazione = Causali_mov(
                                id_causale_mov=causaleFineSistri.\
                                    idCatalogo.__repr__(),
                                descrizione_causale_mov=causaleFineSistri.\
                                    description.__repr__()
                            )
                            res = session.query(Causali_mov).filter(
                                Causali_mov.id_causale_mov == \
                                causaleFineMovimentazione.\
                                id_causale_mov)
                            if res.count() > 0:
                                causaleFineMovimentazione = res.first()
                        idSIS = None
                        if 'idSIS' in movimentazioneSistri:
                            idSIS = movimentazioneSistri.idSIS
                        idSISTRI = None
                        if 'idSISTRI' in movimentazioneSistri:
                            idSISTRI = movimentazioneSistri.idSISTRI
                        versione = None
                        if 'versione' in movimentazioneSistri:
                            versione = movimentazioneSistri.versione.long
                        movimentazioneNumeroSerie = None
                        if 'movimentazioneNumeroSerie' in movimentazioneSistri:
                            movimentazioneNumeroSerie = \
                                movimentazioneSistri.movimentazioneNumeroSerie
                        dataMovimentazione = None
                        if 'dataMovimentazione' in movimentazioneSistri:
                            dataMovimentazione = \
                                movimentazioneSistri.dataMovimentazione
                        dataOraFineMovimentazione = None
                        if 'dataOraFineMovimentazione' in movimentazioneSistri:
                            dataOraFineMovimentazione = \
                                movimentazioneSistri.dataOraFineMovimentazione
                        movimentazione = Movimentazione(
                            idSIS=idSIS,
                            idSISTRI=idSISTRI,
                            versione=versione,
                            dataMovimentazione=dataMovimentazione,
                            movimentazioneNumeroSerie=movimentazioneNumeroSerie,
                            dataOraFineMovimentazione=dataOraFineMovimentazione,
                            causaleFineMovimentazione=causaleFineMovimentazione
                        )
                        session.merge(movimentazione)
                session.commit()
                response = "Ok"
                if elencoMovimentazioni.info:
                    for info in elencoMovimentazioni.info:
                        response += info
        except Exception, e:
            response = e
        return response
