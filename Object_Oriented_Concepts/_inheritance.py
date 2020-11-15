from itertools import count


class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print('Parent.Apple', self.value)

    def google(self):
        print('Parent.Google')
        self.apple()


class Child1(Parent):
    def yahoo(self):        # Completely Independent Method
        print('Child1.Yahoo')


class Child2(Parent):
    def apple(self):        # Overriding Parent class Method
        print('Child2.Apple', self.value)


class Child3(Parent):
    def apple(self):        # Overriding Parent class Method but reusing the original method in Parent
        print('Child2.Apple')
        super().apple()


class Child4(Parent):
    def __init__(self, value, extra):   # Adding a new Attribute
        self.extra_value = extra
        super().__init__(value)


class Parent2:
    def facebook(self):
        print('Parent2.Facebook')


class Child5(Parent, Parent2):  # Child Inheriting from more than one parent
    pass


# Method Resolution Order - MRO
c = Child5(10)
print(c.__class__.__mro__)


# Calculating Payroll of different Employees
class Employee:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name


class WeeklyEmployee(Employee):
    def __init__(self, _id, name, weekly_salary):
        self.weekly_salary = weekly_salary
        super().__init__(_id, name)

    def calculate_pay(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, _id, name, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        super().__init__(_id, name)

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate


class CommisionedEmployee(WeeklyEmployee):
    def __init__(self, _id, name, weekly_salary, commision):
        self.commision = commision
        super().__init__(_id, name, weekly_salary)

    def calculate_pay(self):
        fixed_pay = super().calculate_pay()
        return fixed_pay + self.commision


# Function that calculates the pay of all Employees
def calculate_payroll(employess):
    print('Calculating Payroll')
    for employee in employess:
        print(f'Pay for {employee._id}, {employee.name} = {employee.calculate_pay()}')


e1 = HourlyEmployee('1', 'steve', 40, 20)
e2 = WeeklyEmployee('2', 'Bill', 1250)
e3 = CommisionedEmployee('3', 'John', 1250, 100)
calculate_payroll([e1, e2, e3])

from itertools import count


class BankAccount:
    c = count(start=1)  # To Generate Account Numbers
    __accounts = []  # List to keep track of all the accounts
    interest_rate = 4.0

    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.amount = float(amount)
        self._account_no = str(next(self.c)).zfill(9)
        BankAccount.__accounts.append(self)

    def deposit(self, amount):
        self.amount += float(amount)

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount

    def statement(self):
        print(f"Available Account Balance: {self.amount}")

    def roi(self):
        self.amount = self.amount + self.amount * (self.interest_rate / 100)


class SavingsAccount(BankAccount):
    interest_rate = 4.0

    def withdraw(self, amount):
        if amount > 10000:
            raise ValueError('Can not withdrwa more than 10000 per day')
        super().withdraw(amount)


class SeniorCitizenAccount(BankAccount):
    interest_rate = 5.5

    def withdraw(self, amount):
        if amount > 20000:
            raise ValueError('Can not withdrwa more than 20000 per day')
        super().withdraw(amount)


class SukanyaSamrudhiAccount(BankAccount):
    interest_rate = 9.5

    def deposit(self, amount):
        if amount < 1000:
            raise ValueError('Min Amount Should be 1000rs')
        super().deposit(amount)

    # Completely overriding the parent class method "withdraw"
    def withdraw(self, amount):
        raise Exception("Can not withdraw")


class SalaryAccount(BankAccount):
    def __init__(self, fname, lname, amount):
        self._count = 0
        super().__init__(fname, lname, amount)

    def deposit(self, amount):  # Add A/C opening Bonus of 1000rs
        self._count += 1
        if self._count == 1:
            self.amount += 1000
        super().deposit(amount)


class LongTermSavings:
    def withdraw(self, amount):
        self.amount -= 500  # Penalty for withdrawing from PensionAccount
        super().withdraw(amount)


class RetirementAccount(LongTermSavings, BankAccount):
    pass