# DRY
def digits(n):
    """Return the number of digits in positive integer n.

    >>> digits(5)
    1
    >>> digits(10)
    2
    """
    assert n >= 0, 'n must be positive'
    k = 0
    while n:
        n, k = n // 10, k + 1
    return k

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(1000, 100000)
    False
    """
    return digits(a) == digits(b)

# Higher-order function
def double(x):
    return 2 * x

def twice(f, x):
    """Apply f twice to x.

    >>> twice(double, 3)
    12
    """
    return f(f(x))

# Local function definitions; returning functions
def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Nim
def play(strategy0, strategy1, goal=21):
    """Play twenty-one and return the index of the winner.

    >>> play(two_strat, two_strat)
    1
    """
    n, who = 0, 0
    while(n < goal):
        if who == 0:
            n += strategy0(n)
            who = 1
        elif who == 1:
            n += strategy1(n)
            who = 0
    return who

def two_strat(n):
    return 2

def interactive_start(n):
    choice = 0
    while choice > 3 or choice < 1:
        print('How much will you add to', n, '(1-3)?', end=' ')
        choice = int(input())
    return choice