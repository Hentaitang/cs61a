from fib import fib
def fib_test():
    assert fib(0) == 0, 'fib(0) should be 0'
    assert fib(1) == 1, 'fib(1) should be 1'
    assert fib(3) == 2, 'fib(3) should be 2'
    assert fib(50) == 12586269025, 'fib(50) should be 12586269025'

fib_test()