class Stock:
    """
    Represents a single holding of stock
    cost: returns the cost of stock
    sell: sell an amount of shares
    """

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    @property
    def shares(self):
        return self._shares  # private attribute

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):  # check if attribute is integer
            raise TypeError('Expected integer')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sold):
        if sold > self.shares:
            print(f"Can't sell more than {self.shares}!")
        else:
            self.shares -= sold
