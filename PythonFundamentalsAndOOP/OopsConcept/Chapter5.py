# Access Modifier
# Public Member
class Student:
    def __init__(self):
        self.name="Priyanshu"
s=Student()
print(s.name)

# Protected Member
class Family:
    def __init__(self):
        self._name="Priyanshu"
class Parent(Family):
    def display(self):
        print(self._name)
s=Parent()
s.display()

# Private Member
class Family:
    def __init__(self):
        self.__name="Priyanshu"
s=Family()
print(s._Family__name)