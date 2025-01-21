def f1(n):
    if n == 0:
        return 1
    else:
        return n * f1(n - 1)


def f(n, acc):
    def g():
        if n == 0:
            return acc
        else:
            return f(n - 1, n * acc)

    return g


def f2(n):
    val = f(n, 1)
    while callable(val):
        val = val()
    return val
