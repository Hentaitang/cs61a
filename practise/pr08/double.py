def double(s, v):
    """Insert another v after each v in list s.
    >>> s = [2, 7, 1, 8, 2, 8]
    >>> double(s, 8)
    >>> s
    [2, 7, 1, 8, 8, 2, 8, 8]
    """
    indexs = []
    for i in range(len(s)):
        if s[i] == v:
            indexs.append(i)
    for index in indexs:
        s.insert(index + 1, v)


def double2(s, v):
    """Insert another v after each v in list s.
    >>> s = [2, 7, 1, 8, 2, 8]
    >>> double2(s, 8)
    >>> s
    [2, 7, 1, 8, 8, 2, 8, 8]
    """
    index = 0
    while index < len(s):
        if s[index] == v:
            s.insert(index + 1, v)
            index += 2
        else:
            index += 1
