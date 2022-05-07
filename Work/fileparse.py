"""
Practical Python - 3.3 Making general purpose functions

Auntiewhnor Kpolie
Created: 05/06/2022
Last Edited:

"""
import csv

from numpy import indices
from requests import head


def parse_csv(filename, select=None):
    """
    Parse CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f)

        headers = next(rows)

        # if select columns are chosen, find those indices
        if select:
            indices = [headers.index(column) for column in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            # filter row on selected columns
            if indices:
                row = [row[index] for index in indices]

            # create dictionary record
            record = dict(zip(headers, row))
            records.append(record)

    return records
