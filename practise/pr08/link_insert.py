from link_class import Link


def link_insert(lnklst, value, before):
    """Return a linked list identical to LNKLST, but with VALUE inserted just
    before the first occurrence of BEFORE in the list, if any. The returned
    list is identical to LNKLST if BEFORE does not occur in LNKLST.
    The operation is non-destructive.
    >>> L = link(2, link(3, link(7, link(1))))
    >>> print_link(L)
    (2, 3, 7, 1)
    >>> Q = link_insert(L, 19, 7)
    >>> print_link(Q)
    (2, 3, 19, 7, 1)
    >>> print_link(link_insert(L, 19, 20))
    (2, 3, 7, 1)
    """
    if lnklst is Link.empty:
        return lnklst
    elif lnklst.first == before:
        return Link(value, lnklst)
    else:
        return Link(lnklst.first, link_insert(lnklst.rest, value, before))
