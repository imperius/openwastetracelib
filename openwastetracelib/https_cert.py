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
HTTPS Transport for suds SOAP client using certificate and key files.
"""

import urllib2
import httplib
from suds.client import Client
from suds.options import Options
from suds.transport import *
from suds.transport.http import HttpTransport

class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    """HTTPS Client Auth solution for urllib2.
    Inspired by http://bugs.python.org/issue3466 and improved by David Norton
    of Three Pillar Software. In this implementation, we use properties passed
    in rather than static module fields.
    Found at: http://www.threepillarsoftware.com/soap_client_auth
    """
    def __init__(self, cert, key):
        urllib2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        """
        Rather than pass in a reference to a connection class, we pass in
        a reference to a function which, for all intents and purposes,
        will behave as a constructor
        """
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=9000):
        return httplib.HTTPSConnection(host,key_file=self.key,
                                        cert_file=self.cert)

class HttpAuthUsingCert(HttpTransport):
    """Provides http authentication using certificate and key.
    @ivar handler: The authentication handler.
    @ivar cert: Path to PEM certificate file.
    @ivar key: Path to PEM private key file.
    """
    def __init__(self, cert, key, options=Options()):
        """
        Removed the second variable for resolve issue.
        """
        #HttpTransport.__init__(self, options)
        HttpTransport.__init__(self)
        self.handler = HTTPSClientAuthHandler(cert, key)
        self.urlopener = urllib2.build_opener(self.handler)

    def open(self, request):
        return  HttpTransport.open(self, request)

    def send(self, request):
        return HttpTransport.send(self, request)
