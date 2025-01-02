# copy the content of one file to another file
file = open("file1.txt","r")
content = file.readlines()
file2 = open("file2.txt","w+")
for line in content:
	file2.write(line)
content2 = file2.read()
print(content2)