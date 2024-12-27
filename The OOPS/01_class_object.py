'''
A class in Python is a blueprint or template for creating objects.
It defines the attributes (data) and methods (functions) that objects of the class will have.
Classes are defined using the class keyword.

An object is an instance of a class. It represents a specific entity created based on the
blueprint provided by the class, containing actual data and being able to use the class's
methods.
'''

# creating a class
class myFirstClass:
    # attributes
    name = "Wasiq Afnan"
    age = 25

    # method
    # self keyword is important in methods as it refers to the object itself
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating an object
obj1 = myFirstClass()
obj1.print_info()

#creating another object
obj2 = myFirstClass()
obj2.print_info()
