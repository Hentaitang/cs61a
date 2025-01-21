def prefix(s):
    """Return a list of all prefix sums of list s

    >>> prefix([1, 2, 3])
    [1, 3, 6]
    >>> prefix([2, 2, 2, 0, -5, 5])
    [2, 4, 6, 6, 1, 6]
    """
    return [sum(s[:k+1]) for k in range(len(s))]