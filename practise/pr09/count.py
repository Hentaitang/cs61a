def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def count(f):
    """Return a function that counts the number of times it is applied."""

    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def count_frames(f):
    """Return a function that counts the number of frames on the call stack associated with it."""

    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


@count
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
