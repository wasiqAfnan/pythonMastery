# File I/O (Input/Output) in Python is used to read from and write to files.
# There are two types of file I/O in Python: text and binary.
# Text files are files that contain text data, such as text documents, emails, etc.
# Binary files are files that contain binary data, such as images, videos, etc.

# In Python, you can open a file using the open() function.
# The open() function takes two arguments:
# the name of the file and
# the mode in which you want to open the file.

# The mode can be:
# "r": Read (default mode)
# "w": Write (overwrites file if it exists)
# "a": Append (adds to the end of the file)
# "x": Create (creates a new file, fails if it exists)
# "b": Binary mode (use with others like "rb", "wb")
# "t": Text mode (default)
# "r+": Read and write (default mode)
# "w+": Write and read (overwrites file if it exists)
# "rb": Read binary file
# wb": Write binary file

# Here's an example of opening a file in write mode:
file = open('example.txt', 'w')
msg = "Hey this is my first text file using python file IO"
file.write(msg) # writing the message to the file
file.close() # closing the file

# Here's an example of opening a file in read mode:
file = open('example.txt', 'r')
content = file.read() # reading the content of the opened file
print(content) # printing the content of the file
file.close() # closing the file

# Here's an example of opening a file in append mode:
file = open('example.txt', 'a')
msg = "\nHey this is my second line of text file using python file IO"
file.write(msg) # writing the message to the file
file.close() # closing the file

# Here's an example of opening a file in read mode:
file = open('example.txt', 'r')
for line in file:
    print(line) # printing each line of the file
file.close() # closing the file