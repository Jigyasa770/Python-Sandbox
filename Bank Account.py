class Account:
    AccNumber = 1001
    def __init__(self, name, balance=1000):
        if balance < 1000:
            raise MinimumBalanceError('Account cannot be created')

        self.name = name
        self.account_number = self.AccNumber
        self.balance = balance
        self.AccNumber += 1
    def deposit(self, amt):
        self.balance += amt
    def withdraw(self, amt):
        if self.balance - amt < 1000:
            raise MinimumBalanceError('Amount cannot be withdrawn')
        self.balance -= amt
    def show_details(self):
        print('Account Number: ', self.account_number)
        print('Name: ', self.name)
        print('Balance: ', self.balance)

a1 = Account('John', 10000)
(a1.deposit(10000))
(a1.withdraw(5000))
print(a1.show_details())

