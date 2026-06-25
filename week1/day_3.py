#### My First class ####
'''class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def introduce(self,name,age):
       return f"Hi i am {self.name} and my age is {self.age} year old"
s1 = Student("Nithin",23)
s2 = Student("Vinod", 26)

print(s1.introduce("Nithin",23))
print(s2.introduce("Vinod", 26))'''

#### Instance Variable VS Class Variable ####
'''class Student:
    school = "AP Model school" # Class variable
    count = 0 
    def __init__(self,name,marks):
        self.name = name # Instance variable
        self.marks = marks 
        Student.count += 1 
    
s1 = Student("Nithin", 95)
s2 = Student("Vinod", 99)
s3 = Student("Ninja", 80)

print(Student.count)
print(s1.school)
print(s2.school)
print(s1.name)
print(s2.name)

school = "ZP High school"
print(s1.school)'''

#### Instance Method, Class Method and Static Method
'''class Student:
    school = "AP Model school" # Class Variable
    count = 0 
    def __init__(self,name,marks):
        self.name = name # Instance Variable
        self.marks = marks 
    
    # Instance method
    def student_pass(self):
        if self.marks >= 60:
            return f"{self.marks} is passed"
        return f"{self.marks} is passed"
    
    # Class method 
    @classmethod
    def get_school(cls):
        return cls.school 
    
    # Static method 
    @staticmethod
    def passs(marks):
        return marks >= 75 

s1 = Student("Nithin", 90)
s2 = Student("Vinod", 95)

print(s1.student_pass())
print(s2.student_pass())

print(Student.get_school())

print(Student.passs(90))
print(Student.passs(50))'''

'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Student({self.name}, {self.marks})"

s1 = Student("Ali", 88)
print(s1)'''

#### Building a BankAccount
class BankAccount:
    bank_name = "AI Bank"
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return f"BankAccount(owner={self.name}, balance={self._balance})" 
    
    def __eq__(self, other):
        return self._balance == other._balance
    
    def __lt__(self, other):
        return self._balance < other._balance
    
    def deposit(self,amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")     

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"withdrew {amount}. New balance: {self._balance}")
        else:
            print(f"insufficient funds. Current balance: {self._balance}")

    def get_balance(self):
        print(f"Current balance: {self._balance}")

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest 
        print(f"Interest added: {interest}, New balance: {self._balance}")
    
    def account_info(self):
        return f"SavingsAccount - {self.name}: balance={self._balance}, rate={self.interest_rate*100}%"
    
class LoanAccount(BankAccount):
    def __init__(self, name, balance=0, loan_amount=0):
        super().__init__(name, balance)
        self.loan_amount = loan_amount 
    
    def account_info(self):
        return f"LoanAmount - {self.name}: balance={self._balance}, owes {self.loan_amount}"
    
    def repay(self, amount):
        if amount <= self.loan_amount:
            self.loan_amount -= amount
            print(f"Repaid {amount}. Remaining loan: {self.loan_amount}")
        else:
            print(f"Repay amount exceeds loan. Remaining loan: {self.loan_amount}")

s = SavingsAccount("Ali", 2000)
l = LoanAccount("Sara", 500, loan_amount=10000)

s.deposit(1000)
s.add_interest()
print(s.account_info())

l.repay(2000)
print(l.account_info())

account = [
    SavingsAccount("Ali", 2000),
    BankAccount("Zara", 500),
    LoanAccount("Bilal", 5000, 8000),
]

for acc in sorted(account):
    print(acc)




# acc1 = BankAccount("Ali", 1000)
# acc2 = BankAccount("Sara")

# acc1.deposit(500)
# acc1.withdraw(200)
# acc1.withdraw(2000)
# acc1.get_balance()

# print(acc1)
# print(acc2)
# print(BankAccount.bank_name)

