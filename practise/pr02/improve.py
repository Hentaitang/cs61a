from math import sqrt
def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1 / guess + 1

def gloden_close(guess):
    return appro_equal(guess ** 2, guess + 1)

def appro_equal(x, y, tolerance = 1e-15):
    return abs(x - y) < tolerance

def improve_test():
    phi = (1 + sqrt(5)) / 2
    appro_phi = improve(golden_update, gloden_close)
    assert appro_equal(phi, appro_phi)

def average(x, y):
    return (x + y) / 2

def sqrt_improve(n):
    def sqrt_update(x):
        return average(x, n / x)

    def sqrt_close(x):
        return appro_equal(x**2, n)

    return improve(sqrt_update, sqrt_close)