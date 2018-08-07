# -*- coding: UTF-8 -*-

# from dbconnection.sqlserverconnection import SQLServerConnection pymssql keeps breaking a circleci attempts, removed for now
from dbconnection.mysqlconnection import MySQLConnection
from dbconnection.sqliteconnection import SQLiteConnection


###############################################################################
class ConnectionSupportError(AttributeError):
    pass


###############################################################################
class ConnectionFactory(object):
    """
    Base class describing the expected interface for a database connection
    """
    engineType = {'sqlserver': SQLServerConnection,
                  'mysql': MySQLConnection,
                  'sqlite': SQLiteConnection}

    # -------------------------------------------------------------------------
    def __new__(klass, engine=None, connectionParameters=None):
        """
        Expects
          engine - a String that names the database engine expected
          connectionParameters - a namedtuple containing the relevant
                                 connection parameters for the database engine

        """
        try:
            return ConnectionFactory.engineType[engine](connectionParameters)
        except KeyError as e:
            msg = "The '{}' engine is not currently supported".format(engine)
            raise ConnectionSupportError(msg)
