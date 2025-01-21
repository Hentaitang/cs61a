def fib_generator():
    """
    A generator that yields the Fibonacci sequence indefinitely.
    (The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the previous two.)
    >>> fib = fib_generator()
    >>> next(fib)
    0
    >>> next(fib)
    1
    >>> next(fib)
    1
    >>> next(fib)
    2
    >>> list(next(fib) for i in range(0,10)) # list the next 10 fibonacci numbers
    [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    """
    prev_1, prev_2 = 0, 1
    while True:
        yield prev_1
        prev_1, prev_2 = prev_1 + prev_2, prev_1