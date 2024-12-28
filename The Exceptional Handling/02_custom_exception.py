'''
If an exception occurs that is not a predefined type (like ValueError or FileNotFoundError),
you can handle it using a general exception handler or by defining and raising a custom exception.
'''

# example of custom exception

try:
    # A block of code that might raise an unexpected exception
    number = int(input("Enter a number: "))
    if number < 0:
        raise Exception("Negative numbers are not allowed!") # raising custom exception
    print(f"Your number is: {number}")
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e: # handling general exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")


# Raising any sepcific exception

# inheriting Exception class to create custom exception
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print(f"Your number is: {number}")
except NegativeNumberError as e: # handling specific exceptions that raise by negative number
    print(f"Custom Error: {e}")
except Exception as e: # handling any other exceptions that might occur
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")

