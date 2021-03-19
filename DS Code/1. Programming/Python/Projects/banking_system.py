"""

Banking System using OOP:
==> Holds details about a user
==> Has a function to show user details
==> Child class : Bank
==> Stores details about the account balance
==> Stores details about the amount
==> Allows for deposits, withdrawals, and view balance

"""


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details\n")
        print("Name ", self.name)
        print("Age", self.age)
        print("Gender", self.gender)


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated: $", self.balance)

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient Funds | Balance Available: $", self.balance)
        else:
            self.balance -= amount
            print("Account balance has been updated: $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Balance available: $", self.balance)