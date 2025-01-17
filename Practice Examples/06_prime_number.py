import math
# my approach
def checkPrime(n):
    if n <= 1:
        return False

    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True
#optimized approach
def checkPrimeOptimized(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# main
num = int(input("Enter a number: "))
if checkPrime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a not prime number")

# calling optimized approach
if checkPrimeOptimized(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a not prime number")
