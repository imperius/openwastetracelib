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
This package contains the anagrafiche managment methods defined by Sistri.
For more details on each, refer to the respective class's documentation.
"""

from .. objects import Azienda, Forme_giuridiche, Tipi_stato_impresa, \
    Tipi_sede, Sede, Camere_commercio, Associazioni_categoria, \
    Sottocategorie_star, Tipi_veicolo, Stati_veicolo, Sottotipi_veicolo, \
    Codici_cer_iii_livello, Veicolo, Stati_registro_cronologico, \
    RegistroCronologico, Tipi_reg_cronologico
from .. base_service import OWTBaseService, OWTError


class OWTInvalidAzienda(OWTError):
    """
    Exception: Sent when a an error related invalid Azienda id.
    """
    pass


class UpdatingAziendaRequest(OWTBaseService):
    """
    This class allows you to update an Azienda object.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends a get azienda request. The optional keyword args
        detailed on OWTBaseService apply here as well.
        config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.codiceFiscaleAzienda = None
        # Call the parent OWTBaseService class for basic setup work.
        super(UpdatingAziendaRequest, self).__init__(self._config_obj,
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
        warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        session = self._config_obj.session
        aziendaAllineata = 0
        response = "None"
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    codiceFiscaleAzienda=self.codiceFiscaleAzienda)
        try:
            versioneAnagraficaAzienda = \
                client.service.GetVersioneAnagraficaAzienda(**parm)
            aziendaAllineata = session.query(Azienda).\
                filter(Azienda.codiceFiscale == parm['codiceFiscaleAzienda']).\
                filter(Azienda.versione == versioneAnagraficaAzienda.long).\
                count()
        except Exception, e:
            response = e
        if not aziendaAllineata > 0:
            azienda = GettingAziendaRequest(self._config_obj)
            azienda.codiceFiscaleAzienda = self.codiceFiscaleAzienda
            azienda.identity = self.identity
            azienda.send_request()
            response = azienda.response
        sedi = []
        try:
            if session.query(Azienda).filter(Azienda.codiceFiscale == \
                parm['codiceFiscaleAzienda']).count() > 0:
                azienda = session.query(Azienda).\
                    filter(Azienda.codiceFiscale == \
                    parm['codiceFiscaleAzienda']).first()
                sedi = azienda.sediSummary
        except Exception, e:
            response = e
        for sede in sedi:
            veicolo = GettingVeicoliRequest(self._config_obj)
            veicolo.identity = self.identity
            veicolo.idSISSede = sede.idSIS
            veicolo.send_request()
            response = veicolo.response
        for sede in sedi:
            registroCronologico = GettingRegistroCronologicoRequest(
                self._config_obj)
            registroCronologico.identity = self.identity
            registroCronologico.idSISSede = sede.idSIS
            registroCronologico.send_request()
            response = registroCronologico.response
        return response


