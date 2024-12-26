# seek() method: moves the file pointer to a specified position in the file
# tell() method: returns the current position of the file pointer in the file

# example of seek() and tell() methods
with open('example4.txt', 'w+') as file:
    file.write("example to demonstrate seek and tell function.")
    print(file.tell()) # printing the current position of the file pointer
    file.seek(0) # moving the file pointer to the beginning of the file
    content = file.read() # reading the content of the file
    print(content) # printing the content of the file