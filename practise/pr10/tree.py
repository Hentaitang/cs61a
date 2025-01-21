class Tree:
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            return f"Tree({repr(self.label)}, {repr(self.branches)}"
        else:
            return f"Tree({repr(self.label)})"


def climb(t, f):
    if t.is_leaf():
        return [t.label]
    return [t.label] + climb(max(t.branches, key=f), f)


def max_path(t, g):
    """Return the path s from the root of t to a leaf for which g(s) is largest.
    >>> scare = Tree(0, [Tree(4), Tree(5, [Tree(10)]), Tree(2)])
    >>> crow = Tree(4, [Tree(5), Tree(9, [scare, Tree(7, [Tree(6)])]), Tree(8)])
    >>> max_path(crow, lambda p: -p[-1]) # The path to the smallest leaf
    [4, 9, 0, 2]
    >>> max_path(crow, len) # The longest path
    [4, 9, 0, 5, 10]
    >>> max_path(crow, lambda p: -abs(p[0]-p[-1])) # To the leaf closest in value to the root
    [4, 9, 0, 4]
    """
    x = [t.label]  # You can use x instead of [t.label] to shorten your answer!
    return climb(t, lambda b: g(x + max_path(b, lambda n: g(x + n))))
