# -*- coding: UTF-8 -*-
import os
import sys
from collections import namedtuple
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dbconnection.connectionfactory import ConnectionFactory


def test_sqlite_connection():

    Parameters = namedtuple('Parameters', "database")
    parameters = Parameters(database=":memory:")

    db = ConnectionFactory(
        engine="sqlite",
        connectionParameters=parameters)

    SQL = '''CREATE TABLE DATAGERMANY
            (id_db INTEGER PRIMARY KEY AUTOINCREMENT,
            id_photo INTEGER NOT NULL,
            title TEXT,
            tags TEXT,
            latitude NUMERIC NOT NULL,
            longitude NUMERIC NOT NULL)'''
    db.change(SQL)

    SQL = '''INSERT INTO DATAGERMANY
            (id_photo, title, tags, latitude, longitude)
            VALUES(20, 'fred', 'freddy, fox', 56.34532, 0.28636),
            (20, 'Dilbert', 'Dilbert, Cartoon', 54.34532, 1.28636)'''
    db.change(SQL)

    SQL = "SELECT * FROM DATAGERMANY"

    selection = db.select(SQL)
    assert selection[0] == (1, 20, 'fred', 'freddy, fox', 56.34532, 0.28636)
