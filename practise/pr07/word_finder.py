def word_finder(letter_tree, words_list):
    """ Generates each word that can be formed by following a path
    in TREE_OF_LETTERS from the root to a leaf,
    where WORDS_LIST is a list of allowed words (with no duplicates).
    # Case 1: 2 words found
    >>> words = ['SO', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = Tree("S", [Tree("O"), Tree("A", [Tree("Q"), Tree("W")]), Tree("C", [Tree("H")])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> next(gen)
    'SAW'
    >>> list(word_finder(t, words))
    ['SO', 'SAW']

    # Case 2: No words found
    >>> t = Tree("S", [Tree("I"), Tree("A", [Tree("Q"), Tree("E")]), Tree("C", [Tree("H")])])
    >>> list(word_finder(t, words))
    []

    # Case 3: Same word twice
    >>> t = Tree("S", [Tree("O"), Tree("O")] )
    >>> list(word_finder(t, words))
    ['SO', 'SO']

    # Case 4: Words that start the same
    >>> words = ['TAB', 'TAR', 'BAT', 'BAR', 'RAT']
    >>> t = Tree("T", [Tree("A", [Tree("R"), Tree("B")])])
    >>> list(word_finder(t, words))
    ['TAR', 'TAB']

    # Case 5: Single letter words
    >>> words = ['A', 'AN', 'AH']
    >>> t = Tree("A")
    >>> list(word_finder(t, words))
    ['A']

    # Case 6: Words end in leaf
    >>> words = ['A', 'AN', 'AH']
    >>> t = Tree("A", [Tree("H"), Tree("N")])
    >>> list(word_finder(t, words))
    ['AH', 'AN']

    # Case 7: Words start at root
    >>> words = ['GO', 'BEARS', 'GOB', 'EARS']
    >>> t = Tree("B", [Tree("E", [Tree("A", [Tree("R", [Tree("S")])])])])
    >>> list(word_finder(t, words))
    ['BEARS']

    # Case 8: This special test ensures that your solution does *not*
    # pre-compute all the words before yielding the first one.
    # If done correctly, your solution should error only when it
    # tries to find the second word in this tree.
    >>> words = ['SO', 'SAM', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = Tree("S", [Tree("O"), Tree("A", [Tree("Q"), Tree(1)]), Tree("C", [Tree(1)])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> try:
    ...     next(gen)
    ... except TypeError:
    ...     print("Got a TypeError!")
    ... else:
    ...     print("Expected a TypeError!")
    Got a TypeError!
    """
    def str_builder(tree, string):
        string += tree.label
        if tree.is_leaf() and string in words_list:
            yield string
        for branch in tree.branches:
            yield from str_builder(branch, string)
    yield from str_builder(letter_tree, '')
    # def fn(tree):
    #     if tree.is_leaf():
    #         yield str(tree.label)
    #     for branch in tree.branches:
    #         yield from [str(tree.label) + l for l in fn(branch)]
    # yield from [letter for letter in fn(letter_tree) if letter in words_list]

class Tree:
    """A tree."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches
