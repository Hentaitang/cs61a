from link import *
from tree import *


def count_big(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> count_big(t, 3)
    3
    >>> count_big(t, 6)
    2
    >>> count_big(t, 9)
    1
    """
    if t.is_leaf():
        if t.label >= n:
            return 1
        else:
            return 0
    else:
        return sum([count_big(branch, n - t.label) for branch in t.branches])


def print_big(t, n):
    """Print the paths in t that have a sum larger or equal to n.

    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> print_big(t, 3)
    [1, 2]
    [1, 3, 4]
    [1, 3, 5]
    >>> print_big(t, 6)
    [1, 3, 4]
    [1, 3, 5]
    >>> print_big(t, 9)
    [1, 3, 5]
    """

    def helper(t, list):
        newList = list + [t.label]
        if t.is_leaf():
            if sum(newList) >= n:
                print(newList)
        for branch in t.branches:
            helper(branch, newList)

    helper(t, [])


def big_links(t, n):
    """Yield the paths in t that have a sum larger or equal to n as linked lists.

    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> for p in big_links(t, 3):
    ...     print(p)
    <1 2>
    <1 3 4>
    <1 3 5>
    >>> for p in big_links(t, 6):
    ...     print(p)
    <1 3 4>
    <1 3 5>
    >>> for p in big_links(t, 9):
    ...     print(p)
    <1 3 5>
    """
    if t.is_leaf() and t.label >= n:
        yield Link(t.label)
    else:
        for b in t.branches:
            for link in big_links(b, n - t.label):
                yield Link(t.label, link)
