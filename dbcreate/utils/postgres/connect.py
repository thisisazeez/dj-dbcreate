# """Code for connecting to postgres"""

import psycopg2
from dbcreate.utils.checkpsql import check_postgres_installed

def connect_to_postgres(user='postgres', password='password', host='localhost', port='5432'):
    if not check_postgres_installed():
        print("PostgreSQL is not installed on your system.")
        return None

    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

if __name__ == "__main__":
    # Replace 'your_password' with the actual password
    connection = connect_to_postgres('postgres', 'password')
    if connection:
        print("Connected to PostgreSQL with the default 'postgres' user.")
