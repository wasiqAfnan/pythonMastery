'''
There are several types of operators in Python:

Arithmetic operators:
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor division
% Modulus
** Exponentiation

Comparison operators:
== Equal to
!= Not equal to
< Less than
<= Less than or equal to
> Greater than
>= Greater than or equal to

Logical operators:
and Logical AND
or Logical OR
not Logical NOT

Assignment operators:
= Assignment
+= Addition assignment
-= Subtraction assignment
*= Multiplication assignment
/= Division assignment
%= Modulus assignment
**= Exponentiation assignment

Bitwise operators:
& Bitwise AND
| Bitwise OR
^ Bitwise XOR
~ Bitwise NOT
<< Left shift
>> Right shift

Membership operators:
in Membership test
not in Membership test
is Membership test
is not Membership test

Ternary operator:
? True if expression is true, else false
'''

# Arithmetic operators
a = 5
b = 10
print("Arithmetic Operators")
print(f"{a} + {b} = {a + b}") # Addition output: 5 + 10 = 15
print(f"{a} - {b} = {a - b}") # Subtraction output: 5 - 10 = -5
print(f"{a} * {b} = {a * b}") # Multiplication output: 5 * 10 = 50
print(f"{a} / {b} = {a / b}") # Division output: 5 / 10 = 0.5
print(f"{a} // {b} = {a // b}") # Floor division output: 5 // 10 = 0
print(f"{a} % {b} = {a % b}") # Modulus output: 5 % 10 = 5
print(f"{a} ** {b} = {a ** b}") # Exponentiation output: 5 ** 10 = 3125

# Comparison operators
a = 5
b = 10
print("Comparison Operators")
print(f"{a} == {b}") # Equal to output: 5 == 10 gives False
print(f"{a} != {b}") # Not equal to output: 5 != 10 gives True
print(f"{a} < {b}") # Less than output: 5 < 10 gives True
print(f"{a} <= {b}") # Less than or equal to output: 5 <= 10 gives True
print(f"{a} > {b}") # Greater than output: 5 > 10 gives True
print(f"{a} >= {b}") # Greater than or equal to output: 5 >= 10 gives True

# Logical operators
x = True
y = False

print("Logical Operators")
print(f"{x} and {y} = {x and y}") # Logical AND output: True and False gives False
print(f"{x} or {y} = {x or y}") # Logical OR output: True or False gives True
print(f"not of {x} =  {not x}") # Logical NOT output: not True gives False

# Assignment operators
a = 5
b = 10
print("Assignment Operators")
print(f"= is used to assign any value to the variable")
a+=b # add value of a and b and then store result in a | output: 15
a-=b # subtract value of a and b and then store result in a | output: 5
a*=b # multiply value of a and b and then store result in a | output: 50
a/=b # divide value of a and b and then store result in a   | output: 2.5
a//=b # floor divide value of a and b and then store result in a | output: 2
a%=b # modulus value of a and b and then store result in a | output: 5
a**=b # exponentiate value of a and b and then store result in a | output: 3125

# Bitwise operators
x = 5
y = 10
print("Bitwise Operators")
print(f"{x} & {y} = {x & y}") # Bitwise AND output: 5 & 10 = 0
print(f"{x} | {y} = {x | y}") # Bitwise OR output: 5 | 10 = 15
print(f"{x} ^ {y} = {x ^ y}") # Bitwise XOR output: 5 ^ 10 = 15
print(f"~ {x} = {~x}") # Bitwise NOT output: ~ 5 = -6
print(f"<< {x} = {x << 1}") # Left shift output: 5 << 1 = 10
print(f">> {x} = {x >> 1}") # Right shift output: 5 >> 1 = 2

# Membership operators
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato", "tomato"]

print("Membership Operators")
print(f"{"apple"} in {fruits}") # Membership test output: 'apple' in ['apple', 'banana', 'cherry'] gives True
print(f"{"apple"} not in {fruits}") # Membership test output: 'apple' not in ['apple', 'banana', 'cherry'] gives False

# is and not is
num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = num1

print("is and not is")
print("Num3 is Num1 = ",num3 is num1) # is gives True
print("Num3 is not Num1 = ",num3 is not num1) # is not gives False
print("Num3 is Num2 = ",num3 is num2) # is gives False
print("Num3 is not Num2 = ",num3 is not num2) # is not gives True



# Ternary operator
x = 5
y = 10
print("Ternary Operator")
greater = x if x > y else y
print(f"greater = {greater}") # greater = 10

