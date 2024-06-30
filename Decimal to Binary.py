a = int(input("Enter a number: "))
binary = ''

while a > 0:
    r = a % 2
    a = a // 2
    binary = str(r) + binary

print(binary)