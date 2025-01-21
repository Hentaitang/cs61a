def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)

def list_partition(n, m):
    if m == 0 or n < 0:
        return []
    exact_match = []
    if m == n:
        exact_match =  [[m]]
    return exact_match + [p + [m] for p in list_partition(n - m, m)] + list_partition(n, m - 1)

def partition(n, m):
    if m == 0 or n < 0:
        return []
    exact_match = []
    if m == n:
        exact_match =  [str(m)]
    return exact_match + [p + ' + ' + str(m) for p in partition(n - m, m)] + partition(n, m - 1)

def gen_partitions(n, m):
    if m > 0 and n > 0:
        if n == m:
            yield str(m)
        for p in  gen_partitions(n - m, m):
            yield p + ' + ' + str(m)
        yield from gen_partitions(n, m - 1)


def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n - m, m):
            yield p + ' + ' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m - 1)