class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __str__(self):
        return "{0}/{1}".format(self.numer, self.denom)

    def __repr__(self):
        return "Radio({0}, {1})".format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + other * self.denom
            d = self.denom
        elif isinstance(other, float):
            return float(self) + other
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + other.numer * self.denom
            d = self.denom * other.denom
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    def __float__(self):
        return self.numer / self.denom

    __radd__ = __add__


def gcd(a, b):
    while a != b:
        a, b = min(a, b), abs(a - b)
    return a
