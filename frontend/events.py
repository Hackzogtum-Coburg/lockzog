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

import abc


class EventHandler(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, event_message):
        pass

    @abc.abstractmethod
    def isPre(self):
        pass

    @abc.abstractmethod
    def isPost(self):
        pass


class EventType():
    OPEN  = 1
    CLOSE = 2


class EventMessage():
    def __init__(self, event_type, certificate):
        self.event_type = event_type
        self.certificate = certificate


class EventManager():
    def __init__(self):
        self.pre_handlers  = []
        self.post_handlers = []

    def add_handler(self, handler):
        if handler.isPre():
            self.pre_handlers.append(handler)
        elif handler.isPost():
            self.post_handlers.append(handler)

    def dispatchPreHandlers(self, event_msg):
        for next in self.pre_handlers:
            result = next.handle(event_msg)
            if (result == False):
                return False
        return True

    def dispatchPostHandlers(self, event_msg):
        for next in self.post_handlers:
            result = next.handle(event_msg)
            if (result == False):
                return False
        return True
