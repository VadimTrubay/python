from psycopg2 import Error

from db_connection import connection

create_table_users = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(40),
  email VARCHAR(40),
  password VARCHAR(30),
  age NUMERIC CHECK (age > 0 AND age < 150)
);
"""
if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_table_users)
        c.close()
