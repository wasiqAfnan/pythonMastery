import math
def digits(n):
    num = n
    digit = 0
    while num > 0:
        temp = num % 10
        num //= 10
        digit += 1

    return digit

def checkArmstrong(n):
    digit = digits(n)
    res = 0
    copy = n
    while copy > 0:
        temp = copy % 10
        res += math.pow(temp,digit)
        copy //= 10
    return res == n

#main
num = int(input("Enter a number: "))
if checkArmstrong(num):
    print(f"{num} is armstrong")
else:
    print(f"{num} is not armstrong")
