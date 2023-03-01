from . import fileparse
from . import stock


class Portfolio:
    """
    Container class
    Layer around a portfolio list of Stock instances
    """

    def __init__(self, holdings):
        self.holdings = holdings  # private variable

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError("Expected a Stock instance")
        self.holdings.append(holding)

    # classmethod to read csv files
    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls([])
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float], **opts
        )

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self

    # support iteration
    def __iter__(self):
        return self.holdings.__iter__()

    # other methods
    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, index):  # index like a list
        # portfolio[number]
        return self.holdings[index]

    def __contains__(self, name):  # check 'item' in portfolio
        return any(s.name == name for s in self.holdings)

    @property
    def total_cost(self):
        return sum(s.shares * s.price for s in self.holdings)

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self.holdings:
            total_shares[s.name] += s.shares
        return total_shares
