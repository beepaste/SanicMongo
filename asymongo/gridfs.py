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

from motor.metaprogramming import create_class_with_framework
from motor.motor_gridfs import AgnosticGridFS
from asymongo.core import asymongoAgnosticDatabase
from asymongo.metaprogramming import OriginalDelegate


class asymongoAgnosticGridFS(AgnosticGridFS):

    __motor_class_name__ = 'asymongoGridFS'

    delete = OriginalDelegate()
    get = OriginalDelegate()
    new_file = OriginalDelegate()
    put = OriginalDelegate()

    def __init__(self, database, collection="fs"):
        """An instance of GridFS on top of a single Database.

        :Parameters:
          - `database`: a :class:`~asymongo.asymongoDatabase`
          - `collection` (optional): A string, name of root collection to use,
            such as "fs" or "my_files"

        .. mongodoc:: gridfs

        """

        db_class = create_class_with_framework(
            asymongoAgnosticDatabase, database._framework, self.__module__)

        if not isinstance(database, db_class):
            raise TypeError("First argument to asymongoGridFS must be "
                            "asymongoDatabase, not %r" % database)

        self.io_loop = database.get_io_loop()
        self.collection = database[collection]
        self.delegate = self.__delegate_class__(
            database.delegate,
            collection)

        self._GridFS__collection = self.delegate._GridFS__collection
        self._GridFS__files = self.delegate._GridFS__files
        self._GridFS__chunks = self.delegate._GridFS__chunks
