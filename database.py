"""
TODO: Docstring
"""
from psycopg_pool import ConnectionPool

def __init__(user: str, password: str, host: str, port: int, database: str):
    pool = ConnectionPool(
        f"host={host} port={port} dbname={database} user={user} password={password}",
        open=True, check=ConnectionPool.check_connection
    )
