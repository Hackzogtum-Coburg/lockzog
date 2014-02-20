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

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from frontend.certificate import CertificateWrapper


def index(request):
    try:
        client_cert_pem = request.environ['SSL_CLIENT_CERT']
        client_cert = CertificateWrapper(client_cert_pem)
        # no error here means the certificate is ok
        return HttpResponseRedirect("control-panel")
    except KeyError:
        context = {}
        return render(request, 'welcome.html', context)

def controlPanel(request):
    context = {}
    return render(request, 'control-panel.html', context)
