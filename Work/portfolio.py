class Portfolio:
    """
    Container class
    Layer around a portfolio list
    """

    def __init__(self, holdings):
        self._holdings = holdings  # private variable

    # support iteration
    def __iter__(self):
        return self._holdings.__iter__()

    # other methods
    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):  # index like a list
        # portfolio[number]
        return self._holdings[index]

    def __contains__(self, name):  # check 'item' in portfolio
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