class GettingAziendaRequest(OWTBaseService):
    """
    This class allows you to get an Azienda object.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends a get azienda request. The optional keyword args
        detailed on OWTBaseService apply here as well.
        config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.codiceFiscaleAzienda = None
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingAziendaRequest, self).__init__(self._config_obj,
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
        warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    codiceFiscaleAzienda=self.codiceFiscaleAzienda)
        aziendaSistri = None
        try:
            aziendaSistri = client.service.GetAzienda(**parm)
        except Exception, e:
            response = e.fault.detail.GetAzienda_fault.errorMessage
        try:
            if aziendaSistri:
                sediSummary = []
                if aziendaSistri.sediSummary:
                    for sedeSummary in aziendaSistri.sediSummary:
                        tipoSede = None
                        if sedeSummary.tipoSede:
                            tipoSede = Tipi_sede(
                                id_tipo_sede=sedeSummary.tipoSede.idCatalogo.\
                                    __repr__(),
                                descrizione=sedeSummary.tipoSede.description.\
                                    __repr__()
                            )
                            if session.query(Tipi_sede).filter(Tipi_sede.\
                                id_tipo_sede == tipoSede.id_tipo_sede).\
                                count() > 0:
                                tipoSede = session.query(Tipi_sede).filter(
                                    Tipi_sede.id_tipo_sede == tipoSede.\
                                    id_tipo_sede).first()
                        sede = Sede(
                            idSIS=sedeSummary.idSIS.__repr__(),
                            nomeSede=sedeSummary.nomeSede.__repr__(),
                            codiceIstatLocalita=sedeSummary.\
                                codiceIstatLocalita.__repr__(),
                            codiceCatastale=sedeSummary.codiceCatastale.\
                                __repr__(),
                            nazione=sedeSummary.nazione.__repr__(),
                            siglaNazione=sedeSummary.siglaNazione.__repr__(),
                            indirizzo=sedeSummary.indirizzo.__repr__(),
                            nrCivico=sedeSummary.nrCivico.__repr__(),
                            cap=sedeSummary.cap.__repr__(),
                            versione=sedeSummary.versione.long,
                            tipoSede=tipoSede
                        )
                        if session.query(Sede).filter(Sede.idSIS == \
                            sede.idSIS).count() > 0:
                            sede = session.query(Sede).filter(Sede.idSIS == \
                                sede.idSIS).first()
                        sediSummary.append(sede)
                        session.merge(sede)
                sedeLegale = None
                if aziendaSistri.sedeLegale:
                    sedeLegaleSistri = aziendaSistri.sedeLegale
                    tipoSede = None
                    if sedeLegaleSistri.tipoSede:
                        tipoSedeSistri = sedeLegaleSistri.tipoSede
                        tipoSede = Tipi_sede(
                            id_tipo_sede=tipoSedeSistri.idCatalogo.__repr__(),
                            descrizione=tipoSedeSistri.description.__repr__()
                        )
                        if session.query(Tipi_sede).filter(Tipi_sede.\
                            id_tipo_sede == tipoSede.id_tipo_sede).count() > 0:
                            tipoSede = session.query(Tipi_sede).filter(
                                Tipi_sede.id_tipo_sede == \
                                tipoSede.id_tipo_sede).first()
                    sedeLegale = Sede(
                        idSIS=sedeLegaleSistri.idSIS.__repr__(),
                        nomeSede=sedeLegaleSistri.nomeSede.__repr__(),
                        codiceIstatLocalita=sedeLegaleSistri.\
                            codiceIstatLocalita.__repr__(),
                        codiceCatastale=sedeLegaleSistri.codiceCatastale.\
                            __repr__(),
                        nazione=sedeLegaleSistri.nazione.__repr__(),
                        siglaNazione=sedeLegaleSistri.siglaNazione.__repr__(),
                        indirizzo=sedeLegaleSistri.indirizzo.__repr__(),
                        nrCivico=sedeLegaleSistri.nrCivico.__repr__(),
                        cap=sedeLegaleSistri.cap.__repr__(),
                        versione=sedeLegaleSistri.versione.long,
                        tipoSede=tipoSede
                    )
                    if session.query(Sede).filter(Sede.idSIS == \
                        sedeLegale.idSIS).count() > 0:
                        sedeLegale = session.query(Sede).filter(Sede.idSIS == \
                            sedeLegale.idSIS).first()
                formaGiuridica = None
                if aziendaSistri.formaGiuridica:
                    formaGiuridica = Forme_giuridiche(
                        id_tipo_forma_giuridica=aziendaSistri.formaGiuridica.\
                            idCatalogo.__repr__(),
                        descrizione_forma_giuridica=aziendaSistri.\
                            formaGiuridica.description.__repr__(),
                    )
                    if session.query(Forme_giuridiche).filter(\
                        Forme_giuridiche.id_tipo_forma_giuridica == \
                        formaGiuridica.id_tipo_forma_giuridica).count() > 0:
                        formaGiuridica = session.query(Forme_giuridiche).\
                            filter(Forme_giuridiche.id_tipo_forma_giuridica \
                            == formaGiuridica.id_tipo_forma_giuridica).first()
                tipoStatoImpresa = None
                if aziendaSistri.tipoStatoImpresa:
                    tipoStatoImpresa = Tipi_stato_impresa(
                        id_tipo_stato_impresa=aziendaSistri.tipoStatoImpresa.\
                            idCatalogo.__repr__()
                    )
                    if session.query(Tipi_stato_impresa).\
                        filter(Tipi_stato_impresa.id_tipo_stato_impresa == \
                        tipoStatoImpresa.id_tipo_stato_impresa).count() > 0:
                        tipoStatoImpresa = session.query(Tipi_stato_impresa).\
                            filter(Tipi_stato_impresa.id_tipo_stato_impresa \
                                == tipoStatoImpresa.id_tipo_stato_impresa).\
                                first()
                azienda = Azienda(
                    idSIS=aziendaSistri.idSIS.__repr__(),
                    ragioneSociale=aziendaSistri.ragioneSociale.__repr__(),
                    cognome=aziendaSistri.cognome.__repr__(),
                    nome=aziendaSistri.nome.__repr__(),
                    codiceFiscale=aziendaSistri.codiceFiscale.__repr__(),
                    pIva=aziendaSistri.pIva.__repr__(),
                    numeroIscrizioneAlbo=aziendaSistri.numeroIscrizioneAlbo.\
                        __repr__(),
                    cciaaRea=aziendaSistri.cciaaRea.__repr__(),
                    numeroIscrizioneRea=aziendaSistri.numeroIscrizioneRea.\
                        __repr__(),
                    codiceIstatAttPrincipale=aziendaSistri.\
                        codiceIstatAttPrincipale.__repr__(),
                    dataIscrizioneStar=aziendaSistri.dataIscrizioneStar,
                    codiceAtecoAttPrincipale=aziendaSistri.\
                        codiceAtecoAttPrincipale.__repr__(),
                    descrizioneAttPrincipale=aziendaSistri.\
                        descrizioneAttPrincipale.__repr__(),
                    versione=aziendaSistri.versione.long,
                    sedeLegale=sedeLegale,
                    formaGiuridica=formaGiuridica,
                    tipoStatoImpresa=tipoStatoImpresa,
                    sediSummary=sediSummary,
                )
                session.merge(azienda)
                session.commit()
                response = "Ok"
        except Exception, e:
            response = e
        return response


class GettingSedeRequest(OWTBaseService):
    """
    This class allows you to get an Sede object.
    By default, you can simply pass a identity string to the constructor.
    """
    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends a get azienda request. The optional keyword args
        detailed on OWTBaseService apply here as well.
        config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.idSIS = None
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingSedeRequest, self).__init__(self._config_obj,
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
        warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    idSIS=self.idSIS)
        sedeSistri = None
        try:
            sedeSistri = client.service.GetSede(**parm)
        except Exception, e:
            response = e.fault.detail.GetSede_fault.errorMessage
        try:
            if sedeSistri:
                sottocategorie = []
                if sedeSistri.sottocategorie:
                    for sottocategoria in sedeSistri.sottocategorie:
                        sottocategorie_star = Sottocategorie_star(
                            id_sottocategoria_star=sottocategoria.idCatalogo.\
                                __repr__(),
                            descrizione_sottocategoria=sottocategoria.\
                            description.__repr__()
                        )
                        if session.query(Sottocategorie_star).\
                            filter(Sottocategorie_star.id_sottocategoria_star \
                            == sottocategorie_star.id_sottocategoria_star).\
                            count() > 0:
                            sottocategorie_star = session.\
                                query(Sottocategorie_star).\
                                filter(Sottocategorie_star.\
                                id_sottocategoria_star == sottocategorie_star.\
                                id_sottocategoria_star).first()
                        sottocategorie.append(sottocategorie_star)
                tipoSede = None
                if sedeSistri.tipoSede:
                    tipoSede = Tipi_sede(
                        id_tipo_sede=sedeSistri.tipoSede.idCatalogo.__repr__(),
                        descrizione=sedeSistri.tipoSede.description.__repr__()
                    )
                    if session.query(Tipi_sede).filter(Tipi_sede.id_tipo_sede \
                        == tipoSede.id_tipo_sede).count() > 0:
                        tipoSede = session.query(Tipi_sede).filter(Tipi_sede.\
                            id_tipo_sede == tipoSede.id_tipo_sede).first()
                cameraCommercio = None
                if sedeSistri.cameraCommercio:
                    cameraCommercio = Camere_commercio(
                        id_camera_commercio=sedeSistri.cameraCommercio.\
                        idCatalogo.__repr__()
                    )
                    if session.query(Camere_commercio).filter(
                        Camere_commercio.id_camera_commercio == \
                        cameraCommercio.id_camera_commercio).count() > 0:
                        cameraCommercio = session.query(Camere_commercio).\
                            filter(Camere_commercio.id_camera_commercio == \
                            cameraCommercio.id_camera_commercio).first()
                associazioneCategoria = None
                if sedeSistri.associazioneCategoria:
                    associazioneCategoria = Associazioni_categoria(
                        id_associazione_categoria=sedeSistri.\
                            associazioneCategoria.idCatalogo.__repr__()
                    )
                    if session.query(Associazioni_categoria).\
                        filter(Associazioni_categoria.\
                        id_associazione_categoria == associazioneCategoria.\
                        id_associazione_categoria).count() > 0:
                        associazioneCategoria = session.\
                            query(Associazioni_categoria).\
                            filter(Associazioni_categoria.\
                            id_associazione_categoria == \
                            associazioneCategoria.id_associazione_categoria).\
                            first()
                sede = Sede(
                    idSIS=sedeSistri.idSIS.__repr__(),
                    nomeSede=sedeSistri.nomeSede.__repr__(),
                    codiceIstatLocalita=sedeSistri.codiceIstatLocalita.\
                        __repr__(),
                    codiceCatastale=sedeSistri.codiceCatastale.__repr__(),
                    nazione=sedeSistri.nazione.__repr__(),
                    siglaNazione=sedeSistri.siglaNazione.__repr__(),
                    indirizzo=sedeSistri.indirizzo.__repr__(),
                    nrCivico=sedeSistri.nrCivico.__repr__(),
                    cap=sedeSistri.cap.__repr__(),
                    versione=sedeSistri.versione.long,
                    telefono=sedeSistri.telefono.__repr__(),
                    fax=sedeSistri.fax.__repr__(),
                    numeroAddetti=sedeSistri.numeroAddetti.long,
                    codiceIstatAttPrincipale=sedeSistri.\
                        codiceIstatAttPrincipale.__repr__(),
                    codiceAtecoAttPrincipale=sedeSistri.\
                        codiceAtecoAttPrincipale.__repr__(),
                    descrizioneAttPrincipale=sedeSistri.\
                        descrizioneAttPrincipale.__repr__(),
                    numeroIscrizioneRea=sedeSistri.numeroIscrizioneRea.\
                        __repr__(),
                    numeroUla=sedeSistri.numeroUla.double,
                    latitudine=sedeSistri.latitudine.double,
                    longitudine=sedeSistri.longitudine.double,
                    tipoSede=tipoSede,
                    cameraCommercio=cameraCommercio,
                    associazioneCategoria=associazioneCategoria,
                    sottocategorie=sottocategorie
                )
                session.merge(sede)
                session.commit()
                response = "Ok"
        except Exception, e:
            response = e
        return response


class GettingVeicoliRequest(OWTBaseService):
    """
    This class allows you to updating all Veicoli objects.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends an update cataloghi request. The optional keyword args
        detailed on OWTBaseService apply here as well.
        config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.idSISSede = None
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingVeicoliRequest, self).\
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
        warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        response = "None"
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    idSISSede=self.idSISSede)
        veicoliSistri = None
        try:
            veicoliSistri = client.service.GetVeicoli(**parm)
        except Exception, e:
            response = e.fault.detail.GetVeicoli_fault.errorMessage
        try:
            if veicoliSistri:
                sede = None
                if session.query(Sede).filter(
                    Sede.idSIS == parm['idSISSede']).count() > 0:
                    sede = session.query(Sede).filter(
                        Sede.idSIS == parm['idSISSede']).first()
                for veicoloSistri in veicoliSistri:
                    tipoVeicolo = None
                    if veicoloSistri.tipoVeicolo:
                        tipoVeicoloSistri = veicoloSistri.tipoVeicolo
                        descrizione = None
                        if tipoVeicoloSistri.description:
                            descrizione = tipoVeicoloSistri.description
                        if tipoVeicoloSistri.idCatalogo:
                            tipoVeicolo = Tipi_veicolo(
                                id_tipo_veicolo=tipoVeicoloSistri.idCatalogo,
                                descrizione=descrizione
                            )
                        if session.query(Tipi_veicolo).filter(
                            Tipi_veicolo.id_tipo_veicolo == \
                            tipoVeicolo.id_tipo_veicolo).count() > 0:
                            tipoVeicolo = session.query(Tipi_veicolo).filter(
                                Tipi_veicolo.id_tipo_veicolo == \
                                tipoVeicolo.id_tipo_veicolo).first()
                    statoVeicolo = None
                    if veicoloSistri.statoVeicolo:
                        statoVeicoloSistri = veicoloSistri.statoVeicolo
                        descrizione = None
                        if statoVeicoloSistri.description:
                            descrizione = statoVeicoloSistri.description
                        if statoVeicoloSistri.idCatalogo:
                            statoVeicolo = Stati_veicolo(
                                id_stato_veicolo=statoVeicoloSistri.idCatalogo,
                                descrizione_stato_veicolo=descrizione
                            )
                        if session.query(Stati_veicolo).filter(
                            Stati_veicolo.id_stato_veicolo == \
                            statoVeicolo.id_stato_veicolo).count() > 0:
                            statoVeicolo = session.query(Stati_veicolo).filter(
                                Stati_veicolo.id_stato_veicolo == \
                                statoVeicolo.id_stato_veicolo).first()
                    sottotipoVeicolo = None
                    if veicoloSistri.sottotipoVeicolo:
                        sottotipoVeicoloSistri = veicoloSistri.sottotipoVeicolo
                        descrizione = None
                        if sottotipoVeicoloSistri.description:
                            descrizione = sottotipoVeicoloSistri.description
                        if sottotipoVeicoloSistri.idCatalogo:
                            sottotipoVeicolo = Sottotipi_veicolo(
                                id_sottotipo_veicolo=sottotipoVeicoloSistri.\
                                    idCatalogo,
                                descrizione=descrizione
                            )
                        if session.query(Sottotipi_veicolo).filter(
                            Sottotipi_veicolo.id_sottotipo_veicolo == \
                            sottotipoVeicolo.id_sottotipo_veicolo).count() > 0:
                            sottotipoVeicolo = session.query(
                                Sottotipi_veicolo).filter(Sottotipi_veicolo.\
                                id_sottotipo_veicolo == sottotipoVeicolo.\
                                id_sottotipo_veicolo).first()
                    codiciCerIIILivello = []
                    if veicoloSistri.codiciCerIIILivello:
                        codiciCerIIILivelloSistri = veicoloSistri.\
                            codiciCerIIILivello
                        for codiceCerIIILivello in codiciCerIIILivelloSistri:
                            descrizione = None
                            if codiceCerIIILivello.description:
                                descrizione = codiceCerIIILivello.description
                            if codiceCerIIILivello.idCatalogo:
                                id = codiceCerIIILivello.idCatalogo
                                codici_cer_iii_livello = \
                                    Codici_cer_iii_livello(
                                    id_codice_cer_iii_livello=id,
                                    descrizione_iii_livello=descrizione
                                )
                            if session.query(Codici_cer_iii_livello).\
                                filter(Codici_cer_iii_livello.\
                                id_codice_cer_iii_livello == \
                                codici_cer_iii_livello.\
                                id_codice_cer_iii_livello).count() > 0:
                                codici_cer_iii_livello = session.\
                                    query(Codici_cer_iii_livello).\
                                    filter(Codici_cer_iii_livello.\
                                    id_codice_cer_iii_livello == \
                                    codici_cer_iii_livello.\
                                    id_codice_cer_iii_livello).first()
                            codiciCerIIILivello.append(codici_cer_iii_livello)
                    marca = None
                    if veicoloSistri.marca:
                        marca = veicoloSistri.marca
                    modello = None
                    if veicoloSistri.modello:
                        modello = veicoloSistri.modello
                    annoImmatricolazione = None
                    if veicoloSistri.annoImmatricolazione:
                        annoImmatricolazione = veicoloSistri.\
                            annoImmatricolazione.long
                    if veicoloSistri.targa:
                        veicolo = Veicolo(
                            targa=veicoloSistri.targa,
                            marca=marca,
                            modello=modello,
                            annoImmatricolazione=annoImmatricolazione,
                            sede=sede,
                            tipoVeicolo=tipoVeicolo,
                            statoVeicolo=statoVeicolo,
                            sottotipoVeicolo=sottotipoVeicolo,
                            codiciCerIIILivello=codiciCerIIILivello
                        )
                        session.merge(veicolo)
                session.commit()
                response = "Ok"
        except Exception, e:
            response = e
        return response


