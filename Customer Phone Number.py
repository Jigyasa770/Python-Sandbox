class Customer:
    def __init__(self, name, phoneno):
        self.name = name
        self.phoneno = phoneno
    def get_name(self):
        return self.name
    def get_phoneno(self):
        return self.phoneno
    def set_phoneno(self, ph):
        self.phoneno = ph
a = Customer('John', 9811327590)
print(a.get_name())
print(a.get_phoneno())
a.set_phoneno(9711117590)
print(a.get_phoneno())