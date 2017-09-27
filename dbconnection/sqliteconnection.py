# -*- coding: UTF-8 -*-

import sqlite3
from collections import namedtuple
from dbconnection.connection import Connection


###############################################################################
class SQLiteConnection(Connection):
    """
    A wrapper around sqlite3
    Provides common but very limited methods.
    This is for consistent, de-coupled calling across database types.

    # Function Calls
     select(sql, params=None) - Selects from the database
                                Returns a list of namedtuple Rows

     change(sql, params=None) - Commits changes to the database

    # Expects
     a namedtuple containing
     - database a string containing the path to the database

    """

    # -------------------------------------------------------------------------
    def __init__(self, parameters):
        """
        """
        super(SQLiteConnection, self).__init__(parameters)
        self.database = parameters.database

    # -------------------------------------------------------------------------
    def select(self, sql, params=None) -> tuple:
        self.connection.row_factory = self._namedtuple_factory
        cursor = self._action(sql, params)
        selects = cursor.fetchall()
        return selects

    # -------------------------------------------------------------------------
    def change(self, sql, params=None):
        cursor = self._cursor()
        self._action(sql, params)
        self.connection.commit()

    # -------------------------------------------------------------------------
    def _connect(self):
        if self.connection:
            if self.connection.connected:
                print("Already connected")
                return

        print("New connection")
        self.connection = sqlite3.connect(self.database)
