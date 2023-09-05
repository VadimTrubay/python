#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def old_old_variant():
    import sqlite3
    connect = sqlite3.connect(":memory:")

    try:
        print(connect.execute('SELECT sqlite_version();').fetchone())

        connect.executescript('''\
        CREATE TABLE Test (
            id INTEGER PRIMARY KEY,
            name TEXT
        );

        INSERT INTO Test (name) VALUES ('One');
        INSERT INTO Test (name) VALUES ('Two');
        INSERT INTO Test (name) VALUES ('Three');
        ''')

        print(connect.execute('select * from Test;').fetchall())
        print()

        connect.commit()

    finally:
        connect.close()


def old_variant():
    import sqlite3

    with sqlite3.connect(":memory:") as connect:
        print(connect.execute('SELECT sqlite_version();').fetchone())

        connect.executescript('''\
        CREATE TABLE Test (
            id INTEGER PRIMARY KEY, 
            name TEXT
        );

        INSERT INTO Test (name) VALUES ('One');
        INSERT INTO Test (name) VALUES ('Two');
        INSERT INTO Test (name) VALUES ('Three');
        ''')

        print(connect.execute('select * from Test;').fetchall())
        print()

        connect.commit()


class SQLite3Connect(object):
    def __init__(self, database):
        import sqlite3
        self._connect = sqlite3.connect(database)

    def __enter__(self):
        return self._connect

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._connect.close()


def new_variant():
    with SQLite3Connect(":memory:") as connect:
        print(connect.execute('SELECT sqlite_version();').fetchone())

        connect.executescript('''\
        CREATE TABLE Test (
            id INTEGER PRIMARY KEY, 
            name TEXT
        );

        INSERT INTO Test (name) VALUES ('One');
        INSERT INTO Test (name) VALUES ('Two');
        INSERT INTO Test (name) VALUES ('Three');
        ''')

        print(connect.execute('select * from Test;').fetchall())
        print()

        connect.commit()


if __name__ == '__main__':
    old_old_variant()
    old_variant()
    new_variant()
