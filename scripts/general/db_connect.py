import psycopg2
from psycopg2 import pool


def get_db_pool():
    db_pool = psycopg2.pool.ThreadedConnectionPool(
        1, 10,
        user='',
        password='',
        host='',
        port='',
        database=''
    )
    return db_pool