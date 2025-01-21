from link_class import Link


def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f"{s.first} is not 0"
    digits = f"{s.first}."
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f"{s.first} is not a digit"
        digits += str(s.first)
        s = s.rest
    print(digits + "...")


def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    "*** YOUR CODE HERE ***"
    cache = {}
    tail = result
    while n not in cache:
        tail.rest = Link(10 * n // d)
        tail = tail.rest
        cache[n] = tail
        n = n * 10 % d
    tail.rest = cache[n]
    return result
