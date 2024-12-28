'''
The concept of calling the parent class constructor or method from a subclass in Python
is part of Inheritance. Specifically, using the class name directly
(like Parent.__init__(self, name, age)) is sometimes referred to as explicit inheritance or
explicit method invocation.

When you use super(), it is often called implicit method resolution or implicit inheritance.
super() is a mechanism in Python that handles multiple inheritance more efficiently,
ensuring the correct method is called according to the Method Resolution Order (MRO).
'''

# example  of implicit inheritance
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)


class Child(Parent):
    def __init__(self, name, age, city):
        super().__init__(name, age) # calling parent class constructor using super() method
        self.city = city

    def print_city(self):
        print(self.city)


obj1 = Child("Wasiq", 25, "Kolkata")
obj1.print_name()
obj1.print_city()