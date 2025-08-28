# Variables in Python do not require typing.

x = 10

name = 'Jane'

print(x)
print(name)

# RULES
# Variables can only contain letters, digits and underscores.
# Cannot start with digit
# Dont use keywords as names

# Variables have dynamic typing meaning they can change the value stored
x = 5
x = 'string'

# Multiple assignments
a = b = c = 50
print(a, b, c)

# Multiple assignments with different values
x, y, z = 1, 2, 'Three'
print(x, y, z)

# Type Casting

# int() - Convert to integer
# float() - Convert to floating-point
# str() - Convert to string

string = '10'
number = int(string)

count = 5
f = float(count)

age = 25
age_string = str(age)

print(number, f, age_string)
print(type(age_string))

# TYPE

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

# Object Reference

x = 5

# Python creates an object that presents the value 5 and x is the reference to this object

y = x 

# y is a reference to the same object, NOT to x (shared reference)

x = 'Python'

# Now x is a reference to the object 'Python' but the y variable still reference the original object 5


# Delete a variable 

x = 10
print(10)

del x 
#print(x)


# Swapping variables 

a, b = 5, 10
print(a, b)

a, b = b, a
print(a, b) 


# Counting characters in strings

word = 'Python'
length = len(word)
print('Length of string: ', length)


# Scope

# Local variables
# Defined within a function

# Global variables 
# Defined outside functions, accessible throughout the program
