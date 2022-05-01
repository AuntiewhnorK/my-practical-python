"""
Practical Python 2.4 to 2.7 - Tuples and Dictionaries

Auntiewhnor Kpolie
04/23/2022

Based off of pcost.py, this file defines a
function that opens a given portfolio file
and puts in a list of tuples.
"""
import csv

portfolio = []  # Exercise 2.5


def read_portfolio(file):
    """Returns portfolio in a list of dictionaries"""

    with open(file, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)  # header: names, shares, price list
        for row in rows:
            # holding = (row[0], int(row[1]), float(row[2])) using tuple
            holding = {header[0]: row[0], header[1]: int(row[1]), header[2]: float(row[2])}
            portfolio.append(holding)

    return portfolio


prices = {}  # Exercise 2.6


def read_prices(file):
    """Opens a file and returns a dictionary
    where the keys and values are stock names
    and current stock price"""

    with open(file, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            # can also use if statement
            # to check for empty list
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('No data')

    return prices


# Exercise 2.7

def calculation(stock_portfolio, stock_price):
    total_value = 0.0
    value = {}
    for element in stock_portfolio:
        # value of portfolio: owned shares * current stock price, add up for total
        name = element['name']
        shares = element['shares']
        purchase_price = element['price']
        total_value += (shares * purchase_price)

        # calculate gain/loss for each stock
        current_price = stock_price[name]
        gain_loss = ((current_price - purchase_price) / purchase_price) * 100
        value[name] = gain_loss
    return total_value, value
