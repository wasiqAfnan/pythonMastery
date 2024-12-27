'''
class constructor is a special method that is automatically called when an object is created.
It is used to initialize the object's attributes.
'''

class number:
    # constructor is declare using __init__ method
    def __init__(self, num):
        self.num = num

    # alternative way to declare constructor
    def number(self, num):
        self.num = num

    # normal method
    def print_num(self):
        print(self.num)

    def add(self, num):
        self.num += num

obj1 = number(10)
obj1.print_num()
obj1.add(5)
obj1.print_num()