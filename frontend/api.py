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

from django.http.response import HttpResponse
from frontend.certificate import CertificateWrapper
from frontend.events import EventMessage, EventType
from frontend.door import *
from frontend.events_impl import manager


def door(request):
    # PUT is the right verb, but quite problematic in pure django, so use post for now
    # Consider rewriting the code with http://django-tastypie.readthedocs.org/en/latest/
    # GET is there to make it possible to call the URL with NFC tags
    if request.method == "POST" or request.method == "GET":
        return prepare_action(request.POST.get('action', ''), request.environ)
    else:
        return HttpResponse("Wrong HTTP method!")


action_funs = {
    "open":  open_door,
    "close": close_door
}

action_type = {
    "open":  EventType.OPEN,
    "close": EventType.CLOSE
}


def prepare_action(action, environ):
    action_fun = None
    try:
        action_fun = action_funs[action]
    except KeyError:
        return HttpResponse("Unknown door action!")
    # convert certificate
    try:
        client_cert_pem = environ['SSL_CLIENT_CERT']
        client_cert = CertificateWrapper(client_cert_pem)
        return process_action(action, action_fun, client_cert)
    except KeyError:
        return HttpResponse("No certificate given!")


def process_action(action, action_fun, certificate):
    event_type = action_type[action]
    event_msg = EventMessage(event_type, certificate)
    # execute pre handlers
    if not manager.dispatchPreHandlers(event_msg):
        return HttpResponse("Not all preprocess logic handlers provided positive results!")
    # execute event
    if not action_fun() == 0:
        return HttpResponse("Execution of the action yielded an error.")
    # execute post handlers
    if not manager.dispatchPostHandlers(event_msg):
        return HttpResponse("Not all postprocess logic handlers provided positive results!")

    return HttpResponse("User " + certificate.subject_name() + " performed " + action + " with the door!")
