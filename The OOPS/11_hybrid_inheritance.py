# Hybrid Inheritance: A combination of two or more types of inheritance.

class Parent:
    def display(self):
        print("Parent class method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Grandchild(Child1, Child2):  # Inherits from both Child1 and Child2
    pass

grandchild = Grandchild()
grandchild.display()  # Output: Parent class method
