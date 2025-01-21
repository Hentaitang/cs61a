from tree import Tree


def chop_head(hydra, n):
    assert n > 0 and n <= hydra.label
    if hydra.is_leaf():
        hydra.label = 2
        hydra.branches = [Tree(1), Tree(1)]
    else:
        hydra.label += 1
        left, right = hydra.branches
        if left.label < n:
            chop_head(right, n - left.label)
        else:
            chop_head(left, n)
