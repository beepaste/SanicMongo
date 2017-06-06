# -*- coding: utf-8 -*-

# Copyright 2016 Juca Crispim <juca@poraodojuca.net>

# This file is part of asymongo.

# asymongo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# asymongo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with asymongo. If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase
from mongoengine.connection import _connection_settings
from asymongo import connect, disconnect
from asymongo.connection import (asymongoAsyncIOClient)


class ConnectionTest(TestCase):

    def tearDown(self):
        disconnect()

    def test_connect_with_asyncio(self):
        conn = connect()
        self.assertTrue(isinstance(conn, asymongoAsyncIOClient))

    def test_registered_connections(self):
        # ensures that a sync connection was registered
        connect()
        self.assertEqual(len(_connection_settings), 2,
                         _connection_settings.keys())
