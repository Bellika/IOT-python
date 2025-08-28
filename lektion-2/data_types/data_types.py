# Numeric datatypes 

# Integers - int class, contains positive or negative WHOLE numbers
# Float - float class, its a real number, specified by decimal point
# Complex Numbers - complex class, specified as (real part) + (imaginary part). For example 1 + 2j.
# Think about a system with x-axis and y-axis. z = 2 + 3j would be (2,3) in this system. Real part is 2 steps right in the x-axis and imaginary part is 3 steps up in the y-axis.  

a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))



# Sequence Data Types 

# String Data Type 

s = 'This is a string in Python'
print(s)

print(type(s))

print(s[1])
print(s[2])
print(s[-1])

# List Data Type

a = []

a = [1, 2, 3]
print(a)

b = ['Python', 'is', 'fun', 1, 2]
print(b)

print(b[0])
print(b[1])

# Negative indexing starts from -1 and refers to the last item
print(b[-1])
print(b[-3])

# Tuple Data Type 
# The difference between a Tuple and a list is that a tuple cannot be modified after it is created

tup1 = () # Can for example be used to return an empty value from a function

tup2 = ('Hello', 'World')
print('This is tuple with strings:', tup2)

print(tup2[0])
print(tup2[-1])
print(tup2[-2])


# Boolean Data Type 
print(type(True))
print(type(False))
#print(type(true))


# Set Data Type
# Unordered - when you print a set the order can change 
# Iterable - you can use loops over sets
# Mutable - can be changed
# No duplicated elements

fruits = {"apple", "banana", "cherry"}

numbers = set([1, 2, 3, 4])   # from list
letters = set("hello")         # from string 
print(numbers, '\n', letters)


# Dictionary Data Type
# Dictionary holds a key and a value pair

d = {}

d = {1: 'Hello', 2: 'Python', 3: 'World'}
print(d)

# This can be used if you build a dict from a list, tuple, something you can iterate over
d1 = dict({1: 'Hello', 2: 'Python', 3: 'World'})
print(d1)

# Accessing key values (strings can also be used as keys)
print(d1[2])
print(d1.get(3))




