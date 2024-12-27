# The pass statement in Python is a placeholder that does nothing when executed.
# It is used when a statement is syntactically required, but you don’t want any code to run.

# Why Do We Use pass?
# Placeholder for Code: To define a block of code that you plan to implement later.
# Avoid Syntax Errors: Python does not allow empty code blocks; pass helps to bypass this restriction.
# Readability: Indicates intentional emptiness in a block of code for future implementation.

# example
def print_hello():
    pass

print_hello() # will print nothing