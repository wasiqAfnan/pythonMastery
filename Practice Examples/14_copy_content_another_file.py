src = input("Source file: ")
dest = input("Destination file: ")

with open(src, 'r') as source:
    content = source.read()

with open(dest, 'w') as destination:
    destination.write(content)

with open(dest,'r') as destination:
    print("Destination file contents: ", destination.read())
