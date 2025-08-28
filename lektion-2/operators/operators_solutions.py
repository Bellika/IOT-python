# ==========================
# Python Operators - Solutions
# ==========================

# 1. Arithmetic Operators
a = 8
b = 3

print("Addition:", a + b)          # 11
print("Subtraction:", a - b)       # 5
print("Multiplication:", a * b)    # 24
print("Division:", a / b)          # 2.666...
print("Floor Division:", a // b)   # 2
print("Modulus:", a % b)           # 2
print("Exponentiation:", a ** b)   # 512


# 2. Comparison Operators
a = 7
b = 10

print(a > b)   # False
print(a < b)   # True
print(a == b)  # False
print(a != b)  # True
print(a >= b)  # False
print(a <= b)  # True


# 3. Logical Operators
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False


# 4. Assignment Operators
a = 5
b = a
print(b)  # 5

b += a
print(b)  # 10

b -= a
print(b)  # 5

b *= a
print(b)  # 25


# 5. Identity Operators
a = 10
b = 20
c = a

print(a is b)      # False
print(a is not b)  # True
print(a is c)      # True
print(a is not c)  # False


# 6. Membership Operators
my_list = [5, 10, 15, 20]
x = 25
y = 10

print(x in my_list)   # False
print(x not in my_list)  # True

print(y in my_list)   # True
print(y not in my_list)  # False
