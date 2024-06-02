import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(dir_path, "../../data/database.csv")


class DB:
    def __init__(self, db_path: str=database_path):
        self.db_path = db_path

    def find(self, filtering: dict):
        # May use pandas for larger csv dataset. Use built-in csv reader for this task for simplicity
        with open(self.db_path, newline="") as csvfile:
            result = csv.DictReader(csvfile)
            for key, value in filtering.items():
                result = [row for row in result if row[key] == value]

            return result
