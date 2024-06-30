a = int(input("Enter a number: "))
rev = 0
while a > 0:
    r = a % 10
    a = a // 10
    rev = rev * 10 + r

print("The reversed number is ", rev)
