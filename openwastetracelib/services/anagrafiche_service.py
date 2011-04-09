"""
Cataloghi Service Module
========================
This package contains the cataloghi managment methods defined by Sistri.
For more details on each, refer to the respective class's documentation.
"""
import logging
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
    def __init__(self, config_obj, identity, codiceFiscaleAzienda, *args, **kwargs):
        """
        Sends an update cataloghi request. The optional keyword args
        detailed on L{OWTBaseService} apply here as well.
        @type config_obj: L{OWTConfig}
        @param config_obj: A valid OWTConfig object.
        """
        self._config_obj = config_obj
        self.identity = identity
        self.codiceFiscaleAzienda = codiceFiscaleAzienda
        # Call the parent OWTBaseService class for basic setup work.
        super(GettingAziendaRequest, self).__init__(self._config_obj,
                                                    *args, **kwargs)

    def _check_response_for_request_errors(self):
        """
        Checks the response to see if there were any errors.
        """
        if self.response.HighestSeverity == "ERROR":
            for notification in self.response.Notifications:
                if notification.Severity == "ERROR":
                    if "Invalid tracking number" in notification.Message:
                        raise FedexInvalidTrackingNumber(notification.Code,
                                                         notification.Message)
                    else:
                        raise FedexError(notification.Code,
                                         notification.Message)

    def _assemble_and_send_request(self):
        """
        Fires off the SISTRI request.
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(), WHICH RESIDES
            ON OWTBaseService AND IS INHERITED.
        """
        client = self.client
        # Fire off the query.
        response=client.service.GetAzienda(self.identity,
                                            "",
                                            self.codiceFiscaleAzienda)

        return response
