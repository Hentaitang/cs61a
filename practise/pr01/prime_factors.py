def prime_factors(n):
    """Return the prime factors of n as a list."""
    while n > 1:
        k = smallest_prime_factor(n)
        print(k)
        n = n // k

def smallest_prime_factor(n):
    """Return the smallest prime factor of n."""
    k = 2
    while n % k != 0:
        k += 1
    return k