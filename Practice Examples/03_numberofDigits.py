def digits(n):
    num = n
    digit = 0
    while num > 0:
        num //= 10
        digit += 1

    return digit

# main
num = int (input("Enter a number: "))
dig = digits(num)
print(f"{num} has {dig} digits")

# Another method by converting the number to string
mystr = str(num)
print(mystr)
print(len(mystr))
