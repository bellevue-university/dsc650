from dsc650.assignments.assignment02.util import RESULTS_DIR
from pathlib import Path

kvdb_dir = RESULTS_DIR.joinpath('kvdb')
# Create the db_dir if it doesn't exist
kvdb_dir .mkdir(parents=True, exist_ok=True)
sites_kvdb = kvdb_dir .joinpath('sites.pickle')
measurements_kvdb = kvdb_dir .joinpath('measurements.pickle')
people_kvdb = kvdb_dir .joinpath('people.pickle')
visits_kvdb = kvdb_dir .joinpath('visits.pickle')


class KVDB(object):
    def __init__(self, db_path):
        self._db_path = Path(db_path)
        self._db = {}
        self._load_db()

    def _load_db(self):
        pass

    def get_value(self, key):
        pass

    def set_value(self, key, value):
        pass

    def save(self):
        pass


def create_sites_kvdb():
    pass


def create_people_kvdb():
    pass


def create_visits_kvdb():
    pass


def create_measurements_kvdb():
    pass


def main():
    create_sites_kvdb()
    create_people_kvdb()
    create_visits_kvdb()
    create_measurements_kvdb()