from dsc650.settings import PROCESSED_DATA_DIR
from dsc650.assignments.assignment02.util import read_person_csv, read_site_csv, read_visited_csv, read_measurements_csv
import sqlite3

RESULTS_DIR = PROCESSED_DATA_DIR.joinpath('assignment02')


def create_people_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS people (
        person_id text PRIMARY KEY,
        personal_name text NOT NULL,
        family_name text NOT NULL
        );
    """

    c = conn.cursor()
    c.execute(sql)


def create_sites_table(conn):
    pass


def create_visits_table(conn):
    pass


def create_measurements_table(conn):
    pass


def load_people_table(conn):
    create_people_table(conn)
    df = read_person_csv()
    people = df.values
    c = conn.cursor()
    c.execute('DELETE FROM people;')
    c.executemany('INSERT INTO people VALUES (?,?,?)', people)


def load_visits_table(conn):
    pass


def load_sites_table(conn):
    pass


def load_measurements_table(conn):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
