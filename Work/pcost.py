"""
Practical Python 1.27 - Reading files

Auntiewhnor Kpolie
04/28/2022

Open the file `portfolio.csv` in the Data folder,
reads all the lines, and calculates the total
cost to purchase all the shares in the portfolio.

Excerise 1.30 - make pcost.py a function
"""


def portfolio_cost(filename):
    # skip header
    f = open(filename, "rt")
    header = next(f)
    # header: names, number of shares, price

    # create list to keep purchase price of shares
    shares = []

    # the price column is in a string and has a newline:
    # ex: '32.20\n'

    # need to replace the newline,
    # split each line into a list using .split()
    # take the last element (price)
    # multiply by share number

    for line in f:
        line.replace("\n", "")
        new_line = line.split(",")
        # float of string
        share_price = int(new_line[1]) * float(new_line[2])
        shares.append(share_price)

    f.close()

    # add up every price in the list
    total = round(sum(shares), 2)
    return total


cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost {cost}")
