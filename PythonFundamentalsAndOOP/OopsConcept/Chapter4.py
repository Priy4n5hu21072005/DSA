# Polymorphism
# Method Overridding
class Animal:
    def sound(self):
        print("animal sounds")
class Dog(Animal):
    def sound(self):
        print("Bark!")
class Cat(Animal):
    def sound(self):
        print("Meow!")
d=Dog()
c=Cat()
d.sound()
c.sound()
# Duck Typing
def make_sound(animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())