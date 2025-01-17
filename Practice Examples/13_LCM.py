def gcd(a, b):
    while a % b > 0:
        a, b = b, a % b
    return b

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display LCM
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")
