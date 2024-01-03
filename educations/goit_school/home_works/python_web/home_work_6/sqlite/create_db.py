import sqlite3


def create_db():
    with open('students_sqlite.sql', 'r') as fh:
        sql = fh.read()

    with sqlite3.connect('students_sqlite.db') as connection:
        cursor = connection.cursor()
        cursor.executescript(sql)


if __name__ == "__main__":
    create_db()
    print('Created database!')
