'''
In Python, the self keyword is used to refer to the instance of the class.
When a method is called on an object, the object is automatically passed as the first argument.
This allows the method to access the object's attributes and methods.
'''

class number:
    name = "Wasiq"
    age = 25

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating an object
obj1 = number("Wasiq", 25)
obj1.print_info()
