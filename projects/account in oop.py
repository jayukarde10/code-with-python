class account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,ammount):
        self.balance-=ammount
        print("ammount debited",self.balance)
    def credit(self,ammount):
        self.balance+=ammount
        print("ammount credited",self.balance)
    def balance1(self):
        print("balance is",self.balance)
a1=account(2000,26598)
a1.debit(1000)
a1.credit(2000)
a1.balance1()
