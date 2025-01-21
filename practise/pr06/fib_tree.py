from common import tree, label, branches

def fib_tree(n):
    """Return a Fibonacci tree of depth n."""
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])