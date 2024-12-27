# Operator Overloading: Python allows you to define the behavior of operators (+, -, *, /, **) for your own classes.

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # Overloading the + operator
        return self.value + other.value

num1 = Number(10)
num2 = Number(20)

print(num1 + num2)  # Output: 30
