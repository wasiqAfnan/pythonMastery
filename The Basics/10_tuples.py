# A tuple in Python is an ordered, immutable collection of elements, defined using parentheses ().
# Tuples can store heterogeneous data types and support indexing and slicing.

# Tuple declaration
fruits = ("apple", "banana", "orange")
#fruits[0] = "watermelon" # this will raise an error as tuples are immutable
print(fruits)

# traversing a tuple
for fruit in fruits:
    print(fruit)

# Tuple methods
colors = ("red", "green", "blue")
colors.index("green") # return the index of the first element that matches the given value
colors.count("green") # return the number of times the given value appears in the list

# adding new elements to a tuple
fruits = ("apple", "banana", "orange")
fruits += ("grape", "kiwi")
print(fruits)

# removing elements from a tuple
fruits = ("apple", "banana", "orange")
#fruits.remove("banana") # will rasie an error as tuples are immutable

