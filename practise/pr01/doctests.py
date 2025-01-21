# from doctest import testmod

def sum_natural(n):
    """retutn the sum of natural numbers from 1 to n
    >>> sum_natural(5)
    15
    >>> sum_natural(10)
    55
    >>> sum_natural(100)
    5050
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

# print(testmod())