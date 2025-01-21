def memo(f):
    cache = {}

    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memorized
