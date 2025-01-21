class Transaction:
    """A logged transaction.
    >>> s = [20, -3, -4]
    >>> ts = [Transaction(x) for x in s]
    >>> ts[1].balance()
    17
    >>> ts[2].balance()
    13
    """
    log = []
    def __init__(self, amount):
        self.amount = amount
        self.prior = sum([t.amount for t in self.log])
        self.log.append(self)
    def balance(self):
        return self.amount + self.prior