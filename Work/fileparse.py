"""
Practical Python - 3.3 Making general purpose functions

Auntiewhnor Kpolie
Created: 05/06/2022
Last Edited: 05/07/2022

"""
import csv


def parse_csv(
    lines, select=None, types=None, has_headers=True, delimit=",", silence_errors=False
):
    """
    Parse CSV file into a list of records.
    """
    # expects any type of iterable
    rows = csv.reader(lines, delimiter=delimit)

    # Raise error if select and has_headers=False is passed

    if select and not has_headers:
        raise RuntimeError("select argument needs column headers")

    if has_headers:
        headers = next(rows)
    else:
        headers = []

    # if select columns are chosen, find those indices
    if select:
        indices = [headers.index(column) for column in select]
        headers = select
    else:
        indices = []

    records = []
    for rownum, row in enumerate(rows, start=1):
        if not row:  # Skip rows with no data
            continue
        # filter row on selected columns
        if indices:
            row = [row[index] for index in indices]
        # preform type conversion (ex: int('100') -> 100)
        try:
            if types:
                row = [func(val) for func, val in zip(types, row)]
        except ValueError as v:
            if silence_errors:
                continue
            else:
                print(f"Row {rownum}: Couldn't parse {row}")
                print(f"Reason: {v}")
                continue

        if has_headers and headers != "":
            # create dictionary record
            record = dict(zip(headers, row))
            records.append(record)
        else:
            record = tuple(row)
            records.append(record)

    return records
