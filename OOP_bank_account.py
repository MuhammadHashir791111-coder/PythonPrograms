class Account:
    def __init__(self,bal,accno):
        self.balance = bal
        self.accountno = accno

    #Debit method
    def debit(self,amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print(f"Remaining balance : {self.balance}")

    #Credit method
    def credit(self,amount):
            self.balance += amount
            print(f"Rs. {amount} was credited")
            print(f"Current balance : {self.balance}")

    def checkbal(self):
        return self.balance


acc1 = Account(10000,12345)
print(acc1.checkbal())

acc1.debit(5000)
print(acc1.checkbal())

acc1.credit(50000)
print(acc1.checkbal())