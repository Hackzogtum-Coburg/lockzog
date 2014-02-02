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
    def handle(self, eventMessage):
        pass

    @abc.abstractmethod
    def isPre(self):
        pass

    @abc.abstractmethod
    def isPost(self):
        pass


class EventType():
    OPEN = 1
    CLOSE = 2


class EventMessage():
    def __init__(self, eventType, certificate):
        self.eventType = eventType
        self.certificate = certificate


class EventManager():
    def __init__(self):
        # TODO: implement
        pass

    def dispatchPreHandlers(self):
        # TODO: implement
        pass
        return True

    def dispatchPostHandlers(self):
        # TODO: implement
        pass
        return True


manager = EventManager()
