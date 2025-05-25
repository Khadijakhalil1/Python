class Acount:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def debit(self, amount):
        self.balance-=amount
        print("you  debit   RS =",amount,"amount")
        print("Total balance is =",self.get_balance())

    def  credit(self,amount):
        self.balance+=amount
        print("you credit     RS =",amount,"amount")
        print("Total Balance is  = ",self.get_balance())

    def get_balance(self):
        return self.balance    


a1 = Acount(3344,207230)
a1.debit(200)
a1.credit(500)
a1.get_balance()
print(a1.account)
print(a1.balance)