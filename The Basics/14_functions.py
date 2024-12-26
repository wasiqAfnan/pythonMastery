# basic function
def greet(name):
    print("Hello", name)

greet("Wasiq")

# function with parameters
def greet(name, age):
    print("Hello", name, "your age is", age)

greet("Wasiq", 25)

# function with default parameters
def greet(name, age=25):
    print("Hello", name, "your age is", age)

greet("Wasiq")

# function with multiple parameters
def greet(name, age, city):
    print("Hello", name, "your age is", age, "from", city)

greet("Wasiq", 25, "Kolkata")

# function returning a value
def add(x, y):
    return x + y

result = add(5, 10)
print(result)

# function with multiple return values
def divide(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

quotient, remainder = divide(10, 3)
print(quotient, remainder)  # Output: 3 1


# recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120


# function with variable number of arguments
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum(1, 2, 3, 4, 5)
print(result)  # Output: 15

# function with keyword arguments
def greet(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

greet(name="Wasiq", age=25, city="Kolkata")

# function having both args and kwargs
def greet(*args, **kwargs):
    print("Printing args")
    for arg in args:
        print(arg)

    print("Printing kwargs")
    for key, value in kwargs.items():
        print(key, ":", value)

greet(10,20,30, name="Wasiq", age=25, city="Kolkata")