class Student:
    # Constructor 
    def __init__(self,name,age):
        # Global Variables 
        self.name=name
        self.age=age
        # Method
    def display(self):
        print(self.name,self.age)
# Object 
s1 = Student("Priyanshu",21)
# Calling Method
s1.display()
        
# Encapsulation
class BankBalance:
    def __init__(self):
        self.BankBalance=1000
    def getBalance(self):
        return self.BankBalance
obj = BankBalance()
print(obj.getBalance())


