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

from OpenSSL.crypto import *


class CertificateWrapper():
    def __init__(self, pem_encoded_cert):
        try:
            self.pem_encoded_cert = pem_encoded_cert
            self.cert = load_certificate(FILETYPE_PEM, pem_encoded_cert)
        except Error:
            raise KeyError

    def subject(self):
        tuples = X509.get_subject(self.cert).get_components()
        return dict(tuples)

    def issuer(self):
        tuples = X509.get_issuer(self.cert).get_components()
        return dict(tuples)


    def subject_name(self):
        return self.subject()[b'CN'].decode('utf8')

    def subject_email(self):
        return self.subject()[b'emailAddress'].decode('utf8')
