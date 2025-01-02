# print no of lines, words and char in a file

with open("file1.txt","r") as file:
    word = 0; line = 1; characrter = 0
    content = file.read()
    lines = content.split("\n") # spliiting lines
    words = content.split() # splitting words
    character = len(content) # counting char

    print(len(words))
    print(len(lines))
    print(character)

