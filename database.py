"""
Direct connections with the PostgreSQL database.
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
    Executes a given command (update, delete, insert).
    """
    with connect(f"dbname={DATABASE} user={USER}") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, parameters)


def sql_fetchall(query: str, parameters: tuple = None):
    """
    Fetches all instances of a select query.
    """
    with connect(f"dbname={DATABASE} user={USER}") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, parameters)
            return cursor.fetchall()


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
        required_hours FLOAT,
        studied_hours FLOAT DEFAULT 0,
        deadline DATE)
        """
    )


def create_module(name: str, required_hours: float, deadline: date):
    """
    Creates a single module.
    """
    sql_execute(
        """
        INSERT INTO studytime (
        name, required_hours, deadline
        ) VALUES (%s, %s, %s)
        """, (name, required_hours, deadline)
    )


def create_modules():
    """
    Creates the modules for semester 4.
    """
    create_module("Grafische Datenverarbeitung", 112.50, date(2026, 2, 15))
    create_module("Kommunikationssysteme", 135.00, date(2026, 2, 15))
    create_module("Projektstudium", 303.75, date(2026, 2, 15))
    create_module("Softwaredesign", 135.00, date(2026, 2, 15))


def get_modules():
    """
    Gets the stats of every single module tracked.
    """
    return sql_fetchall("""SELECT * FROM studytime;""")