'''
A module in Python is a file containing Python code (functions, classes, or variables)
that can be reused in other programs. Python provides a wide variety of built-in modules
(e.g., math, os, random) and allows you to create your own modules.
'''

# importing a module in Python
import math
print(math.pi) # prints the value of pi
print(math.sqrt(25)) # prints the square root of 25

# importing a module and using its functions
from math import sqrt, sin, cos
print(sqrt(25)) # prints the square root of 25
print(sin(math.pi/2)) # prints the sine of pi/2
print(cos(math.pi)) # prints the cosine of pi

# importing a module and using its variables
from math import pi
print(pi) # prints the value of pi

# importing all functions from a module
from math import *
print(pi) # prints the value of pi
print(sqrt(25)) # prints the square root of 25
print(sin(pi/2)) # prints the sine of pi/2
print(cos(pi)) # prints the cosine of pi

# importing a module using alias
import math as m
print(m.pi) # prints the value of pi

# importing a fucntion from module using alias
from math import sqrt as s
print(s(25)) # prints the square root of 25
