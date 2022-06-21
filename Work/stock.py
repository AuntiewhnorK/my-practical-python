from typedproperty import String, Integer, Float


class Stock:
    """
    Represents a single holding of stock
    cost: returns the cost of stock
    sell: sell an amount of shares
    """

    # restrict attributes
    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sold):
        if sold > self.shares:
            print(f"Can't sell more than {self.shares}!")
        else:
            self.shares -= sold
