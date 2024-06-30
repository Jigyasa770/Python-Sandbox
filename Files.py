""" Accessing file """
file = open('MyData.txt', 'r')
str1 = file.read()
print(str1)
file.close()

"""Modes of Opening a File"""
file = open('ModeDemo.txt', 'w') # WRITE
file.write('Hello\n')
file.write('How are you?\n')
file.close()

file = open('ModeDemo.txt', 'a') # APPEND
file.write('Iam learning python\n')
file.write('It is fun and good to learn.\n')
file.close()

file = open('ModeDemo.txt', 'r+') # READ + WRITE
str1 = file.read()
print(str1)
file.write('Goodbye\n')
file.write('Darkness my old friend\n')
file.close()

file = open('ModeDemo.txt', 'w+') # WRITE + READ
str1 = file.read()
print(str1)
file.write('bleh bleh\n')
file.close()

"""Properties of files"""
file = open('MyData.txt', 'r')
file.close()
print(file.mode)
print(file.name)
print(file.closed)
