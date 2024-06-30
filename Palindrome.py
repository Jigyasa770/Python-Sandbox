a = int(input("Enter a number: "))
b = a
rev = 0
while a > 0:
    r = a % 10
    a = a // 10
    rev = rev * 10 + r

if rev == b:
    print("Is palindrome")
else:
    print("Is not palindrome")