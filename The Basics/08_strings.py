# string in python is a sequence of characters.
# string can be enclosed in single quotes ('') or double quotes ("") or triple quotes ("""""").

# String declaration using single quotes
name = 'Wasiq Afnan Ansari'
print(name)

# String declaration using double quotes
name = "Wasiq\nis a programmer"
print(name)

# String declaration using triple quotes
name = """Wasiq Afnan Ansari
is a programmer.
He knows Python"""
print(name)

# String concatenation
name = "Wasiq Afnan"
surname = "Ansari"
print(name + " " + surname)

# String interpolation
first_name = "Wasiq Afnan"
last_name = "Ansari"
print(f"{first_name} {last_name}")

# String slicing
name = "Wasiq Afnan Ansari"
print(name[0:5]) # Wasiq
print(name[5:10]) # Afna
print(name[10:15]) # n Ansari
print(name[15:]) # ari

# Negative indexing
name = "Wasiq Afnan Ansari"
print(name[-1]) # i

# Neggative Slicing
name = "Wasiq Afnan Ansari"
print(name[-6:]) # Ansari
print(name[-10:-5]) # nan A

# String methods
name = "Wasiq Afnan Ansari    "
print(name.upper()) # WASIQ AFNAN ANSARI
print(name.lower()) # wasiq afnan ansari
print(name.title()) # Wasiq Afnan Ansari
print(name.strip()) # Wasiq Afnan Ansari
print(name.replace("Afnan", "Afnan-1")) # Wasiq Afnan-1 Ansari
print(name.split()) # ['    Wasiq ', ' Afnan ', ' Ansari    ']
print(",".join(name.split())) # Wasiq,Afnan,Ansari
print(name.find("Afnan")) # 10
print(name.count("Afnan")) # 1
print(name.index("Afnan")) # 10
print(name.startswith("Afnan")) # False
print(name.endswith("Afnan")) # False
print(name.capitalize()) # Wasiq afnan ansari

num = "12345"
text = "Hello world"

print(num.isdigit()) # True
print(name.isalpha()) # False
print(text.replace(" ","").isalpha()) # True
print(num.isalpha()) # False
print(text.isupper()) # False
print(text.islower()) # False