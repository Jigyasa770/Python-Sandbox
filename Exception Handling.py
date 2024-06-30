#Exception Handling
L = [10, 20, 30, 40, 50]
try:
    index = int(input('Enter the Index: '))
    print(L[index])
    print('End of try block')
except:
    print('Invalid index')
print('Terminated Gracefully')
print("                                 ")

#Handling Multiple exceptions
L1 = [10, 20, 30, 40, 50]
try:
    index1 = int(input('Enter the Index: '))
    print(L1[index1])
    print('End of try block')
except IndexError as msg:
    print('Invalid index', msg) # gives desc of exception as message
except ValueError:
    print('Enter only int value')
print('Terminated Gracefully')
print("                                            ")

#Why Try and Except
def div(a,b):
    if b != 0:
        c = a // b
        return c
    else:
        raise ZeroDivisionError
a = int(input('Enter NO1: '))
b= int(input('Enter NO2: '))
try:
    c = a // b
    print(c)
except ZeroDivisionError as msg:
    print('Zero Division Error: ', msg)
print("                                            ")

#try...except...else...finally
print('BEFORE TRY')
try:
    a = int(input('Enter numerator: '))
    b = int(input('Enter denominator: '))
    c = a // b
    print('Try block executed')
except ZeroDivisionError as err:
    print(err)
else:
    print('Division is: ', c)
finally:
    print('Finally Block')
