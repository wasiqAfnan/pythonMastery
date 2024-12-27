# Single Inheritance: A child class inherits from one parent class.
# example to demonstrate single inheritance
class employee:
    def __init__(self, id, name): # constructor
        self.id = id
        self.name = name

    # function to display details about employee
    def display(self):
        print(f"{self.name} has an id {self.id}")

class hr(employee): # hr class inheriting from employee class
    def display2(self):
        print("Hello, this is a function under hr class")

# main
# creating object of hr class
# as hr inherits from employee we can use constructor of parent class
obj = hr(101,"wasiq")
obj.display() # calling function from parent class
obj.display2() # calling function from hr class
