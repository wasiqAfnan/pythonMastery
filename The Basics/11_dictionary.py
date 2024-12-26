'''
A dictionary in Python is an unordered, mutable collection of key-value pairs,
where each key is unique and serves as an identifier for its corresponding value.
Dictionaries are defined using curly braces {} and allow for fast lookups by key.
'''

# Creating a dictionary
my_dict = {"name": "Wasiq", "age": 25, "city": "Kolkata"}
print(my_dict)

# traversing a dictionary
for key, value in my_dict.items(): # items() method returns both keys and values
    print(key, ":", value)

for key in my_dict.keys(): # keys() method returns a list of keys
    print(key)

for value in my_dict.values(): # values() method returns a list of values
    print(value)

# Accessing values by key
for key in my_dict.keys():
    print(key, ":", my_dict[key])

# disctionary methods
my_dict = {"name": "Wasiq", "age": 25, "city": "Kolkata"}
print(my_dict.get("name")) # return the value associated with the given key, or None if the key is not found
print(my_dict.update({"country": "India"}) )# add new key-value pairs to the dictionary
print(my_dict.pop("country")) # remove the key-value pair with the given key
print(my_dict.popitem()) # remove the key-value pair with the given key and return it as a tuple
print(my_dict.clear()) # remove all key-value pairs from the dictionary

# dictionary comprehension
# Create a dictionary of squares for numbers from 1 to 5
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Create a dictionary of even numbers from 1 to 10
even_numbers = {x: x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)

# Nested dictionaries
person = {"name": "Wasiq",
          "age": 25,
          "city": "Kolkata",
          "hobbies": {"reading": "books", "playing": "video Games"}
          }
print(person)

# Accessing nested values
person = {"name": "Wasiq",
          "age": 25,
          "city": "Kolkata",
          "hobbies": {"reading": "books", "writing": "stories"}}
print(person["hobbies"]["reading"])