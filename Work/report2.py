"""
Practical Python - Tuples, Dictionaries, Functions

Auntiewhnor Kpolie
Created: 04/23/2022
Last Edited: 06/26/2022

Defines a function that opens a
portfolio file and prices file
and prints a report.
"""
from portfolio import Portfolio
from fileparse import parse_csv
from stock import Stock
import tableformat


def read_portfolio(file, **options):
    """Returns portfolio in a list of dictionaries"""

    # use ** to expose fileparse.parse_csv() options
    with open(file) as lines:
        portdicts = Portfolio.from_csv(lines, **options)

    # use **, keyword variable arguments
    # instead of explict dict[key] call

    return Portfolio(portdicts)


def read_prices(file):
    """Opens a file and returns a dictionary
    where the keys and values are stock names
    and current stock price"""

    with open(file) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(stock_portfolio, stock_price):
    """
    Takes in portfolio and prices file and makes
    a report
    """
    # total_value = 0.0
    report_list = []
    for element in stock_portfolio:
        name = element.name
        shares = element.shares
        purchase_price = element.price
        # total_value += (shares * purchase_price)

        current_price = stock_price[name]
        # gain_loss = ((current_price - purchase_price) / purchase_price) * 100
        change = current_price - purchase_price
        data = (name, shares, current_price, change)
        report_list.append(data)
    return report_list


def print_report(report, formatter):
    """
    Prints out a table
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for names, shares, price, change in report:
        rowdata = [names, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    """
    function for report printing
    """
    # set files for report
    file_portfolio = read_portfolio(portfolio_filename)
    file_prices = read_prices(prices_filename)

    # make report
    report_final = make_report(file_portfolio, file_prices)

    # printing
    formatter = tableformat.create_formatter(fmt)
    print_report(report_final, formatter)


def main(arguments):
    if len(arguments) != 4:
        raise SystemExit(f"Usage: {arguments[0]} " "portfile pricefile format")

    # single function call for reporting
    portfolio_report(arguments[1], arguments[2], arguments[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
