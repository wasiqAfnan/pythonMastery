'''
Inheritance in Python is a feature of object-oriented programming that allows a class
(child class) to inherit properties and methods from another class (parent class).
It promotes code reuse and enables the creation of hierarchical class relationships.
'''

# syntax
'''
class ParentClass:
    # Parent class code

class ChildClass(ParentClass):
    # Child class code
'''

# example of inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog class inherits from Animal
    pass

dog = Dog()
dog.speak()  # Output: Animal speaks

# example 2
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):  # Inherits from Vehicle
    def drive(self):
        print("Car is driving")

car = Car()
car.move()  # Output: Vehicle is moving
car.drive()  # Output: Car is driving



