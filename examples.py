# /usr/bin/env python
# -*- coding: UTF-8 -*-

import typing
from collections import namedtuple

from dbconnection.connectionfactory import ConnectionFactory

# ----------------------------------------------------------------------
def main():
    #sql_server_example()
    #mysql_example()
    sqlite_example()

# ----------------------------------------------------------------------
def sql_server_example():
    Auth = namedtuple("Auth", "username, password")
    auth = Auth(username="<username>", password="<password>")


    Parameters = namedtuple('Parameters', "auth, host, database")
    parameters = Parameters(auth=auth,
                            host="<hostIP or DNSName>",
                            database="database")

    db = ConnectionFactory(engine="sqlserver",
                           connectionParameters=parameters)

    SQL = "SELECT * FROM AccountDirectDebitInstructions"
    selection = db.select(SQL)
    for i in selection:
        print(i)
        #break
    print(i)

# ----------------------------------------------------------------------
def mysql_example():
    Auth = namedtuple("Auth", "username, password")
    Parameters = namedtuple('Parameters', "auth, host, database")

    auth = Auth(
        username="<username>",
        password="<password>")
    parameters = Parameters(
        auth=auth, host="<hostIP or DNSName>",
        database="database")

    db = ConnectionFactory(
        engine="mysql",
        connectionParameters=parameters)

    SQL = "SELECT * FROM accounts WHERE email='klee@peoplevalue.co.uk'"
    selection = db.select(SQL)

    for i in selection:
        print("Hello")
        print(type(i))
        if isinstance(i, typing.NamedTuple):
            print("Is namedtuple")
        print(i)
        #break
    print(i)
    print("Goodbye")


# ----------------------------------------------------------------------
def sqlite_example():

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
    for i in selection:
        print("Hello")
        print(type(i))
        if isinstance(i, typing.NamedTuple):
            print("Is namedtuple")
        print(i)
        #break
    print(i)
    print("Goodbye")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
