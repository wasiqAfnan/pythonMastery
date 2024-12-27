'''
Inheritance in Python is a feature of object-oriented programming that allows a class
(child class) to inherit properties and methods from another class (parent class).
It promotes code reuse and enables the creation of hierarchical class relationships.
'''

# example of inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog class inherits from Animal
    pass

dog = Dog()
dog.speak()  # Output: Animal speaks


