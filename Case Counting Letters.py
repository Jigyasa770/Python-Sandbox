def count(string):
    up = 0
    low = 0
    for i in string:
        if 65 <= ord(i) <=90:
            up += 1
        elif 97 <= ord(i) <=122:
            low += 1
    return up, low
b = count('IJHASYamdnsaas')
print(b)

def count1(string):
    lower = 0
    upper = 0
    for l in string:
        if l.islower():
            lower += 1
        elif l.isupper():
            upper += 1
    return lower, upper
b1 = count1('IJHASYamdnsaas')
print(b1)