def min_abs_indices(s):
    """Indices of all elements in s that have the smallest absolute value.

    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    >>> min_abs_indices([1, 2, 3, 4, -1])
    [0, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])
    [0, 5]
    """
    return [i for i in range(len(s)) if abs(s[i]) == min(s, key=abs)]


def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list.

    >>> largest_adj_sum([1, 2, 3, 4, 5])
    9
    >>> largest_adj_sum([1, 2, 3, 4, 5, -1])
    9
    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([x + y for x, y in zip(s[:-1], s[1:])])


def digit_dict(s):
    """Map each digit d to the list of elements in s that end with d.

    >>> digit_dict([525, 45, 717, 846])
    {5: [525, 45], 6: [846], 7: [717]}
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [n for n in s if n % 10 == d] for d in range(10) if d in map(lambda n: n % 10, s)}


def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([1, 2, 3, 4, 5])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    # return all([s[i] in s[:i] + s[i + 1 :] for i in range(len(s))])
    return min([s.count(x) for x in s]) > 1
