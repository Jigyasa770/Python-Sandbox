class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, a, b):
        return a + b

    def __sub__(self, a, b):
        if a < b:
            return a - b
        else:
            return b - a

    def __mul__(self, a, b):
        return a * b

    def __divmod__(self, a, b):
        return a // b
a = Calculator(10, 5)
print(a.__mul__(10, 5))
