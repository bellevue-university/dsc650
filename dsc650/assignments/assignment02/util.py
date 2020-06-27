import pandas as pd
from dsc650.settings import TIDYNOMICON_DIR
from pathlib import Path

ASSIGNMENT_DIR = Path(__file__)
RESULTS_DIR = ASSIGNMENT_DIR.joinpath('results')


def read_person_csv():
    csv_path = TIDYNOMICON_DIR.joinpath('person.csv')
    df = pd.read_csv(csv_path)
    return df


def read_measurements_csv():
    csv_path = TIDYNOMICON_DIR.joinpath('measurements.csv')
    df = pd.read_csv(csv_path)
    return df


def read_site_csv():
    csv_path = TIDYNOMICON_DIR.joinpath('site.csv')
    df = pd.read_csv(csv_path)
    return df


def read_visited_csv():
    csv_path = TIDYNOMICON_DIR.joinpath('visited.csv')
    df = pd.read_csv(csv_path)
    return df
