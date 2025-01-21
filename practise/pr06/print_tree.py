from common import tree, label, branches
from fib_tree import fib_tree

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent + str(label(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)