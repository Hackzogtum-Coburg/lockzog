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

from datetime import datetime
from django.db import models


class Operation(models.Model):

    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    action = models.CharField(max_length=5)
    time = models.DateTimeField(default=datetime.now(), primary_key=True)

    def __str__(self):
        return self.time.__str__() + " > " + self.name + " performed action " + self.action
