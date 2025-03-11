# 6.Write a Python class BankAccount with attributes like account_number, balance, 
# date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self,amount):
       
        if amount > 0:
            self.balance = self.balance + amount

            print("deposit Rs :",amount)
            print("New balance is :",self.balance)
        else:
            print("Invalid deposit balance")    




    def withdraw(self,amount):
        if amount > 0 and amount<=self.balance:
            self.balance = self.balance - amount

            print("withdrao Rs :",amount)
            print("New balance is :",self.balance)
        else:
            print("Insufficient balance") 
       


    def check_balance(self):
       return self.balance    

        
B = BankAccount(266377183,0,"25/3/25","Manisha")
# print(B.__dict__)
B.deposit(-1000)

B.withdraw(500)

print(B.balance)
