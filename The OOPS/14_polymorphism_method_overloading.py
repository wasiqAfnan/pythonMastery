'''
Python does not directly support method overloading. Instead, we can emulate it by using
default arguments or variable-length arguments (*args and **kwargs).
'''

# example of method overloading using default arguments
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example usage
calc = Calculator()
print(calc.add(5))          # Adds 5 + 0 + 0 (default values)
print(calc.add(5, 10))      # Adds 5 + 10 + 0
print(calc.add(5, 10, 15))  # Adds 5 + 10 + 15

# example of method overloading using variable-length arguments
class Calculator:
    def add(self, *args):
        return sum(args)

# Example usage
calc = Calculator()
print(calc.add(5))                     # Adds 5
print(calc.add(5, 10))           # Adds 5 + 10
print(calc.add(5, 10, 15, 20))   # Adds 5 + 10 + 15 + 20


# example using kwargs
def addKwargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total+=value
    return total

print(addKwargs(a=5, b=10, c=15))  # Output: 30
print(addKwargs(a=5))  # Output: 5
print(addKwargs(a=5, b=20))  # Output: 25