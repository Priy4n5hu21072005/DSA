# Single Inheritance
class Father:
    def running(self):
        print("Father is Running")
class Son(Father):
    def Jogging(self):
        print("Son is Jogging")
#Multiple Inheritance
class Daughter(Son,Father):
    def Cycling(self):
        print("Daughter is cycling")
c=Daughter()
c.running()
c.Jogging()
c.Cycling()

# Abstraction 
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car is start")
c=Car()
c.start()