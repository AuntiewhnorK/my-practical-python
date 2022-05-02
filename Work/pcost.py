"""
Practical Python 1.27 - Reading files

Auntiewhnor Kpolie
04/28/2022

Open the file `portfolio.csv` in the Data folder,
reads all the lines, and calculates the total
cost to purchase all the shares in the portfolio.

Exercise 1.30 - make pcost.py a function
"""
import csv
import sys


def portfolio_cost(filename):
    """
    Computes total cost of portfolio file
    """
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)  # header: names, number of shares, price
        for row_num, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            # catch missing data and errors in int(), float() conversion
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += num_shares * price
            except ValueError:
                print(f"Couldn't parse row {row_num}: {row}")

        f.close()
        # add up every price in the list
    return round(total_cost, 2)


# command line usage:
# ex: python pcost.py Data/portfolio.csv
if len(sys.argv) == 2:
    # sys.argv[0] is the name of the script (pcost.py)
    file = sys.argv[1]  # filename to be passed
else:
    file = "Data/portfolio.csv"

cost = portfolio_cost(file)
print(f"Total cost {cost}")
