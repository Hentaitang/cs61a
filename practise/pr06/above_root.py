from common import tree, label, branches

def above_root(t):
    """Print all the labels of t that are larger than the root label.

    >>> t = tree(3, [tree(-1), tree(2, [tree(4, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> above_root(t)
    4
    >>> above_root(branches(t)[1])
    4
    3
    """
    def progress(u):
        if label(u) > label(t):
            print(label(u))
        else:
            for branch in branches(u):
                progress(branch)
    progress(t)