def max3(x,y,z):
    if x>y and x>z:
        return x
    elif y>z:
        return y
    else:
        return z

b1 = int(input('Enter number 1: '))
b2 = int(input('Enter number 2: '))
b3 = int(input('Enter number 3: '))
print(max3(b1, b2, b3))
