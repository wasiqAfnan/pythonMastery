def checkPalindrome(n):
    num = n
    reverse = 0
    while num > 0:
        temp = num % 10
        reverse = reverse * 10 + temp;
        num //= 10

    if reverse == n:
        return True
    else:
        return False

# main
num = int (input("Enter a number: "))
if checkPalindrome(num):
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not a palindorme number")
