'''
The concept of calling the parent class constructor or method from a subclass in Python
is part of Inheritance. Specifically, using the class name directly
(like Parent.__init__(self, name, age)) is sometimes referred to as explicit inheritance or
explicit method invocation.
'''

# example  of explicit inheritance
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)


class Child(Parent):
    def __init__(self, name, age, city):
        Parent.__init__(self, name, age) # calling parent class constructor using parent class name
        self.city = city

    def print_city(self):
        print(self.city)


obj1 = Child("Wasiq", 25, "Kolkata")
obj1.print_name()
obj1.print_city()