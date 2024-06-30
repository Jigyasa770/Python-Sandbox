'''length of string'''
s1 ='hello'
print(len(s1))

'''printing chars in string'''
for x in s1:
    print(x)

'''multiline string'''
s2 = '''Hello
How are you'''
print(s2)

'''Concatenation'''
s3 ='Hello'
s4 = ' World'
s5 = s3 + s4
s6 = 'Hello' ' 15'
print(s5)
print(s6)

'''Repetition'''
s7 ='hi '
print(s7 * 7)

'''Indexing'''
s8 = 'Hello World'
print(s8[4])
print(s8[7])
print(s8[-5])
for i in range(0,len(s8)):
    print(s8[i])

'''Slicing'''
s9 = 'Hello World'
print(s9[3:10:1])

'''in and not in'''
print(('me' not in s9))
print(('h' in s9))
print(('Hello' in s9))

'''starts with and ends with'''
s10 = 'python is very easy'
print(s10.startswith('python'))
print(s10.startswith('py'))
print(s10.startswith('thon'))
print(s10.startswith('is',7))
print(s10.startswith('v',7,11))
print(s10.endswith('python'))
print(s10.endswith('easy'))
print(s10.endswith('ry',12))
print(s10.endswith('ry',12,7))




