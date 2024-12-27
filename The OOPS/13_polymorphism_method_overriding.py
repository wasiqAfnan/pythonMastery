# Definition: A child class provides a specific implementation of a method
# that is already defined in its parent class.

class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")  # Overriding the parent method

child = Child()
child.show()  # Output: Child class method