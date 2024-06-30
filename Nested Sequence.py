def flatten(L):
    for e in L:
        if hasattr(e, '__iter__'):
            yield from flatten(e)
        else:
            yield e

#g = flatten([1, 2, 3, 4, 5, 6, 7, 8])
g = flatten([1, 2,[3, 4, [5, 6], 7], 8])
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
