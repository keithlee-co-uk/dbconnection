# -*- coding: UTF-8 -*-
import sys
try:
    import pymssql
except ModuleNotFoundError:
    print("pymssql is not installed.")
    sys.exit(status=1)
from dbconnection.connection import Connection
from collections import namedtuple


###############################################################################
class SQLServerConnection(Connection):
    """
    A wrapper around pymssql
    Provides common but very limited methods.
    This is for consistent, de-coupled calling across database types.

    Function Calls
    select - Selects from the database Returns a tuple of namedtuple Rows
    change - Executes and commits a change to the database

    Expects a named tuple containing
     - auth a namedtuple with
        - username - a string
        - password - string

     - host - a string containing the hostname or IPv4 address

     - database - a string containing the database name/scheme

    Optionally
     - port - an integer of the TCP/IP port that the host is listening on for
              database connections
              default 1433

    """

    # -------------------------------------------------------------------------
    def __init__(self, parameters):
        """
        """
        super(SQLServerConnection, self).__init__(parameters)
        self.username = parameters.auth.username
        self.password = parameters.auth.password
        self.host = parameters.host

        try:
            self.port = parameters.port
        except AttributeError:
            self.port = 1433

    # -------------------------------------------------------------------------
    def select(self, sql, params=None) -> tuple:
        cursor = self._action(sql, params)
        selects = cursor.fetchall()
        return self._dicts_to_namedtuples(selects)

    # -------------------------------------------------------------------------
    def _connect(self):
        """
        """
        if self.connection:
            if self.connection.connected:
                print("Already connected")
                return

        print("New connection")
        self.connection = pymssql.connect(host=self.host,
                                          user=self.username,
                                          login_timeout=30,
                                          password=self.password,
                                          database=self.database,
                                          as_dict=True,
                                          port=self.port)
