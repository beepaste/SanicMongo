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

from motor.frameworks import asyncio as asyncio_framework
from motor.metaprogramming import create_class_with_framework
from asymongo.core import (asymongoAgnosticClient)


asymongoAsyncIOClient = create_class_with_framework(asymongoAgnosticClient,
                                                      asyncio_framework,
                                                      'asymongo.clients')
