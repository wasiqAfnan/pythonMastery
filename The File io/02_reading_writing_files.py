# methods to read and write to files in Python
# read() method: reads the entire content of the file and returns it as a string
# readline() method: reads a single line from the file and returns it as a string
# readlines() method: reads all lines from the file and returns them as a list of strings
# write() method: writes a string to the file
# writelines() method: writes a list of strings to the file
# append() method: appends a string to the end of the file
# close() method: closes the file

# example to showcase methods to read and write to files in Python
# opening a file in write mode
file = open('example2.txt', 'w')
msg = ["This msg", " is written using", " writelines() method"]
file.writelines(msg) # writing the list of strings to the file
file.close() # closing the file

# opening the file in read mode
file = open('example2.txt', 'r')
content = file.readlines() # reading all lines from the file
for line in content:
    print(line.strip()) # printing each line of the file
file.close() # closing the file

# with open in file io is used to open a file and automatically close it after
# the block of code is executed
# it is a context manager that ensures that the file is properly closed after
# the block of code is executed

# example of with open in file io
with open ('example3.txt', 'w') as file:
    file.write("This is a file opened using with open in file io")
# the file is automatically closed after the block of code is executed

with open('example3.txt', 'r') as file:
    content = file.readlines() # reading all lines from the file
    for line in content:
        print(line.strip()) # printing each line of the file