# importing my own module
import my_module

# calling functions from my own module
result = my_module.add(10, 20)
print(result) # prints 30

result = my_module.subtract(10, 20)
print(result) # prints -10

result = my_module.greet(my_module.my_name)
print(result) # prints "Hello, Wasiq!"

# importing all functions from my own module
from my_module import *

result = add(10, 20)
print(result) # prints 30

result = subtract(10, 20)
print(result) # prints -10

result = greet(my_name)
print(result) # prints "Hello, Wasiq!"

# improving specific functions from my own module
from my_module import add, subtract
add(10, 20) # prints 30
subtract(10, 20) # prints -10
