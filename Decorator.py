def decorator(fun):
    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)
    return wrapper
@decorator #modifies the function and decorates them
def display(msg):
    print(msg)

#d = decorator(display) # represents wrapper which displays function
display('Hello bbg')