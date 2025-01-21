from link_class import Link


def ordered(s, key=lambda x: x):
    """Is Link s ordered?

    >>> ordered(Link(1, Link(2, Link(3))))
    True
    >>> ordered(Link(1, Link(3, Link(2))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key=abs)
    True
    >>> ordered(Link(1, Link(4, Link(3))), key=abs)
    False
    """
    if s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)


def merge(s, t):
    """Return a new list that merges sorted lists s and t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(3))
    >>> merge(a, b)
    Link(1, Link(1, Link(3, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(3))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))


def merge_in_place(s, t):
    """Return a sorted Link with the elements of sorted s & t.

    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(1, Link(4, Link(5))))
    >>> b
    Link(1, Link(4, Link(5)))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t
