# Multiple Inheritance: A child class inherits from two parent classes.
# example to demonstrate multiple inheritance

class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2): # child class inheriting from both parent class parent1 and parent2
    pass

child = Child() # creating object of child class
child.method1()  # Output: Method from Parent1
child.method2()  # Output: Method from Parent2
