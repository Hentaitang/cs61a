def fib(n):
    """Return the nth fibonacci number."""
    prev, curr = 1, 1
    k = 2
    while k < n:
        prev, curr = curr, prev + curr
        k += 1
    if n < 1:
        return 0
    else:
        return curr