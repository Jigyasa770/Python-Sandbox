d1 = {'abacus': 'a calculator', 'a bachelor': 'unmarried person', 'cable': 'strong rope'}
print(d1['abacus'])
print("                ")
d2 = {101: 'John', 102: 'Smith', 103: 'Mark', 104: 'David'}
print(d2[101])
print("                ")

d2[103] = 'Mathew'
d2[105] = 'Ajay'
del d2[104]
for i in d2:
    print(i)
print("                ")

for i in d2:
    print(i, d2[i])
print("                ")

print(d2)
print("                ")

#Dictionary Comprehension
d3 = dict()
d3['apple'] = 'red'
d3['mango'] = 'yellow'
for x in range(1, 6):
    d3[x] = x**2
d4 = dict(((1, 2), (2, 3), (4, 5), (6, 5), (7, 4)))
L1 = ['hello', 'bonjour', 'namaste']
S1 = {1, 2, 3}
d5 = dict(zip(S1, L1))
d6 = dict(enumerate(L1))
d7 = {x: x**2 for x in S1}
d8 = dict((x, x + 1) for x in S1)
d9 = dict((x, y) for x,y in zip(S1, L1))
d10 = {x:y for x, y in enumerate(L1)}
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8)
print(d9)
print(d10)
print("                ")

#Looping Over Dictionary
d11 = {101: 'PRODUCTION', 102: 'ACCOUNTS', 103: 'SALES AND MARKETING', 104: 'INVENTORY'}
for x in d11:
    print(x, d11[x])
for x in d11:
    print(x, d11.get(x))
print(d11.get(106, 'Invalid Key'))  #if value is found it will return that value but if value is not found it will return invalid key
print(d11.keys())
print(d11.values())
print(d11.items())
for k in d11.keys():
    print(k, d11[k])
for v in d11.values():
    print(v)
for x, y in d11.items():
    print(x, y)
print("                ")

#Dictionary Methods
d12 = d11.copy()
d13 = {105: 'DESIGNING', 106: 'INVENTORY'}
d12.update(d13)
d12.setdefault(108, 'POLICE')
L2 = [11, 22, 33, 44, 55]
d14 = {}
d14 = d14.fromkeys(L2, 'hi')
d14.pop(11)
d14.popitem()
d15 = d14.fromkeys(L2, 'hi')
d15.clear()
print(d14.pop(66, 'None'))
print(d12)
print(d14)
print(d15)
