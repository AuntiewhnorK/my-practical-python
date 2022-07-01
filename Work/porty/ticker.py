"""
Practical Python 6.10 - Piplines

Author: Auntiewhnor Kpolie
Created: 6/17/2022

Reads in portfolio csv file and outputs rows
"""
import report2
import tableformat
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


def parse_stock_data(lines):
    """
    Read in stock data
    """
    row = csv.reader(lines)
    rows = select_columns(row, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


'''
def filter_symbols(rows, names):
    """
    Filter rows based on user argument
    """
    for row in rows:
        if row["name"] in names:
            yield row
'''


def ticker(portfile, logfile, fmt):
    """
    Given portfolio and log file,
    output data based on given format
    """
    portfolio = report2.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)

    # generator expression - equal to filter_symbols func
    rows = (row for row in rows if row["name"] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row["name"], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(argument):
    if len(argument) != 4:
        raise SystemExit("Usage: %s portfoliofile logfile fmt" % argument[0])
    ticker(argument[1], argument[2], argument[3])


if __name__ == "__main__":

    import sys

    main(sys.argv)
