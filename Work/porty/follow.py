"""
Practical Python - Generators

Author: Auntiewhnor Kpolie
Created: 06/16/2022

stocklog.csv is a continuous stream of data
which comes from running stocksim.py
in the Data folder.

This program reads stocklog.csv and
prints out stocks with change less than 0.

Shows information for stocks in 'Data/portfolio.csv'
"""
import os
import time


def follow(file):
    f = open(file)
    f.seek(0, os.SEEK_END)  # move pointer to the end of file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)  # stop for 0.1 seconds, then try again
            continue
        yield line


if __name__ == '__main__':
    import report2

    # information for stocks only in this csv
    portfolio = report2.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
