# Intro
def add3(a, b, c):
    r = a + b + c
    return r


res = add3(10, 25, 5)
print(res)
print("                                     ")


# Default Args
def add1(a, b=0, c=0):
    return a + b + c


print(add1(11, 2))


def sum_item(item, L=[]):
    L.append(item)
    return L


L1 = [1, 2, 3, 4, 5]
sum_item(6, L1)
print(L1)
print(sum_item(7))
print("                                     ")


# Variable Length Arg
def fun1(*args):
    print(type(args), args)


fun1()
fun1(10, 20)
fun1(20324, 32432, 32432, 432342, 32432, 432324)


# Unpacking Args
def fun2(a, b, c):
    print(a, b, c)


L2 = [11, 22, 33]
fun2(L1[0], L1[1], L1[2])
fun2(*L2)


def fun3(a, b, c):
    return a + 1, b + 1, c + 1


x, y, z = fun3(10, 20, 30)
t = fun3(5, 10, 15)
print(t)


def fun4(**kwargs):
    print(kwargs)


fun4(name='ajay', roll_no=10, home='delhi', mom="laila")


def fun5(a, b, *args, **kwargs):
    print(a, b, *args, kwargs)


fun5(2, 4, 20, 30, 40, 68, 39, 9324, name='ajay', roll_no=10, home='delhi', mom="laila")
print("                                     ")

# Iterators and Generators
L3 = [1, 2, 3, 4, 5]

itr = iter(L3)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print("                                     ")


# Generators
def Days():
    L = ['sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
    i = 0
    while True:
        x = L[i]
        i = (i + 1) % 7
        yield x


d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print("                                     ")
# Global vs Local Variable
g = 10


def gvl(a, b):
    c = a + b
    print('local', c)
    print('global', g)


gvl(4, 9)

a, b, c, d = 11, 22, 33, 44


def gvl1(a=15, b=25):
    x, y, z = 1, 2, 3
    print(locals())


gvl1()
print(globals())
print("                                     ")


# Recursive Function
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
print("                                     ")

# Built-In Functions
o = -15
print(abs(o))  # gives positive val in any case
letter = '\u0521'
print(ascii(letter))  # gives ascii code
print("                                     ")

print(bin(o))  # gives binary value
print("                                     ")

print(bool(o))  # converts to boolean datatype
print("                                     ")

ba = bytearray(6)  # Creates array of bytes
print(ba)
print("                                     ")

n = 10


def add(a, b):
    return a + b


print(callable(n))  # check if obj is func or not
print(callable(add))
print("                                     ")

print(chr(65))  # takes ascii code gives char
print("                                     ")

print(ord('A'))  # takes char gives code
print("                                     ")

print(dir(str))  # gives details of the class
print("                                        ")

print(divmod(10, 3))  # gives div as well as mod
print("                                           ")

o1 = [1, 2, 3, 4, 5]  # gives indexing if used with for loop
e = enumerate(o1)
for i in e:
    print(i)
print("                                   ")

print(eval('3 * 10 + 15/3'))  # can evaluate exp in string
print("                                              ")

s4 = 'x=10\ny=20\nprint(x+y)'
exec(s4)  # executes all types of statements
print("                                  ")

o3 = [3, 6, 9, 12, 15, 18, 21, 24]
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False
f = filter(even, o3)
for i in f:
    print(i) # filters objects in function
print("                             ")

o4 = [1, 2, 3, 4, 5]
print(frozenset(o4)) # converts iterable into non modifiable frozen set
print("                                 ")

jig = "jigyasa"
print(hash(jig)) # gives hash code of obj
print("                        ")

help(jig.lower) # gives details of any method
print("                             ")

print(isinstance(jig, int)) # tells if particular obj is instance of that class
print("                              ")

jig1 = ['shukla']
jig2 = ['jigyasa']
m = map(lambda x,y:x+y, jig1,jig2 )
print(list(m))
print("                              ")
