def apply_to_all(fn, list):
    """map"""
    return [fn(n) for n in list]
def keep_if(fn, list):
    """filter"""
    return [n for n in list if fn(n)]

def reduce(fn, list, initial):
    """Return the result of applying fn to all the elements of the list, starting with initial."""
    reduced = initial
    for item in list:
        reduced = fn(reduced, item)
    return reduced