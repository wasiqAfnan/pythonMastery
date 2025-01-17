'''
Write a program in Python to calculate the value of e^x series upto nth term.
The value of x and n should be given by the user.

'''
import math


def calculateEtoX(n,x):
    sumofseries = 1
    for i in range(0,n):
        sumofseries += (math.pow(x,i+1)/math.factorial(i+1))
    print(sumofseries)
calculateEtoX(5,2)