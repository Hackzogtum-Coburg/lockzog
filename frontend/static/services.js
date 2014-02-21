/*****************************************************************************
 * lockzog - door managment service
 * Copyright (C) 2014  Tobias Wich
 * Contact: tobias.wich@electrologic.org
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 ****************************************************************************/


function send_open() {
    send_message("open");
}

function send_close() {
    send_message("close");
}

function handler() {
    var body = this.responseText;
    console.info(body);
    var status = document.getElementById("status");
    status.innerHTML = body;
    status.className = "info";
}

function send_message(action) {
    var req = new XMLHttpRequest();
    req.open("POST", "api/door");
    req.addEventListener("loadend", handler);
    var data = new FormData();
    data.append("action", action);
    req.send(data);
}
