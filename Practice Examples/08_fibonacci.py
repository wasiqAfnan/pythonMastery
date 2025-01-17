def fibRecursion(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibRecursion(n-1) + fibRecursion(n-2)

def fibLoop(n):
    a = 0
    b = 1
    for i in range(0, n):
        if(i == 0):
            print("0", end = "\t")
        elif(i == 1):
            print("1", end = "\t")
        else:
            c = a+b
            print(c, end = "\t")
            a = b
            b = c

# main
num = int(input("Enter a number: "))
for i in range(1, num+1):
    print(fibRecursion(i), end = "\t")
#fibLoop(num)