class GettingRegistroCronologicoRequest(OWTBaseService):
    """
    This class allows you to updating all RegistroCronologico objects.
    By default, you can simply pass a identity string to the constructor.
    """

    def __init__(self, config_obj, *args, **kwargs):
        """
        Sends an update cataloghi request. The optional keyword args
        detailed on OWTBaseService apply here as well.
        config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = None
        self.idSISSede = None
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingRegistroCronologicoRequest, self).\
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
        warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
        WHICH RESIDESON OWTBaseService AND IS INHERITED.
        """
        response = "None"
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    idSISSede=self.idSISSede)
        registroCronologicoSistri = None
        try:
            registroCronologicoSistri = client.service.\
                GetRegistroCronologico(**parm)
        except Exception, e:
#            import pdb; pdb.set_trace()
            response = e.fault.detail.GetRegistroCronologico_fault.errorMessage
        try:
            if registroCronologicoSistri:
                sede = None
                if session.query(Sede).filter(
                    Sede.idSIS == parm['idSISSede']).count() > 0:
                    sede = session.query(Sede).filter(
                        Sede.idSIS == parm['idSISSede']).first()
                for registroSistri in registroCronologicoSistri:
                    statoRegistroCronologico = None
                    if 'statoRegistroCronologico' in registroSistri:
                        statoRegistroSistri = registroSistri.\
                            statoRegistroCronologico
                        statoRegistroCronologico = Stati_registro_cronologico(
                            id_stato_registro_cronologico=statoRegistroSistri.\
                                idCatalogo.__repr__(),
                            descrizione_stato_reg_crono=statoRegistroSistri.\
                                description.__repr__()
                        )
                        if session.query(Stati_registro_cronologico).filter(
                            Stati_registro_cronologico.\
                            id_stato_registro_cronologico == \
                            statoRegistroCronologico.\
                            id_stato_registro_cronologico).count() > 0:
                            statoRegistroCronologico = session.query(\
                                Stati_registro_cronologico).filter(\
                                Stati_registro_cronologico.\
                                id_stato_registro_cronologico == \
                                statoRegistroCronologico.\
                                id_stato_registro_cronologico).first()
                    tipoRegCronologico = None
                    if 'tipoRegCronologico' in registroSistri:
                        tipoRegSistri = registroSistri.tipoRegCronologico
                        tipoRegCronologico = Tipi_reg_cronologico(
                            id_tipo_reg_cronologico=tipoRegSistri.\
                                idCatalogo.__repr__(),
                            descrizione_tipo_reg_crono=tipoRegSistri.\
                                description.__repr__()
                        )
                        if session.query(Tipi_reg_cronologico).filter(
                            Tipi_reg_cronologico.id_tipo_reg_cronologico == \
                            tipoRegCronologico.id_tipo_reg_cronologico).\
                            count() > 0:
                            tipoRegCronologico = session.query(
                                Tipi_reg_cronologico).filter(
                                Tipi_reg_cronologico.id_tipo_reg_cronologico \
                                == tipoRegCronologico.\
                                id_tipo_reg_cronologico).first()
                    sottocategoria = None
                    if 'sottocategoria' in registroSistri:
                        sottocategoriaSistri = registroSistri.sottocategoria
                        sottocategoria = Sottocategorie_star(
                            id_sottocategoria_star=sottocategoriaSistri.\
                                idCatalogo.__repr__(),
                            descrizione_sottocategoria=sottocategoriaSistri.\
                                description.__repr__()
                        )
                        if session.query(Sottocategorie_star).filter(
                            Sottocategorie_star.id_sottocategoria_star == \
                            sottocategoria.id_sottocategoria_star).count() > 0:
                            sottocategoria = session.query(
                                Sottocategorie_star).filter(
                                Sottocategorie_star.id_sottocategoria_star \
                                == sottocategoria.id_sottocategoria_star).\
                                first()
                    idSIS = None
                    if 'idSIS' in registroSistri:
                        idSIS = registroSistri.idSIS
                    codiceRegistroCronologico = None
                    if 'codiceRegistroCronologico' in registroSistri:
                        codiceRegistroCronologico = registroSistri.\
                            codiceRegistroCronologico.__repr__()
                    nomeUnitaOperativa = None
                    if 'nomeUnitaOperativa' in registroSistri:
                        nomeUnitaOperativa = registroSistri.\
                            nomeUnitaOperativa.__repr__()
                    versione = None
                    if 'versione' in registroSistri:
                        versione = registroSistri.versione.long
                    ultimoNumero = None
                    if 'ultimoNumero' in registroSistri:
                        ultimoNumero = registroSistri.ultimoNumero.long
                    dataUltimoNumero = None
                    if 'dataUltimoNumero' in registroSistri:
                        dataUltimoNumero = registroSistri.dataUltimoNumero.long
                    registroCronologico = RegistroCronologico(
                        idSIS=idSIS,
                        codiceRegistroCronologico=codiceRegistroCronologico,
                        nomeUnitaOperativa=nomeUnitaOperativa,
                        dataUltimoNumero=dataUltimoNumero,
                        versione=versione,
                        ultimoNumero=ultimoNumero,
                        idSISSede=sede,
                        statoRegistroCronologico=statoRegistroCronologico,
                        tipoRegCronologico=tipoRegCronologico,
                        sottocategoria=sottocategoria
                    )
                    session.merge(registroCronologico)
                session.commit()
                response = "Ok"
        except Exception, e:
            response = e
        return response
