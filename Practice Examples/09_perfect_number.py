'''
A number is called perfect when sum of all its factors, except itself, is equal to the number,
i.e. 6 is a perfect number, 6=1+2+3, factors of 6=(1,2,3)).
'''

def checkPerfectNumber(n):
    res = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            res += i
    return res == n
# main
num = int(input("Enter a number: "))
if checkPerfectNumber(num):
    print(f"{num} is Perfect number")
else:
    print(f"{num} is not Perfect number")