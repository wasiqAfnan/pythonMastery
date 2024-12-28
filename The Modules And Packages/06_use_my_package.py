# as we need to import the module which is in My_First_package package
# we need to first tell package name then module name

# Example 1
import My_First_package.math_module
print(My_First_package.math_module.pow(2, 3)) # prints 8

# Example 2
from My_First_package import math_module, string_module
print(string_module.greet(string_module.my_name)) # prints "Hello, Wasiq!"
print(math_module.pow(2, 3)) # prints 8

# Example 3
from My_First_package.math_module import my_num
print(my_num) # prints 3.14

from My_First_package.string_module import my_name as name
print(name) # prints "Wasiq"

from My_First_package.string_module import concat
print(concat("Wasiq", "Afnan")) # prints "Wasiq Afnan"
