birthday = {
    'SACHIN': '3/14/2003',
    'CARL': '1/17/2001',
    'KHAN': '12/10/2006',
    'DONALD': '6/14/2010',
    'ROHAN': '1/6/2005'}

name = input("Enter the name: ")

if name in birthday:
    print(birthday[name])
else:
    print('Name not in dictionary')
