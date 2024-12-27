'''
Access specifiers determine the visibility and accessibility of variables, methods, or attributes
within a class. Python has three levels of access specifiers: public, protected, and private.
Unlike other languages (e.g., Java, C++), Python relies on naming conventions rather than
strict access controls to implement them.
'''

'''
1. Public Access
Definition: Attributes and methods with public access can be accessed from anywhere—inside or outside the class.
Implementation: By default, all attributes and methods in Python are public.

2. Protected Access
Definition: Attributes and methods with protected access can only be accessed within the class and its subclasses. In Python, this is a convention indicated by a single underscore _attribute.
Implementation: Use a single underscore (_) before the attribute or method name.

3. Private Access
Definition: Attributes and methods with private access can only be accessed from within the class itself.
Implementation: To define a private attribute or method, prefix the name with a double underscore (__).
Private attributes and methods cannot be accessed from outside the class.
'''

# example of public access
class PublicExample:
    def __init__(self):
        self.name = "Public Attribute"  # Public attribute

    def display(self):  # Public method
        print(self.name)

obj = PublicExample()
print(obj.name)  # Accessing the public attribute
obj.display()    # Accessing the public method

# example of protected access
class ProtectedExample:
    def __init__(self):
        self._data = "Protected Attribute"  # Protected attribute

    def _protected_method(self):  # Protected method
        print(self._data)

class SubClass(ProtectedExample):
    def access_protected(self):
        print(self._data)  # Accessing protected attribute from subclass
        self._protected_method()  # Accessing protected method from subclass

obj = SubClass()
obj.access_protected()
# Accessing protected members outside class is discouraged but possible:
print(obj._data)  # Not recommended

# example of private access
class PrivateExample:
    def __init__(self):
        self.__secret = "Private Attribute"  # Private attribute

    def __private_method(self):  # Private method
        print("This is a private method.")

    def access_private(self):  # Public method to access private members
        print(self.__secret)
        self.__private_method()

obj = PrivateExample()
obj.access_private()  # Accessing private members via a public method
# Direct access is not allowed:
# print(obj.__secret)  # AttributeError
# Accessing private members using name mangling (not recommended):
print(obj._PrivateExample__secret)  # Output: Private Attribute


