from operator import mul, truediv


def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float("inf")


def reduce(f, s, initial):
    """
    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial


def reduce_recur(f, s, initial):
    """
    >>> reduce_recur(mul, [2, 4, 8], 1)
    64
    """
    if not s:
        return initial
    else:
        return reduce_recur(f, s[1:], f(s[0], initial))
