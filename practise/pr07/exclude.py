from common import tree, label, branches

def exclude(t, x):
    """Return a tree with the non-root nodes of t whose labels are not equal to x.
    >>> t = tree(1, [tree(2, [tree(2), tree(3)]), tree(4, [tree(1)])])
    >>> exclude(t, 2)
    tree(1, [tree(3), tree(4, [tree(1)])])
    >>> t # t is not changed
    tree(1, [tree(2, [tree(2), tree(3)]), tree(4, [tree(1)])])
    >>> exclude(t, 1) # The root node cannot be excluded
    tree(1, [tree(2, [tree(2), tree(3)]), tree(4)])
    """
    filtered_branches = map(lambda y: exclude(y, x), branches(t))

    bs = []
    for b in filtered_branches:
        if label(b) == x:
            bs.extend(branches(b))
        else:
            bs.append(b)
    print(bs)
    return tree(label(t), bs)