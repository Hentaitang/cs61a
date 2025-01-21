from common import tree, label, branches

def count_paths(t, total):
    """Count paths from root to leaves that sum to total.

    >>> t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if total == label(t):
        found = 1
    else:
        found = 0
    return found + sum([count_paths(branch, total - label(t)) for branch in branches(t)])