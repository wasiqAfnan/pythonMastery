def factRecursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return  n * factRecursion(n-1)
def factLoop(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
# main
num = int (input("Enter a number: "))
fact = factLoop(num)
fact2 = factRecursion(num)
print(f"factorial of {num} is = {fact}")
print(f"factorial of {num} is = {fact2}")