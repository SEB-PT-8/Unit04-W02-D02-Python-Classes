print('Classes Lesson')

# declaring a class
class BankAccount():
    minmum_balance = 100 # minimum balance for entire class is 100

    # 1. all classes have a __init__() method
    # 2. ALL methods have first parameter self
    def __init__(self, owner_param, balance_param = 100):
        print('init function called')
        self.balance = balance_param
        self.owner = owner_param        

    def withdraw(self, withrdaw_amount):
        if withrdaw_amount > self.balance:
            print('Insufficient Funds')
            return
        self.balance -= withrdaw_amount
    
    def __str__(self):
        return f'Owner: {self.owner}, balance: {self.balance}'
    
    @classmethod
    def change_minimum_balance(self, new_minimum):
        if new_minimum < 0:
            print('error: value not positive')
            return
        self.minmum_balance = new_minimum
        


# create an object of the BankAccount class
ali_account = BankAccount('Ali',500)

omar_account = BankAccount('Omar',200 )

mohammad_account = BankAccount('Mohammad')

omar_account.withdraw(150)

print(omar_account.balance)

print(ali_account.balance)

print(mohammad_account.balance)



print(ali_account)


print(BankAccount.minmum_balance)



class Student():
    def __init__(self, name, country = 'Bahrain'):
        self.name = name
        self.country = country
    
    def introduct_self(self):
        print(f'my name is {self.name} and I am from {self.country}')



class GAEmployee():
    def __init__(self, name, fridge_code):
        self.name = name
        self.fridge_code = fridge_code
    
    def introduce_self(self):
        print(f'Hello I am {self.name} and I am GA Employee')



# Teacher inherets from GA Employee
class Teacher(GAEmployee):
    def __init__(self, name, fridge_code, courses_taught):
        super().__init__(name,fridge_code)
        self.courses_taught = courses_taught
    
    def introduce_self(self):
        print(f'Hello I am {self.name} and I teach {self.courses_taught[0]}')




omar_teacher = Teacher('Omar',101, ['SEB','Java'])


omar_teacher.introduce_self()

