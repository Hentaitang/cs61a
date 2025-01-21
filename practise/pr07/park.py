def park(n):
    """Yield the ways to park cars and motorcycles in n adjacent spots.
    >>> sorted(park(1))
    ['%', '.']
    >>> sorted(park(2))
    ['%%', '%.', '.%', '..', '<>']
    >>> sorted(park(3))
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(list(park(4)))
    29
    """
    if n == 0:
        yield ''
    elif n > 0:
        for s in park(n-1):
            yield s + '%'
            yield s + '.'
        for s in park(n-2):
            yield s +'<>'