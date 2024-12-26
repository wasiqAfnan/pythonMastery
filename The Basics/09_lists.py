# lists are mutable sequences
# lists can contain any type of data
# lists are indexed starting from 0

# List declaration
fruits = ["apple", "banana", "orange"]
fruits[0] = "apple"
fruits[1] = "banana"
fruits[2] = "orange"
print(fruits)

# traversing list
for fruit in fruits:
    print(fruit)


# List methods
colors = ["red", "green", "blue"]
colors.append("yellow") # add an element to the end of the list
colors.insert(0, "black") # add an element to the beginning of the list
colors.remove("green") # remove an element from the list
colors.pop() # remove an element from the end of the list
colors.pop(2) # remove an element from the index 2
colors.clear() # remove all elements from the list

colors = ["red", "green", "blue"]
colors.index("green") # return the index of the first element that matches the given value
colors.count("green") # return the number of times the given value appears in the list
colors.sort() # sort the list in ascending order
colors.reverse() # reverse the list
colors.copy() # return a copy of the list
colors.sort(reverse=True) # sort the list in descending order
print(colors)

# List comprehension
'''
List comprehension in Python is a concise and powerful way to create lists. 
It allows you to construct new lists by applying an expression to each item in an iterable, 
optionally with a condition.


Key Components:
Expression: The operation or transformation applied to each item.
Iterable: The source of data (e.g., list, range, string).
Condition (optional): Filters items based on a condition.

Syntax: 
[expression for item in iterable if condition]
'''

# Create a list of squares for numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)

# Create a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# Create a list of numbers that are divisible by 3
divisible_by_three = [x for x in range(1, 11) if x % 3 == 0]
print(divisible_by_three)
