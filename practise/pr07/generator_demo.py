def generator_demo():
    def cycle(s):
        while True:
            for x in s:
                print("before yielding!")
                yield x
                print("after yielding!")


    l = [1,2,3]
    g = cycle(l)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))