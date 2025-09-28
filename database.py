"""
TODO: Docstring
"""
from datetime import date
from os import getenv
from psycopg import connect
from dotenv import load_dotenv


load_dotenv()
DATABASE = getenv("PSQL_DATABASE")
USER = getenv("PSQL_USER")


def sql_execute(query: str, parameters: tuple = None):
    """
    TODO: Docstring
    """
    with connect(f"dbname={DATABASE} user={USER}") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, parameters)


def create_studytime():
    """
    Creates a studytime table if it does not exist yet.
    Requires a PostgreSQL database 'studytime'.
    """
    sql_execute(
        """
        CREATE TABLE IF NOT EXISTS studytime (
        id serial PRIMARY KEY,
        name TEXT,
        required_time NUMERIC,
        studied_time NUMERIC,
        deadline DATE)
        """
    )


def create_module(name: str, required_time: float, deadline: date):
    """
    TODO: Docstring
    """
    sql_execute(
        f"""
        INSERT INTO studytime (
        name, required_time, deadline
        ) VALUES ({name}, {required_time}, {deadline}))
        """
    )


def create_modules():
    """
    Creates the modules for semester 4.
    """

create_studytime()
