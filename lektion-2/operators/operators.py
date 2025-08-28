# Arithmetic Operators 
# Used to perform basic math

a = 11
b = 2

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)


# Comparison
a = 2
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Logical Operators
a = True
b = False
print('########')
print(a and b)
print(a or b)
print(not a)

# Assignment Operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)

# Identity Operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership Operators - tests whether a values or variable is in a sequence
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

