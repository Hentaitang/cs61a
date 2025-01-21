from tree import Tree


def pile(t):
    """Return a dict that contains every path from a leaf to the root of tree t.
    >>> pile(Tree(5, [Tree(3, [Tree(1), Tree(2)]), Tree(6, [Tree(7)])]))
    {1: (3, (5, ())), 2: (3, (5, ())), 7: (6, (5, ()))}
    """
    p = {}

    def gather(u, path):
        if u.is_leaf():
            p[u.label] = path
        for b in u.branches:
            gather(b, (u.label, path))

    gather(t, ())
    return p


class Path:
    """A path through a tree from the root to a leaf, identified by its leaf label.
    >>> a = Tree(5, [Tree(3, [Tree(1), Tree(2)]), Tree(6, [Tree(7)])])
    >>> print(Path(a, 7), Path(a, 2))
    5-6-7 5-3-2
    """

    def __init__(self, t, leaf_label):
        self.pile, self.end = pile(t), leaf_label

    def __str__(self):
        path, s = self.pile[self.end], str(self.end)
        while path:
            path, s = path[1], f"{str(path[0])}-{s}"
        return s


def pile_list(t):
    """Return a dict that contains every path from a leaf to the root of tree t.
    >>> pile_list(Tree(5, [Tree(3, [Tree(1), Tree(2)]), Tree(6, [Tree(7)])]))
    {1: [5, 3, 1], 2: [5, 3, 2], 7: [5, 6, 7]}
    """
    p = {}

    def gather(u, path):
        if u.is_leaf():
            p[u.label] = path + [u.label]
        for b in u.branches:
            gather(b, path + [u.label])

    gather(t, [])
    return p
