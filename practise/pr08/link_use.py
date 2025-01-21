from link_class import Link


def map_link(f, s):
    """Return a Link with f applied to each element of s.
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    """Return a Link with only elements of s for which f(e) is true.
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def range_link(start, end):
    """Return a Link with elements start, start+1, ..., end-1.
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))


square, odd = lambda x: x * x, lambda x: x % 2 == 1
list(map(square, filter(odd, range(1, 6))))  # [1, 9, 25]
map_link(square, filter_link(odd, range_link(1, 6)))  # Link(1, Link(9, Link(25)))


def double_link(s, v):
    """Insert another v after each v in linked list s.
    >>> s = Link(2, Link(7, Link(1, Link(8, Link(2, Link(8))))))
    >>> double_link(s, 8)
    >>> print(s)
    <2 7 1 8 8 2 8 8>
    """
    while s is not Link.empty:
        if s.first == v:
            s.rest = Link(v, s.rest)
            s = s.rest.rest
        else:
            s = s.rest


def cycle(k, n):
    """Build an n-element list that cycles among range(k).
    >>> cycle(3, 10)
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    """
    list = []
    for x in range(n):
        list.append(x % k)
    return list


def cycle2(k, n):
    """Build an n-element list that cycles among range(k).
    >>> cycle2(3, 10)
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    """
    list = []
    while n > 0:
        for x in range(k):
            if n > 0:
                list.append(x)
                n -= 1
    return list


def cycle_link(k, n):
    """Build an n-element linked list that cycles among range(k).
    >>> print(cycle_link(3, 10))
    <0 1 2 0 1 2 0 1 2 0>
    """
    first = Link.empty
    for i in range(n):
        new_link = Link(i % k)
        if first is Link.empty:
            first, last = new_link, new_link
        else:
            last.rest, last = new_link, new_link
    return first


def cycle_link2(k, n):
    """Build an n-element linked list that cycles among range(k).
    >>> print(cycle_link2(3, 10))
    <0 1 2 0 1 2 0 1 2 0>
    """
    link = Link.empty
    n -= 1
    while n >= 0:
        link = Link(n % k, link)
        n -= 1
    return link


def slice_link(s, i, j):
    """Return a linked list containing elements from i:j.
    >>> evens = Link(4, Link(2, Link(6)))
    >>> slice_link(evens, 1, 100)
    Link(2, Link(6))
    >>> slice_link(evens, 1, 2)
    Link(2)
    >>> slice_link(evens, 0, 2)
    Link(4, Link(2))
    >>> slice_link(evens, 1, 1) is Link.empty
    True
    """
    assert i >= 0 and j >= 0
    link = Link.empty
    for x in range(j):
        if s is Link.empty:
            break
        if x >= i:
            temp = Link(s.first)
            if link is Link.empty:
                link, last = temp, temp
            else:
                last.rest, last = Link(s.first), s
        s = s.rest
    return link


def slice_link2(s, i, j):
    """Return a linked list containing elements from i:j.
    >>> evens = Link(4, Link(2, Link(6)))
    >>> slice_link2(evens, 1, 100)
    Link(2, Link(6))
    >>> slice_link2(evens, 1, 2)
    Link(2)
    >>> slice_link2(evens, 0, 2)
    Link(4, Link(2))
    >>> slice_link2(evens, 1, 1) is Link.empty
    True
    """
    assert i >= 0 and j >= 0
    if j == 0 or s is Link.empty:
        return Link.empty
    elif i == 0:
        return Link(s.first, slice_link2(s.rest, i, j - 1))
    else:
        return slice_link2(s.rest, i - 1, j - 1)


def insert_link(s, x, i):
    """Insert x into linked list s at index i.
    >>> evens = Link(4, Link(2, Link(6)))
    >>> insert_link(evens, 8, 1)
    >>> insert_link(evens, 10, 4)
    >>> insert_link(evens, 12, 0)
    >>> insert_link(evens, 14, 10)
    Index out of range
    >>> print(evens)
    <12 4 8 2 6 10>
    """
    if s is Link.empty:
        print("Index out of range")
    elif i == 0:
        second = Link(s.first, s.rest)
        s.first = x
        s.rest = second
    elif i == 1 and s.rest is Link.empty:
        s.rest = Link(x)
    else:
        insert_link(s.rest, x, i - 1)


def tens(s):
    """Print all prefix sums of Link s that are multiples of ten.
    >>> tens(Link(3, Link(9, Link(8, Link(10, Link(0, Link(14, Link(6))))))))
    20
    30
    30
    50
    """
    sum = 0
    last = s
    while last is not Link.empty:
        sum += last.first
        if sum % 10 == 0:
            print(sum)
        last = last.rest


def tens2(s):
    """Print all prefix sums of Link s that are multiples of ten.
    >>> tens2(Link(3, Link(9, Link(8, Link(10, Link(0, Link(14, Link(6))))))))
    20
    30
    30
    50
    """

    def f(suffix, total):
        if total % 10 == 0:
            print(total)
        if suffix is not Link.empty:
            f(suffix.rest, total + suffix.first)

    f(s.rest, s.first)
