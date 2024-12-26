# Loops are used to repeat a block of code multiple times.

# for loop
print("for loop")
for i in range(5): # range(5) generates numbers from 0 to 4
    print(i)

# while loop
print("while loop")
i = 0
while i < 5:
    print(i)
    i += 1

# nested loops
# program to print star pattern
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()

# break statement
print("break statement")
for i in range(10):
    if i == 5:
        break # break statement stops the loop
    print(i)

# continue statement
print("continue statement")
for i in range(10):
    if i == 5:
        continue # continue statement skips the portion of the loop in which condition is true
    print(i)

# else statement
# In Python, the else statement can be used with loops (for and while). It executes only if the loop completes normally without being interrupted by a break statement.

print("else statement")

for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without interruption!")
# The else block won't execute because of the 'break'.

# Example 2: Using else with a while loop
count = 0
while count < 3:
    count += 1
else:
    print("Loop ended naturally!")
# Output: Loop ended naturally!

# range staement
print("range statement")
for i in range(5): # range(5) generates numbers from 0 to 4
    print(i)

for i in range(1, 6): # range(1, 6) generates numbers from 1 to 5
    print(i)

for i in range(1, 10, 2): # range(1, 10, 2) generates numbers from 1 to 10 with a step of 2
    print(i)

# Pass statement
# In Python, the pass statement is a null operation — it does nothing when executed. It is
# commonly used as a placeholder in loops, conditionals, functions, or classes where code is
# syntactically required but you don't want to write any code at that moment.

print("pass statement")

for i in range(5):
    pass  # No action taken in this loop
print("Loop completed.")


'''
Why use pass?
Maintain syntax: It’s used to avoid syntax errors when a statement is required, but you
don’t want to do anything in a certain part of the code yet.
'''

