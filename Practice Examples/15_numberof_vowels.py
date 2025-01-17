src = input("Enter file name: ")
vowels = "aeiouAEIOU"
vowel = 0
with open(src,'r') as source:
    content = source.read()
    for char in content:
        if char in vowels:
            vowel += 1
    print("Number of vowels: ", vowel)