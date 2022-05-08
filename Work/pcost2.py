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
    return sum([s.shares * s.price for s in portfolio])


# command line usage:
# ex: python pcost.py Data/portfolio.csv
def main(arguments):
    if len(arguments) != 2:
        raise SystemExit(f'Usage: {arguments[0]} ' 'portfolio_file')
    file = arguments[1]
    print(f"Total cost {portfolio_cost(file)}")


if __name__ == '__main__':
    import sys
    main(sys.argv)
