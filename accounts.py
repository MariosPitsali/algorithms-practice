import datetime
import pytz

class Account:
    """Simple account class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list=[(Account._current_time(),balance)]
        print ("Account created for {}".format(self.name))
        
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            
    def withdraw(self, amount):
        if  self.balance >= amount > 0 :
            self.balance -= amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), -amount))
        else:
            print("Cannot withdraw amount larger than your existing balance!")
        
    def show_balance(self):
        print ("Balance is: " + str(self.balance))
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0 :
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print ("{:5} was {} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    new_account = Account("Marios Pitsalidis", 140.80)
    new_account.deposit(56.00)
    new_account.withdraw(24.80)
    new_account.withdraw(89990)
    new_account.show_transactions()
    
    georgia = Account("Georgia Idunno", 870.91)
    georgia.deposit(89.0)
    georgia.withdraw(679.4)
    georgia.show_transactions()
    print(georgia.__dict__)