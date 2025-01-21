def smallest_factor(n):
    if n%2 == 0:
        return 2
    k = 3
    while k < n:
        if n%k == 0:
            return k
        k += 1
    return n

def unique_prime_factors(n):
    """Return the number of unique prime factors of n.

    >>> unique_prime_factors(51)  # 3 * 17
    2
    >>> unique_prime_factors(27)   # 3 * 3 * 3
    1
    >>> unique_prime_factors(120) # 2 * 2 * 2 * 3 * 5
    3
    """
    k = smallest_factor(n)
    def no_k(x):
        if x == 1:
            return 0
        elif x % k != 0:
            return unique_prime_factors(x)
        else:
            return no_k(x//k)
    return 1 + no_k(n)