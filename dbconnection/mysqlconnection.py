# -*- coding: UTF-8 -*-

try:
    from mysql.connector import connect, cursor, errors
except ModuleNotFoundError:
    print("mysql.connector is not installed.")
from dbconnection.connection import Connection


###############################################################################
class MySQLConnection(Connection):
    """
    A wrapper around mysql.connector
    Provides common but very limited methods.
    This is for consistent, de-coupled calling across database types.

    Expects a named tuple containing
     - auth a namedtuple with
        - username - a string
        - password - string

     - host - a string containing the hostname or IPv4 address

     - database - a string containing the database name/scheme

    Optionally
     - port - an integer of the TCP/IP port that the host is listening on for
              database connections

    """

    # -------------------------------------------------------------------------
    def __init__(self, parameters):
        super(MySQLConnection, self).__init__(parameters)
        self.username = parameters.auth.username
        self.password = parameters.auth.password
        self.host = parameters.host
        try:
            self.port = parameters.port
        except AttributeError:
            self.port = 3306

    # -------------------------------------------------------------------------
    def select(self, sql, params=None) -> tuple:
        return tuple(self._action(sql, params))

    # -------------------------------------------------------------------------
    def _cursor(self):
        try:
            cursor = self.connection.cursor(named_tuple=True)
        except:
            self._connect()
            cursor = self.connection.cursor(named_tuple=True)
        return cursor

    # -------------------------------------------------------------------------
    def _connect(self):
        if self.connection:
            if self.connection.is_connected:
                return

        self.connection = connect(host=self.host,
                                  user=self.username,
                                  connect_timeout=30,
                                  passwd=self.password,
                                  db=self.database,
                                  port=self.port)
