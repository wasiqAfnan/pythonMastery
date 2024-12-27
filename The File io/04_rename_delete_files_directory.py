# to rename a file or directory in python we have to use a function called os.rename()
# to delete a file or directory in python we have to use a function called os.remove()
# to delete a directory in python we have to use a function called os.rmdir()

import os

# creating a file using file io
with open('newfile.txt', 'w') as file:
    file.write("This is an example file")

# rename a file or directory
os.rename('newfile.txt', 'new_file.txt')
# delete a file
os.remove('new_file.txt')
# delete a directory
os.rmdir('old_directory')