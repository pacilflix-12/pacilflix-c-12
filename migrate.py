from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from os import environ
from dotenv import load_dotenv

load_dotenv(override=True)

dbname = environ.get('PGDATABASE')
user = environ.get('PGUSER')
password = environ.get('PGPASSWORD')
host = environ.get('PGHOST')
port = environ.get('PGPORT', 5432)


def migrate():
    print('Migrating...')
    load_dotenv(override=True)

    connection = connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('CONNECTION SUCCESS!')

    cursor = connection.cursor()
    with open('migration.sql', 'r') as sql_file:
        sql_commands = sql_file.read()

    cursor.execute(sql_commands)
    print('SUCCESS MIGRATE!')

    cursor.close()
    connection.close()


def seeding():
    print('Seeding...')
    load_dotenv(override=True)

    connection = connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('CONNECTION SUCCESS!')

    cursor = connection.cursor()
    with open('dummy_data.sql', 'r') as sql_file:
        sql_commands = sql_file.read()

    cursor.execute(sql_commands)
    print('SUCCESS SEEDING!')

    cursor.close()
    connection.close()


def reset():
    print('Resetting DB...')
    load_dotenv(override=True)

    connection = connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('CONNECTION SUCCESS!')

    cursor = connection.cursor()
    cursor.execute('DROP SCHEMA public CASCADE')
    print('Success drop schema!')
    cursor.execute('CREATE SCHEMA public')
    print('Success create schema!')

    cursor.close()
    connection.close()

    migrate()
    seeding()


if __name__ == '__main__':
    reset()
