class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branches_str = f", {repr(self.branches)}"
        else:
            branches_str = ""
        return "Tree({0}{1})".format(repr(self.label), branches_str)

    def __str__(self):
        return "\n".join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append("    " + line)
        return [str(self.label)] + lines


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 1)
        right = fib_tree(n - 2)
        return Tree(left.label + right.label, [left, right])


def leaves(tree):
    """Return a list containing the leaf labels of tree."""
    assert isinstance(tree, Tree)
    if tree.is_leaf():
        return [tree.label]
    else:
        all_leaves = []
        for b in tree.branches:
            all_leaves.extend(leaves(b))
        return all_leaves


def height(tree):
    """Return the number of branches in the deepest path in tree."""
    if tree.is_leaf():
        return 1
    else:
        return 1 + max([height(b) for b in tree.branches])
