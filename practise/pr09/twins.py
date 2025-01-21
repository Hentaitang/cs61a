from tree import Tree


def twins(t):
    """Count the pairs of sibling nodes with equal labels.
    >>> t1 = Tree(3, [Tree(4, [Tree(5), Tree(6)]), Tree(4, [Tree(5), Tree(5)])])
    >>> twins(t1) # 4 and 5
    2
    >>> twins(Tree(1, [Tree(1, [Tree(2)]), Tree(2, [Tree(2)])]))
    0
    >>> twins(Tree(8, [t1, t1, t1])) # 3 pairs of twins at the top, plus 2 in each branch
    9
    """
    count = 0
    n = len(t.branches)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if t.branches[i].label == t.branches[j].label:
                count += 1
    return count + sum([twins(branch) for branch in t.branches])


def exclude(t, x):
    """Exclude all non-root nodes labeled x from t.
    >>> u = Tree(1, [Tree(2, [Tree(2), Tree(3)]), Tree(4)])
    >>> exclude(u, 2)
    Tree(1, [Tree(3), Tree(4)])

    >>> v = Tree(2, [Tree(2, [Tree(3), Tree(2)]), Tree(4)])
    >>> exclude(v, 2)
    Tree(2, [Tree(3), Tree(4)])

    >>> w = Tree(1, [Tree(3), Tree(4)])
    >>> exclude(w, 2)
    Tree(1, [Tree(3), Tree(4)])

    >>> x_tree = Tree(1, [
    ...     Tree(2, [
    ...         Tree(2, [Tree(2), Tree(5)]),
    ...         Tree(3)
    ...     ]),
    ...     Tree(2, [Tree(4), Tree(2)])
    ... ])
    >>> exclude(x_tree, 2)
    Tree(1, [Tree(5), Tree(3), Tree(4)])

    >>> y_tree = Tree(1, [
    ...     Tree(2, [
    ...         Tree(2, [Tree(2, [Tree(2, [Tree(2), Tree(8)]), Tree(6, [Tree(2), Tree(7)])]), Tree(5)]),
    ...         Tree(3)
    ...     ]),
    ...     Tree(2, [Tree(4), Tree(2)])
    ... ])
    >>> exclude(y_tree, 2)
    Tree(1, [Tree(8), Tree(6, [Tree(7)]), Tree(5), Tree(3), Tree(4)])
    """

    def flatten_branches(branches, x):
        result = []
        for b in branches:
            if b.label == x:
                result.extend(flatten_branches(b.branches, x))
            else:
                result.append(Tree(b.label, flatten_branches(b.branches, x)))
        return result

    return Tree(t.label, flatten_branches(t.branches, x))


def remove(t, x):
    """Remove all non-root nodes labeled x from t.
    >>> u = Tree(1, [Tree(2, [Tree(2), Tree(3)]), Tree(4)])
    >>> remove(u, 2)
    Tree(1, [Tree(3), Tree(4)])
    >>> remove(u, 3)
    Tree(1, [Tree(4)])
    """
    t.branches = exclude(t, x).branches
    return t
