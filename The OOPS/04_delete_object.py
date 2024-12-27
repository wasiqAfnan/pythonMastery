# we can delete an object by using the del keyword
# also we can delete an attribute by using del

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

del obj1

# below 2 lines will raise name error as we deleted the object
# print(obj1.name)
# print(obj1.age)

# Example 2
class employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def print_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}")

# creating an object
emp1 = employee("Wasiq", 1234, 100000)
emp1.print_info()

del emp1.salary

print(emp1.name)
print(emp1.id)
print(emp1.salary) # this will raise AttributeError as we deleted the attribute