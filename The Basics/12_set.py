'''
A set in Python is an unordered collection of unique elements. Sets are mutable,
meaning you can add or remove elements, but they do not allow duplicate values.
Sets are defined using curly braces {} or the set() constructor.
'''

# Creating a set
fruits = {"apple", "banana", "orange"}
print(fruits)

# another way to create a set
fruits = set(["apple", "banana", "orange"])

# traversing a set
for fruit in fruits:
    print(fruit)

# set methods
colors = {"red", "green", "blue"}
colors.add("yellow") # add an element to the set
colors.remove("green") # remove an element from the set if present else gave error
colors.discard("green") # remove an element from the set if it is present else do nothing
colors.clear() # remove all elements from the set
print(colors)
colors.copy() # return a copy of the set
print(colors.union({"red", "green", "blue", "yellow"})) # return a new set with elements from both sets
print(colors.intersection({"red", "green", "blue", "yellow"})) # return a new set with elements common to both sets
print(colors.difference({"red", "green", "blue", "yellow"})) # return a new set with elements in the first set but not in the second set
print(colors.symmetric_difference({"red", "green", "blue", "yellow"})) # return a new set with elements in either set but not in both