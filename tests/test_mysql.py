# -*- coding: UTF-8 -*-
import os
import sys
from collections import namedtuple
# from pytest_mysql import factories
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dbconnection.connectionfactory import ConnectionFactory

# mysql_my_proc = factories.mysql_proc(port=None, logsdir='/tmp')


def test_mysql_connection():
    return
    Auth = namedtuple("Auth", "username, password")
    Parameters = namedtuple('Parameters', "auth, host, database")

    auth = Auth(
        username="circleci",
        password="<password>")
    parameters = Parameters(
        auth=auth, host="localhost",
        database="database")

    db = ConnectionFactory(
        engine="mysql",
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
