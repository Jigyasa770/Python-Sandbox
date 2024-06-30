n = int(input("Enter number of terms: "))
a = int(input("Enter first term: "))
b = int(input("Enter second term: "))
for t in range (n):
    print(a)
    c = a + b
    a = b
    b = c
