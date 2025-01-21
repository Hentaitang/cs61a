def add_to_each(p, edit):
    """
    Given a list, p, of 3-element tuples: [(x1, y1, z1), (x2, y2, z2), ...]
    And an edit tuple (also 3 elements) = (a, b, c),
    return a map object where
    a is added to each x-value,
    b to each y-value, and
    c to each z-value.
    >>> list(add_to_each([(0, 0, 0), (1, 1, 1)], (10, 10, 10)))
    [(10, 10, 10), (11, 11, 11)]
    >>> list(add_to_each([(1, 2, 3), (1, 1, 1)], (10, 20, 30)))
    [(11, 22, 33), (11, 21, 31)]
    """
    return map(lambda t: (t[0] + edit[0], t[1] + edit[1], t[2] + edit[2]), p)