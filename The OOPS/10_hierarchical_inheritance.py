# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

class Parent:
    def show(self):
        print("Parent class method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

child1 = Child1()
child1.show()  # Output: Parent class method

child2 = Child2()
child2.show()  # Output: Parent class method
