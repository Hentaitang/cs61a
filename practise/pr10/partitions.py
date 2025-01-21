from link import Link, map_link, join_link


def partitions(n, m):
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        with_m = map_link(lambda s: Link(m, s), partitions(n - m, m))
        without_m = partitions(n, m - 1)
        if with_m is Link.empty:
            return without_m
        elif without_m is Link.empty:
            return with_m
        else:
            return with_m + without_m


def print_partitions(n, m):
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))
