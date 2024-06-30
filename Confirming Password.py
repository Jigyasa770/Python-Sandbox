a = input('Enter password: ')
b = input('Enter password again: ')
c = a.casefold()
d = b.casefold()
if a == b:
    print("Correct password")
elif c == d:
    print("Check Cases")
else:
    print("Password's do not match")