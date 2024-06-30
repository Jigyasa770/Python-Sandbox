def Closure():
    msg = 'Hello'
    def display():
        print('*' * 10)
        print(msg * 10)
        print('*' * 10)
    return display
d = Closure()
d()