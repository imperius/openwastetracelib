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
    Codici_cer_iii_livello, Veicolo
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
        aziendaAllineata = 0
        response = "None"
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    codiceFiscaleAzienda=self.codiceFiscaleAzienda)
#        try:
        versioneAnagraficaAzienda = \
            client.service.GetVersioneAnagraficaAzienda(**parm)
        aziendaAllineata = session.query(Azienda).\
            filter(Azienda.codiceFiscale == parm['codiceFiscaleAzienda']).\
            filter(Azienda.versione == versioneAnagraficaAzienda.long).count()
#        except Exception, e:
#            response = e
        if aziendaAllineata <= 0:
            aziendaSistri = client.service.GetAzienda(**parm)
#        try:
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
                            id_tipo_sede == tipoSede.id_tipo_sede).count() > 0:
                            tipoSede = session.query(Tipi_sede).filter(
                                Tipi_sede.id_tipo_sede == tipoSede.\
                                id_tipo_sede).first()
                    sede = Sede(
                        idSIS=sedeSummary.idSIS.__repr__(),
                        nomeSede=sedeSummary.nomeSede.__repr__(),
                        codiceIstatLocalita=sedeSummary.codiceIstatLocalita.\
                            __repr__(),
                        codiceCatastale=sedeSummary.codiceCatastale.__repr__(),
                        nazione=sedeSummary.nazione.__repr__(),
                        siglaNazione=sedeSummary.siglaNazione.__repr__(),
                        indirizzo=sedeSummary.indirizzo.__repr__(),
                        nrCivico=sedeSummary.nrCivico.__repr__(),
                        cap=sedeSummary.cap.__repr__(),
                        versione=sedeSummary.versione.long,
                        tipoSede=tipoSede
                    )
                    if session.query(Sede).filter(Sede.idSIS == sede.idSIS).\
                        count() > 0:
                        sede = session.query(Sede).filter(Sede.idSIS == sede.\
                            idSIS).first()
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
                        tipoSede = session.query(Tipi_sede).filter(Tipi_sede.\
                            id_tipo_sede == tipoSede.id_tipo_sede).first()
                sedeLegale = Sede(
                    idSIS=sedeLegaleSistri.idSIS.__repr__(),
                    nomeSede=sedeLegaleSistri.nomeSede.__repr__(),
                    codiceIstatLocalita=sedeLegaleSistri.codiceIstatLocalita.\
                        __repr__(),
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
                if session.query(Sede).filter(Sede.idSIS == sedeLegale.idSIS).\
                    count() > 0:
                    sedeLegale = session.query(Sede).filter(Sede.idSIS == \
                        sedeLegale.idSIS).first()
            formaGiuridica = None
            if aziendaSistri.formaGiuridica:
                formaGiuridica = Forme_giuridiche(
                    id_tipo_forma_giuridica=aziendaSistri.formaGiuridica.\
                        idCatalogo.__repr__(),
                    descrizione_forma_giuridica=aziendaSistri.formaGiuridica.\
                        description.__repr__(),
                )
                if session.query(Forme_giuridiche).filter(Forme_giuridiche.\
                    id_tipo_forma_giuridica == formaGiuridica.\
                    id_tipo_forma_giuridica).count() > 0:
                    formaGiuridica = session.query(Forme_giuridiche).\
                        filter(Forme_giuridiche.id_tipo_forma_giuridica == \
                        formaGiuridica.id_tipo_forma_giuridica).first()
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
                        filter(Tipi_stato_impresa.id_tipo_stato_impresa == \
                            tipoStatoImpresa.id_tipo_stato_impresa).first()
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
#        except Exception, e:
#            response = e
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
        sedeSistri = client.service.GetSede(**parm)
        try:
            sottocategorie = []
            if sedeSistri.sottocategorie:
                for sottocategoria in sedeSistri.sottocategorie:
                    sottocategorie_star = Sottocategorie_star(
                        id_sottocategoria_star=sottocategoria.idCatalogo.\
                            __repr__(),
                        descrizione_sottocategoria=sottocategoria.description.\
                            __repr__()
                    )
                    if session.query(Sottocategorie_star).\
                        filter(Sottocategorie_star.id_sottocategoria_star == \
                        sottocategorie_star.id_sottocategoria_star).\
                        count() > 0:
                        sottocategorie_star = session.\
                            query(Sottocategorie_star).\
                            filter(Sottocategorie_star.id_sottocategoria_star \
                            == sottocategorie_star.id_sottocategoria_star).\
                            first()
                    sottocategorie.append(sottocategorie_star)
            tipoSede = None
            if sedeSistri.tipoSede:
                tipoSede = Tipi_sede(
                    id_tipo_sede=sedeSistri.tipoSede.idCatalogo.__repr__(),
                    descrizione=sedeSistri.tipoSede.description.__repr__()
                )
                if session.query(Tipi_sede).filter(Tipi_sede.id_tipo_sede == \
                    tipoSede.id_tipo_sede).count() > 0:
                    tipoSede = session.query(Tipi_sede).filter(Tipi_sede.\
                        id_tipo_sede == tipoSede.id_tipo_sede).first()
            cameraCommercio = None
            if sedeSistri.cameraCommercio:
                cameraCommercio = Camere_commercio(
                    id_camera_commercio=sedeSistri.cameraCommercio.idCatalogo.\
                        __repr__()
                )
                if session.query(Camere_commercio).filter(Camere_commercio.\
                    id_camera_commercio == cameraCommercio.\
                    id_camera_commercio).count() > 0:
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
                    filter(Associazioni_categoria.id_associazione_categoria\
                    == associazioneCategoria.id_associazione_categoria).\
                    count() > 0:
                    associazioneCategoria = session.\
                        query(Associazioni_categoria).\
                        filter(Associazioni_categoria.\
                        id_associazione_categoria == associazioneCategoria.\
                        id_associazione_categoria).first()
            sede = Sede(
                idSIS=sedeSistri.idSIS.__repr__(),
                nomeSede=sedeSistri.nomeSede.__repr__(),
                codiceIstatLocalita=sedeSistri.codiceIstatLocalita.__repr__(),
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
                codiceIstatAttPrincipale=sedeSistri.codiceIstatAttPrincipale.\
                    __repr__(),
                codiceAtecoAttPrincipale=sedeSistri.codiceAtecoAttPrincipale.\
                    __repr__(),
                descrizioneAttPrincipale=sedeSistri.descrizioneAttPrincipale.\
                    __repr__(),
                numeroIscrizioneRea=sedeSistri.numeroIscrizioneRea.__repr__(),
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
    This class allows you to updating all gVeicoli objects.
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
        client = self.client
        session = self._config_obj.session
        parm = dict(identity=self.identity,
                    parametriAggiuntivi="",
                    idSISSede=self.idSISSede)
        veicoliSistri = client.service.GetVeicoli(**parm)
        try:
#            sede = None
#            if session.query(Sede).filter(
#                Sede.idSIS == parm['idSISSede']).count() > 0:
#                sede = session.query(Sede).filter(
#                    Sede.idSIS == parm['idSISSede']).first()
            for veicoloSistri in veicoliSistri:
                tipoVeicolo = None
                if veicoloSistri.tipoVeicolo:
                    tipoVeicoloSistri = veicoloSistri.tipoVeicolo
                    tipoVeicolo = Tipi_veicolo(
                        id_tipo_veicolo=tipoVeicoloSistri.idCatalogo.\
                            __repr__(),
                        descrizione=tipoVeicoloSistri.description.__repr__()
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
                    statoVeicolo = Stati_veicolo(
                        id_stato_veicolo=statoVeicoloSistri.idCatalogo.\
                            __repr__(),
                        descrizione_stato_veicolo=statoVeicoloSistri.\
                            description.__repr__()
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
                    sottotipoVeicolo = Sottotipi_veicolo(
                        id_sottotipo_veicolo=sottotipoVeicoloSistri.\
                            idCatalogo.__repr__(),
                        descrizione=sottotipoVeicoloSistri.description.\
                            __repr__()
                    )
                    if session.query(Sottotipi_veicolo).filter(
                        Sottotipi_veicolo.id_sottotipo_veicolo == \
                        sottotipoVeicolo.id_sottotipo_veicolo).count() > 0:
                        sottotipoVeicolo = session.query(Sottotipi_veicolo).\
                            filter(Sottotipi_veicolo.id_sottotipo_veicolo == \
                            sottotipoVeicolo.id_sottotipo_veicolo).first()
                codiciCerIIILivello = []
                if veicoloSistri.codiciCerIIILivello:
                    codiciCerIIILivelloSistri = veicoloSistri.\
                        codiciCerIIILivello
                    for codiceCerIIILivello in codiciCerIIILivelloSistri:
                        codici_cer_iii_livello = Codici_cer_iii_livello(
                            id_codice_cer_iii_livello=codiceCerIIILivello.\
                                idCatalogo.__repr__(),
                            descrizione_iii_livello=codiceCerIIILivello.\
                                description.__repr__()
                        )
                        if session.query(Codici_cer_iii_livello).\
                            filter(Codici_cer_iii_livello.\
                            id_codice_cer_iii_livello == \
                            codici_cer_iii_livello.id_codice_cer_iii_livello).\
                            count() > 0:
                            codici_cer_iii_livello = session.\
                                query(Codici_cer_iii_livello).\
                                filter(Codici_cer_iii_livello.\
                                id_codice_cer_iii_livello == \
                                codici_cer_iii_livello.\
                                id_codice_cer_iii_livello).first()
                        codiciCerIIILivello.append(codici_cer_iii_livello)
                annoImmatricolazione = None
                annoImmatricolazioneSistri = veicoloSistri.annoImmatricolazione
                if annoImmatricolazioneSistri:
                    annoImmatricolazione = annoImmatricolazioneSistri.long
                veicolo = Veicolo(
                    targa=veicoloSistri.targa.__repr__(),
                    marca=veicoloSistri.marca.__repr__(),
                    modello=veicoloSistri.modello.__repr__(),
                    annoImmatricolazione=annoImmatricolazione,
#                    sede=sede,
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
