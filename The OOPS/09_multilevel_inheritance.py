# Multilevel Inheritance: A child class inherits from a parent class,
# and another class inherits from the child class.

# example to demonstrate multilevel inheritance
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent): # parent class inheriting from grandparent class
    def greet2(self):
        print("Hello from Parent")

class Child(Parent): # child class inheriting from parent class
    def greet3(self):
        print("Hello from Child")

child = Child()
child.greet()  # Output: Hello from Grandparent
child.greet2()  # Output: Hello from Parent
child.greet3()  # Output: Hello from Child
