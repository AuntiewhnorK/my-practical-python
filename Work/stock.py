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

    def cost(self):
        return self.shares * self.price

    def sell(self, sold):
        if sold > self.shares:
            print(f"Can't sell more than {self.shares}!")
        else:
            self.shares -= sold
