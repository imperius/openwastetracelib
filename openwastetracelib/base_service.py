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
The L{base_service} module contains classes that form the low level foundations
of the Web Service API. Things that many different kinds of requests have in
common may be found here.
In particular, the L{OWTBaseService} class handles most of the basic,
repetetive setup work that most requests do.
"""

import os
import logging
import suds
from suds.client import Client
from https_cert import HttpAuthUsingCert

class OWTBaseServiceException(Exception):
    """
    Exception: Serves as the base exception that other service-related 
    exception objects are sub-classed from.
    """
    def __init__(self, error_code, value):
        self.error_code = error_code
        self.value = value
    def __unicode__(self):
        return "%s (Error code: %s)" % (repr(self.value), self.error_code)
    def __str__(self):
        return self.__unicode__()

class OWTFailure(OWTBaseServiceException):
    """
    Exception: The request could not be handled at this time. This is generally 
    a server problem.
    """
    pass

class OWTError(OWTBaseServiceException):
    """
    Exception: These are generally problems with the client-provided data.
    """
    pass

class SchemaValidationError(OWTBaseServiceException):
    """
    Exception: There is probably a problem in the data you provided.
    """
    def __init__(self):
        self.error_code = -1
        self.value = "suds encountered an error validating your data against this service's WSDL schema. Please double-check for missing or invalid values, filling all required fields."

class OWTBaseService(object):
    """
    This class is the master class for all SISTRI request objects. It gets all
    of the common SOAP objects created via suds and populates them with
    values from a L{OWTConfig} object, along with keyword arguments
    via L{__init__}.
    @note: This object should never be used directly, use one of the included
        sub-classes.
    """
    def __init__(self, config_obj, *args, **kwargs):
        """
        This constructor should only be called by children of the class.
        As is such, only the optional keyword arguments caught by C{**kwargs}
        will be documented.
        @type customer_transaction_id: L{str}
        @keyword customer_transaction_id: A user-specified identifier to
            differentiate this transaction from others. This value will be
            returned with the response from SISTRI.
        """
        self.logger = logging.getLogger('owt')
        """@ivar: Python logger instance with name 'owt'."""
        self.config_obj = config_obj
        """@ivar: The OWTConfig object to pull auth info from."""
        self.transport = HttpAuthUsingCert(self.config_obj.certificate,
                                            self.config_obj.privatekey)
        self.client = Client(self.config_obj.wsdl, transport=self.transport)
        self.response = None
        """@ivar: The response from SISTRI. You will want to pick what you
            want out here here. This object does have a __str__() method,
            you'll want to print or log it to see what possible values
            you can pull."""

    def __check_response_for_sistri_error(self):
        """
        This checks the response for general Sistri errors.
        """
        if self.response.HighestSeverity == "FAILURE":
            for notification in self.response.Notifications:
                if notification.Severity == "FAILURE":
                    raise OWTFailure(notification.Code,notification.Message)

    def _check_response_for_request_errors(self):
        """
        Override this in each service module to check for errors that are
        specific to that module.
        """
        if self.response.HighestSeverity == "ERROR":
            for notification in self.response.Notifications:
                if notification.Severity == "ERROR":
                    raise OWTError(notification.Code,
                                     notification.Message)

    def create_wsdl_object_of_type(self, type_name):
        """
        Creates and returns a WSDL object of the specified type.
        """
        return self.client.factory.create(type_name)

    def send_request(self, send_function=None):
        """
        Sends the assembled request on the child object.
        @type send_function: function reference
        @keyword send_function: A function reference (passed without the
            parenthesis) to a function that will send the request. This
            allows for overriding the default function in cases such as
            validation requests.
        """
        # Send the request and get the response back.
        try:
            # If the user has overridden the send function, use theirs
            # instead of the default.
            if send_function:
                # Follow the overridden function.
                self.response = send_function()
            else:
                # Default scenario, business as usual.
                self.response = self._assemble_and_send_request()
        except suds.WebFault:
            # When this happens, throw an informative message reminding the
            # user to check all required variables, making sure they are
            # populated and valid.
            raise SchemaValidationError()
        # Check the response for general Sistri errors/failures that aren't
        # specific to any given WSDL/request.
        self.__check_response_for_sistri_error()
        # Check the response for errors specific to the particular request.
        # This is handled by an overridden method on the child object.
        self._check_response_for_request_errors()
        # Debug output.
        self.logger.debug("== SISTRI QUERY RESULT ==")
        self.logger.debug(self.response)
