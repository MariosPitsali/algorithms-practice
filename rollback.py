from decimal import *

class Account(object):
    
    def __init__(self, name: str, opening_balance:int = 0):
        self._balance = opening_balance
        self.name = name
        print ("Account created for {0.name}".format(self))
        self.show_balance()
    def show_balance(self):
        print ("Balance on account {0.name} is {0._balance}".format(self))
        
    def deposit(self, amount:int) ->float:
        if amount > 0.0:
            self._balance += amount
            print("{:.2f} deposited".format(amount/100))
        return self._balance
    
    def withdraw (self, amount:int) -> float:
        if  self._balance > amount > 0.0:
            self._balance -= amount
            print ("{:2f} withdrawn".format(amount/100))
            return self._balance
        else:
            print ("Amount must be more than zero and less than your account balance.")
            return self._balance
        
if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.show_balance()