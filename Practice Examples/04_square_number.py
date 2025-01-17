import math
def checkSquare(n):
    sqrt = math.sqrt(n)
    return sqrt.is_integer()


# main
num = int (input("Enter a number: "))
if checkSquare(num):
    print(f"{num} is square number")
else:
    print(f"{num} is not a square number")
