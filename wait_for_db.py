import os
import psycopg2
from time import sleep


def wait_for_db():
    db_url = os.getenv('DATABASE_URL')
    while True:
        try:
            conn = psycopg2.connect(db_url)
            conn.close()
            break
        except psycopg2.OperationalError:
            print('Waiting for database to be ready...')
            sleep(5)


if __name__ == '__main__':
    wait_for_db()
