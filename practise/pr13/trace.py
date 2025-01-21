def trace(fn):
    def traced(n):
        print(f"{fn.__name__}({n})")
        return fn(n)

    return traced

@trace
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
