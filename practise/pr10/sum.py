def sums(n, k):
    """Return the ways in which K positive integers can sum to N.
    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(2, 3)
    []
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if k == 1:
        return [[n]]
    y = []
    for x in range(1, n):
        y.extend([s + [x] for s in sums(n - x, k - 1)])
    return y


f = lambda x, y: (x and [[x] + z for z in y] + f(x - 1, y)) or []


def sums_2(n, k):
    """Return the ways in which K positive integers can sum to N.
    >>> sums_2(2, 2)
    [[1, 1]]
    >>> sums_2(2, 3)
    []
    >>> sums_2(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums_2(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    g = lambda w: (w and f(n, g(w - 1))) or [[]]
    return [v for v in g(k) if sum(v) == n]
