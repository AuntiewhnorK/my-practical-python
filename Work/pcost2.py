"""
Practical Python 1.27 - Reading files

Auntiewhnor Kpolie
Created: 04/28/2022
Last Edited: 05/07/2022

Open the file `portfolio.csv` in the Data folder,
reads all the lines, and calculates the total
cost to purchase all the shares in the portfolio.

Exercise 1.30 - make pcost.py a function
"""
import csv
import sys
from report2 import read_portfolio


def portfolio_cost(filename):
    """
    Computes total cost of portfolio file
    """
    portfolio = read_portfolio(filename)
    # add up every price in the list
    return sum([s['shares'] * s['price'] for s in portfolio])


# command line usage:
# ex: python pcost.py Data/portfolio.csv
if len(sys.argv) == 2:
    # sys.argv[0] is the name of the script (pcost.py)
    file = sys.argv[1]  # filename to be passed
else:
    file = "Data/portfolio.csv"

cost = portfolio_cost(file)
print(f"Total cost {cost}")
