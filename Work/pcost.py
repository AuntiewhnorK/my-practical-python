"""
Practical Python 1.27 - Reading files

Auntiewhnor Kpolie
04/28/2022

Open the file `portfolio.csv` in the Data folder,
reads all the lines, and calculates the total
cost to purchase all the shares in the portfolio.

Exercise 1.30 - make pcost.py a function
"""
import csv, sys
from fileinput import filename


def portfolio_cost(filename):
    # skip header
    with open(filename, "rt") as f:
        # use csv reader
        rows = csv.reader(f)
        # header: names, number of shares, price
        header = next(f)

        # create list to keep purchase price of shares
        shares = []

        # the price column is in a string and has a newline:
        # ex: '32.20\n'

        # need to replace the newline,
        # split each line into a list using .split()
        # take the last element (price)
        # multiply by share number

        for row in rows:
            # catch missing data
            try:
                # csv automatically parses
                # line.replace("\n", "")
                # new_line = line.split(",")
                share_price = int(row[1]) * float(row[2])
                shares.append(share_price)
            except ValueError:
                print("Couldn't parse", row)

        f.close()
        # add up every price in the list
        total = round(sum(shares), 2)
    return total


# command line usage:
# ex: python pcost.py Data/portfolio.csv
if len(sys.argv) == 2:
    # sys.argv[0] is the name of the script (pcost.py)
    filename = sys.argv[1]  # filename to be passed
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost {cost}")
