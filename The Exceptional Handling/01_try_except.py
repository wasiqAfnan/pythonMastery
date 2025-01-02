'''
Exception Handling is a mechanism in Python to handle runtime errors gracefully without
halting the execution of the program. Python provides the try-except block to handle exceptions.

- try block: Code that might raise an exception is placed here.
- except block: Handles the exception if it occurs.
- else block (optional): Executes if no exception occurs in the try block.
- finally block (optional): Executes no matter what, used for cleanup tasks.

Errors:
'''

try: # try block
    num = int(input("Enter a number: "))
    divisor = int(input("Enter the divisor: "))
    result = num / divisor
    print(f"Result: {result}")
except ZeroDivisionError: # ZeroDivisionError is a built-in exception
    print("Error: You cannot divide by zero.")
except ValueError: # ValueError is a built-in exception
    print("Error: Invalid input. Please enter numbers only.")
else: # else block is executed if no exception occurs in the try block
    print("Division successful.")
finally: # finally block is executed no matter what, used for cleanup tasks
    print("Execution completed.")

'''
Common types of Exceptions:

- ZeroDivisionError: raised when a number is divided by zero.
- ValueError: raised when an invalid value is passed to a function.
- TypeError: raised when an operation is performed on an object of an inappropriate type.
- NameError: raised when a variable or function is not defined.
- IndexError: raised when an index is out of range.
- KeyError: raised when a key is not found in a dictionary.
- FileNotFoundError: raised when a file is not found.
- AttributeError: occurs when you try to access or modify an attribute 
(like a variable or function) that doesn't exist for the object you're working with
'''