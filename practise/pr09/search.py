def search_sorted_1(s, v):
    """Return whether v is in the sorted list s.
    >>> evens = [2*x for x in range(50)]
    >>> search_sorted(evens, 22)
    True
    >>> search_sorted(evens, 23)
    False
    """
    for num in s:
        if num == v:
            return True
    return False

def search_sorted_2(s, v):
    """Return whether v is in the sorted list s.
    >>> evens = [2*x for x in range(50)]
    >>> search_sorted(evens, 22)
    True
    >>> search_sorted(evens, 23)
    False
    """
    if len(s) == 0:
        return False
    center = len(s) // 2
    if s[center] > v:
        return search_sorted_2(s[:center], v)
    elif s[center] < v:
        return search_sorted_2(s[center:], v)
    else:
        return True
evens = [x for x in range(123456789)]
search_sorted_2(evens, 12345678)