"""
BANK ACCOUNT: For this challenge, create a bank account class that has two attributes:

    owner
    balance

and two methods:

    deposit
    withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class bank:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, value):
        self.value = value
        self.balance += value
        return print("Deposited: {}. Your current funds are: {}".format(value, self.balance))
    
    def withdraw(self, value):
        self.value = value
        if self.balance < value:
            return print("Insufficient funds on Your account. Your current funds are: {}".format(self.balance))
        else:
            self.balance -= value
            return print("Withdrew: {}. Your current funds are: {}".format(value, self.balance))
