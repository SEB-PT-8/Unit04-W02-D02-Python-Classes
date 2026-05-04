print('Classes Lesson')

# declaring a class
class BankAccount():
    # 1. all classes have a __init__() method
    # 2. ALL methods have first parameter self
    def __init__(self, owner_param, balance_param = 100):
        print('init function called')
        self.balance = balance_param
        self.owner = owner_param

    def withdraw(self, withrdaw_amount):
        self.balance -= withrdaw_amount
        


# create an object of the BankAccount class
ali_account = BankAccount('Ali',500)

omar_account = BankAccount('Omar',200 )

mohammad_account = BankAccount('Mohammad')

omar_account.withdraw(150)

print(omar_account.balance)

print(ali_account.balance)

print(mohammad_account.balance)


