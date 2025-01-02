# seek() method: moves the file pointer to a specified position in the file. Seek has these parameters:
# 0: Beginning of the file (default)
# 1: Current position in the file
# 2: End of the file
# tell() method: returns the current position of the file pointer in the file

# example of seek() and tell() methods
with open('example4.txt', 'w+') as file:
    file.write("example to demonstrate seek and tell function.")
    print(file.tell()) # printing the current position of the file pointer
    file.seek(5) # moving the file pointer at 5th position of the file
    content = file.read() # output: le to demonstrate seek and tell function.
    print(content) # printing the content of the file