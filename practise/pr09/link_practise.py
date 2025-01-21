from link_class import Link


def length_recursive(s):
    """The number of elements in s.
    >>> length_recursive(Link(3, Link(4, Link(5))))
    3
    """
    if s is Link.empty:
        return 0
    else:
        return 1 + length_recursive(s.rest)


def length_iterative(s):
    """The number of elements in s.
    >>> length_iterative(Link(3, Link(4, Link(5))))
    3
    """
    k = 0
    while s is not Link.empty:
        s, k = s.rest, k + 1
    return k


def range_link_recursive(start, end):
    """Return a Link containing consecutive
    integers from start up to end.
    >>> range_link_recursive(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link_recursive(start + 1, end))


def range_link_iterative(start, end):
    """Return a Link containing consecutive
    integers from start to end.
    >>> range_link_iterative(3, 6)
    Link(3, Link(4, Link(5)))
    """
    s = Link.empty
    k = end - 1
    while k >= start:
        s = Link(k, s)
        k -= 1
    return s


def append_recursive(s, x):
    """Append x to the end of non-empty s.
    >>> s = Link(3, Link(4, Link(5)))
    >>> append_recursive(s, 6) # returns None!
    >>> print(s)
    <3 4 5 6>
    """
    if s.rest is not Link.empty:
        append_recursive(s.rest, x)
    else:
        s.rest = Link(x)


def append_iterative(s, x):
    """Append x to the end of non-empty s.
    >>> s = Link(3, Link(4, Link(5)))
    >>> append_iterative(s, 6) # returns None!
    >>> print(s)
    <3 4 5 6>
    """
    while s.rest is not Link.empty:
        s = s.rest
    s.rest = Link(x)


def pop(s, i):
    """Remove and return element i from linked list s for positive i.
    >>> t = Link(3, Link(4, Link(5, Link(6))))
    >>> pop(t, 2)
    5
    >>> pop(t, 2)
    6
    >>> pop(t, 1)
    4
    >>> t
    Link(3)
    """
    assert i > 0 and i < length_recursive(s)
    for x in range(i - 1):
        s = s.rest
    pop = s.rest.first
    s.rest = s.rest.rest
    return pop