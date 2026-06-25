#### Inheritance - child gets everything from parent ####
'''class BankAccount:
    bank_name = "AI Bank"
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance 
        
    def deposit(self,amount):
        self.balance += amount 
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount 
            print(f"withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")

    def get_balance(self):
        print(f"Current balance: {self.balance}")

    def __str__(self):
        return f"BankAccount owner={self.name}, balance={self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate 
    
    def add_interest(self):
        interest = self.balance * self.interest_rate 
        self.balance += interest 
        print(f"Interest added: {interest}. New balance: {self.balance}")

s = SavingsAccount("Ali", 1000)
s.deposit(500)
s.withdraw(200)
s.add_interest()
print(s)'''



#### Polymorphism - same method name, different behavior ####
'''class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name 
        self.balance = balance 
    def account_info(self):
        return f"Basic account - {self.name}: {self.balance}"
    
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate 
    
    def account_info(self):
        return f"Savings account - {self.name}: {self.balance} @ {self.interest_rate*100}% interest"
    
class LoanAccount(BankAccount):
    def __init__(self, name, balance=0, loan_amount=0):
        super().__init__(name, balance)
        self.loan_amount = loan_amount 
    
    def account_info(self):
        return f"Loan Account - {self.name}: owes {self.loan_amount}"
    
account = [
    BankAccount("Ali", 1000),
    SavingsAccount("Sara", 2000, 0.08),
    LoanAccount("Bilal", 500, 15000),
]
for acc in account:
    print(acc.account_info())'''




#### Encapsulation - protecting data ####
'''class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance # -- makes it private 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance # controlled access
    
acc = BankAccount("Ali", 1000)
acc.deposit(500)
print(acc.get_balance())

# print(acc.__balance)
print(acc.name)'''

#### Dunder methods - Python's magic ####
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name 
        self.balance = balance 
    
    def __str__(self):      # print(acc) -> readable string
        return f"BankAccount ({self.name}, {self.balance})"
    
    def __repr__(self):     # repr(acc) -> developer string, for debugging
        return f"BankAccount(name='{self.name}', balance={self.balance})"
    
    def __len__(self):      # len(acc) -> return something meaningful
        return self.balance 
    
    def __eq__(self, other):
        return self.balance == other.balance 
    
    def __lt__(self, other):
        return self.balance < other.balance 
    
    def __add__(self, other):
        return self.balance + other.balance

acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Sara", 2000)
acc3 = BankAccount("Bilal", 1000)

print(acc1)
print(repr(acc1))
print(len(acc1))
print(acc1 == acc3)
print(acc1 == acc2)
print(acc1 < acc2)
print(acc1 + acc2)
accounts = [acc2, acc1, acc3]
ranked = sorted(accounts)
for a in ranked:
    print(a)