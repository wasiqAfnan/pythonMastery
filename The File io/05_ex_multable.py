# Program to generate multiplication table using file IO

with open("multiplication.txt","w+") as file:
    for i in range(1, 11):
        file.write(f"Multiplication table for {i}\n")
        for j in range(1, 11):
            result = i * j
            file.write(f"{i} x {j} = {result}\n")

