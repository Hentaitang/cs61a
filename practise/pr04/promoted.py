def promoted(s, f):
    """Return a list with the same elements as s, but with all
    elements e for which f(e) is a true value placed first.
    >>> promoted(range(10), odd) # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    return [x for x in s if f(x)] + [n for n in s if not f(n)]