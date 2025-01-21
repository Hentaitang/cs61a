from tree import Tree


def fib_tree(n):
    if n == 1:
        return Tree(1)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 1)
        right = fib_tree(n - 2)
        return Tree(left.label + right.label, [left, right])

def sum_fib(s):
    return s.label + sum([sum_fib(b) for b in s.branches])
