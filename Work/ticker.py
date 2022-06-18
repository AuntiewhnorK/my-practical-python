"""
Practical Python 6.10 - Piplines

Author: Auntiewhnor Kpolie
Created: 6/17/2022

Reads in portfolio csv file and outputs rows
"""

from follow import follow
import csv


def select_columns(rows, indices):
    """
    select columns from stocklog.csv
    """
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    """
    output list of converted values
    """
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    """
    make dictionary of headers and rows
    ex: {header 1: row_1 value}
    """
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    """
    Filter rows based on user argument
    """
    for row in rows:
        if row['name'] in names:
            yield row


def parse_stock_data(lines):
    row = csv.reader(lines)
    rows = select_columns(row, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


if __name__ == '__main__':
    # filter stocks in Data/portfolio.csv

    import report2
    portfolio = report2.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
