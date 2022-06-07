class Portfolio:
    """
    Layer around a portfolio list
    """

    def __init__(self, holdings):
        self._holdings = holdings  # private variable

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
