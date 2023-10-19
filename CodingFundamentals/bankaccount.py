#class Bank_Account:
#    def __init__(self):
#        self.balance=1000
 
#    def deposit(self):
#        amount=float(input("Enter amount to be Deposited: "))
#        self.balance += amount
#        print("Amount Deposited:",amount)
 
#    def withdraw(self):
#        amount = float(input("Enter amount to be Withdrawn: "))
#        if self.balance>=amount:
#            self.balance-=amount
#            print("You have withdrawn:", amount)
#        else:
#            print("Not enough funds")
 
#    def display(self):
#        print("Available Balance=",self.balance)
 
#money = Bank_Account()
   
#print("Hello would you like to deposit or withdraw today")
#userinput = input("Enter Deposit or Withdraw")
#if userinput == "deposit" or "Deposit":
#    money.deposit()
#    money.display()
#elif userinput == "withdraw" or "Withdraw":
#    money.withdraw()
#    money.display()
#else: 
#    print("invalid choice please try again")

class Bankaccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount

    def get_balance(self):
        return f"£{self.balance}"
    
acct = Bankaccount("1234")

acct.deposit(1000)
print(acct.get_balance())
acct.withdraw(50)
print(acct.get_balance())
acct.withdraw(1500)