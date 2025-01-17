def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# another method
def gcd2(a, b):
    while a % b > 0:
        a, b = b, a % b
    return b

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display GCD
result = gcd(num1, num2)
result2 = gcd2(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
print(f"The GCD of {num1} and {num2} is {result2}")
