import psycopg2


def create_db():
    with open('students_postgresql.sql', 'r') as fh:
        sql = fh.read()

    with psycopg2.connect(database='some-postgres', user='postgres',
                          password='password', host='localhost', port='5432') as connection:
        cursor = connection.cursor()
        cursor.execute(sql)


if __name__ == "__main__":
    create_db()
    print('Created database!')
