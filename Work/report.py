"""
Practical Python - Tuples, Dictionaries, Functions

Auntiewhnor Kpolie
Created: 04/23/2022
Last Edited: 05/06/2022

Defines a function that opens a
portfolio file and prices file
and prints a report.
"""
import csv


# Exercise 2.5


def read_portfolio(file):
    """Returns portfolio in a list of dictionaries"""
    portfolio = []
    with open(file) as f:
        rows = csv.reader(f)
        header = next(rows)  # header: names, shares, price list
        for row_number, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            # holding = (row[0], int(row[1]), float(row[2])) using tuple
            holding = {
                "name": record["name"],
                "shares": int(record["shares"]),
                "price": float(record["price"]),
            }
            portfolio.append(holding)

    return portfolio


# Exercise 2.6


def read_prices(file):
    """Opens a file and returns a dictionary
    where the keys and values are stock names
    and current stock price"""
    prices = {}
    with open(file) as f:
        rows = csv.reader(f)
        for row in rows:
            # can also use if statement
            # to check for empty list
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue

    return prices


# Exercise 2.7, 2.9


def make_report(stock_portfolio, stock_price):
    """
    Takes in portfolio and prices file and makes
    a report
    """
    # total_value = 0.0
    report_list = []
    for element in stock_portfolio:
        name = element["name"]
        shares = element["shares"]
        purchase_price = element["price"]
        # total_value += (shares * purchase_price)

        current_price = stock_price[name]
        # gain_loss = ((current_price - purchase_price) / purchase_price) * 100
        change = current_price - purchase_price
        data = (name, shares, current_price, change)
        report_list.append(data)
    return report_list


# Exercise 3.2
def print_report(report):
    """
    Prints out a table
    """
    headers = ("Name", "Shares", "Prices", "Change")
    print("%10s %10s %10s %10s" % headers)
    print("%10s" % "---------- " * len(headers))  # separator

    for names, share_num, price_num, change_num in report:
        print(
            f"{names:>10s} {share_num:>10d}",
            "{:>10}".format("${:.2f}".format(price_num)),
            f"{change_num:>10.2f}",
        )


def portfolio_report(portfolio_filename, prices_filename):
    """
    function for report printing
    """
    # set files for report
    file_portfolio = read_portfolio(portfolio_filename)
    file_prices = read_prices(prices_filename)

    # printing
    report_final = make_report(file_portfolio, file_prices)
    print_report(report_final)


# single function call for reporting
portfolio_report("Data/portfolio.csv", "Data/prices.csv")
