print('Classes Lesson')

# declaring a class
class BankAccount():
    # 1. all classes have a __init__() method
    # 2. ALL methods have first parameter self
    def __init__(self, balance_param, owner_param):
        print('init function called')
        self.balance = balance_param
        self.owner = owner_param

    def withdraw(self, withrdaw_amount):
        self.balance -= withrdaw_amount
        


# create an object of the BankAccount class
ali_account = BankAccount(500, 'Ali')

omar_account = BankAccount(200, 'Omar' )

omar_account.withdraw(150)

print(omar_account.balance)

print(ali_account.balance)

