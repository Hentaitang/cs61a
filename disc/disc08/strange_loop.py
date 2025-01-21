from link_class import Link


def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    "*** YOUR CODE HERE ***"
    s = Link(1)
    s.first = s
    s.rest = s
    return s
