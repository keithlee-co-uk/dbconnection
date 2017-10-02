# -*- coding: UTF-8 -*-

from collections import namedtuple
import typing


###############################################################################
class Connection(object):
    """
    # Function Calls
     select(sql, params=None) - Selects from the database
                                Returns a list of namedtuple Rows

     change(sql, params=None) - Commits changes to the database

    # Expects
     a namedtuple containing
     - database a string containing the database name

    """

    # -------------------------------------------------------------------------
    def __init__(self, parameters):
        """
        """
        self.database = parameters.database
        self.connection = None

    # -------------------------------------------------------------------------
    def change(self, sql, params=None):
        self._action(sql, params)
        self.connection.commit()

    # -------------------------------------------------------------------------
    def _dicts_to_namedtuples(self, selects) -> tuple:
        selectionList = []

        for select in selects:
            selectionList.append(namedtuple('Row', select.keys())(**select))

        return tuple(selectionList)

    # -------------------------------------------------------------------------
    def _cursor(self):
        try:
            cursor = self.connection.cursor()
        except:
            self._connect()
            cursor = self.connection.cursor()
        return cursor

    # -------------------------------------------------------------------------
    def _action(self, sql: str, params):
        cursor = self._cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        return cursor

    # -------------------------------------------------------------------------
    def _namedtuple_factory(self, cursor, row) -> typing.NamedTuple:
        fields = [field[0] for field in cursor.description]
        Row = namedtuple("Row", fields)
        return Row(*row)

    # -------------------------------------------------------------------------
    def __str__(self):

        return '{}(host={}, database={})'.format(self.__class__.__name__,
                                                 self.host,
                                                 self.database)