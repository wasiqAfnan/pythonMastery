# if statement
x = 5
if x > 10:
    print(f"{x} is greater than 10")

# if-else statement
x = 5
if x > 10:
    print(f"{x} is greater than 10")
else:
    print(f"{x} is less than or equal to 10")

# if-elif-else statement
x = 5
if x > 10:
    print(f"{x} is greater than 10")
elif x == 10:
    print(f"{x} is equal to 10")
else:
    print(f"{x} is less than 10")

# Nested if-elif-else statement
# Example to find greatest of three numbers
x = 5
y = 10
z = 15
if x > y:
    if x > z:
        print(f"{x} is the greatest number")
    else:
        print(f"{z} is the greatest number")
else:
    if y > z:
        print(f"{y} is the greatest number")
    else:
        print(f"{z} is the greatest number")