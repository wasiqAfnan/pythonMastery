'''
Write a program in Python to test the given number is special number or not.
Special No : abc=a! + b! + c! (Ex : 145= 1! + 4! +5! )
'''
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def checkSpecialNumber(n):
    copy = n; sum = 0
    while copy > 0:
        temp = copy % 10
        sum += fact(temp)
        copy //= 10
    return sum == n

# main
num = int(input("Enter a number: "))
if checkSpecialNumber(num):
    print(f"{num} is a special number")
else:
    print(f"{num} is not a special number")