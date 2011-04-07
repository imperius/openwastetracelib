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

class GettingAziendaRequest(OWTBaseService,codiceFiscaleAzienda):
    """
    This class allows you to get an Azienda object.
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
        # Holds version info for the VersionId SOAP object.
        self._version_info = {'service_id': 'trck', 'major': '4',
                             'intermediate': '0', 'minor': '0'}
        self.TrackPackageIdentifier = None
        """@ivar: Holds the TrackPackageIdentifier WSDL object."""
        # Call the parent FedexBaseService class for basic setup work.
        super(FedexTrackRequest, self).__init__(self._config_obj,
                                                'TrackService_v4.wsdl',
                                                *args, **kwargs)

    def _prepare_wsdl_objects(self):
        """
        This sets the package identifier information. This may be a tracking
        number or a few different things as per the Fedex spec.
        """
        self.TrackPackageIdentifier = self.client.factory.create('TrackPackageIdentifier')
        # Default to tracking number.
        self.TrackPackageIdentifier.Type = 'TRACKING_NUMBER_OR_DOORTAG'

    def _check_response_for_request_errors(self):
        """
        Checks the response to see if there were any errors specific to
        this WSDL.
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
        Fires off the Fedex request.
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(), WHICH RESIDES
            ON FedexBaseService AND IS INHERITED.
        """
        client = self.client
        # Fire off the query.
        response = client.service.track(WebAuthenticationDetail=self.WebAuthenticationDetail,
                                        ClientDetail=self.ClientDetail,
                                        TransactionDetail=self.TransactionDetail,
                                        Version=self.VersionId,
                                        PackageIdentifier=self.TrackPackageIdentifier)

        return response
