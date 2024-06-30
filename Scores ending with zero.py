Scores = [200, 456, 300, 100,234, 678]
def zero(L):
    s = 0
    for i in L:
        if i % 10 == 0:
            s = s + i
    return s

b = zero(Scores)
print(b)