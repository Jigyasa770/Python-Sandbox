s1 = input('Enter string : ')
low = ''
up = ''
for x in s1:
    if x.islower():
        low += x
    else:
        up += x

s2 = low + up
print(s2)