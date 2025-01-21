from link_class import Link


def overlap_list(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = [3,4,6,7,9,10]
    >>> b = [1,3,5,7,8]
    >>> overlap_list(a, b)  # 3 and 7
    2
    >>> overlap_list(a[1:], b)  # just 7
    1
    >>> overlap_list([0]+a, [0]+b)
    3
    """
    "*** YOUR CODE HERE ***"
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] > t[j]:
            j += 1
        else:
            i += 1
    return count


def overlap_recursive(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap_recursive(a, b)  # 3 and 7
    2
    >>> overlap_recursive(a.rest, b)  # just 7
    1
    >>> overlap_recursive(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty or t is Link.empty:
        return 0
    elif s.first == t.first:
        return 1 + overlap_recursive(s.rest, t.rest)
    elif s.first > t.first:
        return overlap_recursive(s, t.rest)
    else:
        return overlap_recursive(s.rest, t)


def overlap_iter(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap_iter(a, b)  # 3 and 7
    2
    >>> overlap_iter(a.rest, b)  # just 7
    1
    >>> overlap_iter(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while s is not Link.empty and t is not Link.empty:
        if s.first == t.first:
            count, s, t = count + 1, s.rest, t.rest
        elif s.first > t.first:
            t = t.rest
        else:
            s = s.rest
    return count
