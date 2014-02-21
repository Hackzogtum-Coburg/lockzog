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

from frontend.events import EventHandler, EventType
from frontend.models import ActionLog

class ActionLogger(EventHandler):
    def handle(self, event_msg):
        event_type = event_msg.event_type
        if event_type == EventType.OPEN:
            action = "open"
        else:
            action = "close"
        cert = event_msg.certificate
        email = cert.subject_email()
        name = cert.subject_name()

        entry = ActionLog();
        entry.email = email
        entry.name = name
        entry.action = action
        entry.save()

    def isPre(self):
        return False

    def isPost(self):
        return True
