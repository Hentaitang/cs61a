from common import apply_to_all, keep_if, reduce
from operator import add
def divisors_of(n):
    return [1] + keep_if(lambda x: n % x == 0, range(2, n))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return n == sum_of_divisors(n)