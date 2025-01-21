def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def f(i):
        if n == i:
            return True
        elif n % i == 0:
            return False
        return f(i + 1)
    return f(2)
