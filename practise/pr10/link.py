class Link:
    empty = ()

    def __init__(self, first, rest=()):
        assert isinstance(rest, Link) or rest == Link.empty
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ""
        else:
            rest = f", {repr(self.rest)}"
        return "Link({0}{1})".format(self.first, rest)


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


Link.__add__ = extend_link


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def join_link(s, separator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return f"{str(s.first)}{separator}{join_link(s.rest, separator)}"
