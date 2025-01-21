from common import tree, label, branches

def largest_label(t):
    """Return the largest label in tree t.

    >>> t = tree(3, [tree(-1), tree(2, [tree(4, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> largest_label(t)
    4
    """
    return max([largest_label(branch) for branch in branches(t)] + [label(t)])