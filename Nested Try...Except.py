try:
    a = int(input('Enter No1: '))
    try:
        b = int(input('Enter No2: '))
        try:
            c = a // b
            print(c)
        except ZeroDivisionError as e:
            print(e)
    except ValueError as e:
        print(e)
except ValueError:
    print('Value Error')