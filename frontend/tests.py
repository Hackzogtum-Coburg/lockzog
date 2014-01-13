# lockzog - door managment service
# Copyright (C) 2014  Tobias Wich
# Contact: tobias.wich@electrologic.org
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

from django.test import TestCase
from frontend.certificate import CertificateWrapper


testCert = """-----BEGIN CERTIFICATE-----
MIICXDCCAhygAwIBAgIBATAJBgcqhkjOPQQBMIGLMQswCQYDVQQGEwJERTEPMA0G
A1UECBMGQmF5ZXJuMQ8wDQYDVQQHEwZDb2J1cmcxHzAdBgNVBAoTFkhhY2t6b2d0
dW0gQ29idXJnIGUuVi4xGzAZBgNVBAMMElRlc3QgVXNlciBGaWFsb3bDoDEcMBoG
CSqGSIb3DQEJARYNdGVzdEB0ZXN0LmNvbTAeFw0xNDAxMTIxNTE3MDBaFw0xODAx
MTIxNTE3MDBaMIGLMQswCQYDVQQGEwJERTEPMA0GA1UECBMGQmF5ZXJuMQ8wDQYD
VQQHEwZDb2J1cmcxHzAdBgNVBAoTFkhhY2t6b2d0dW0gQ29idXJnIGUuVi4xGzAZ
BgNVBAMMElRlc3QgVXNlciBGaWFsb3bDoDEcMBoGCSqGSIb3DQEJARYNdGVzdEB0
ZXN0LmNvbTBDMBMGByqGSM49AgEGCCqGSM49AwABAywABABI9ZObisqR/7riMwBg
kfFZAP9nAgbYIHbo5CYo0IIx3da6fGR52p/5QKOBhTCBgjAMBgNVHRMBAf8EAjAA
MB0GA1UdDgQWBBTs65LV3Prs0d1ofOdBgQ83X063SjALBgNVHQ8EBAMCBLAwEwYD
VR0lBAwwCgYIKwYBBQUHAwEwEQYJYIZIAYb4QgEBBAQDAgWgMB4GCWCGSAGG+EIB
DQQRFg94Y2EgY2VydGlmaWNhdGUwCQYHKoZIzj0EAQMvADAsAhRYQQTJghRJD8g5
U56f/p228E9h3QIUNRcvZZcaAiqpyktKRqb8Lm82a6g=
-----END CERTIFICATE-----
"""


class CertificateTest(TestCase):
    def instance(self):
        return CertificateWrapper(testCert)

    def test_load_certificate(self):
        certWrapper = self.instance()
        print(certWrapper.subject())

    def test_name(self):
        self.assertEqual("Test User Fialovà", self.instance().subject_name())

    def test_email(self):
        self.assertEqual("test@test.com", self.instance().subject_email())
