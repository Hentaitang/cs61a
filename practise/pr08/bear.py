class Bear:
    """A Bear.

    >>> oski = Bear()
    >>> oski
    Bear()
    >>> print(oski)
    a bear
    >>> print(str(oski))
    a bear
    >>> print(repr(oski))
    Bear()
    >>> print(oski.__repr__())
    oski
    >>> print(oski.__str__())
    oski the bear
    """

    def __init__(self):
        self.__str__ = lambda: "oski the bear"
        self.__repr__ = lambda: "oski"

    def __str__(self):
        return "a bear"

    def __repr__(self):
        return "Bear()"
