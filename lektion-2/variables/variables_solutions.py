# ==========================
# Variables in Python - Solutions
# ==========================

# 1. Simple variable
city = "Stockholm"
print(city)  # Output: Stockholm


# 2. Naming rules
variable1 = 100       # Fixed: cannot start with a number
my_variable = "hello" # Fixed: cannot use dashes
print_value = "hej"   # Fixed: avoid overwriting built-ins like 'print'


# 3. Case sensitivity
Age = 25
age = 30
print(Age)  # 25
print(age)  # 30
# Explanation: 'Age' and 'age' are two different variables.


# 4. Dynamic typing
x = 42
print(x)        # 42
x = "Now I'm text"
print(x)        # Now I'm text


# 5. Multiple assignments
a, b, c = 10, 20, "Thirty"
print(a, b, c)  # Output: 10 20 Thirty


# 6. Type casting
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print(num_int, type(num_int))     # 123 <class 'int'>
print(num_float, type(num_float)) # 123.0 <class 'float'>


# 7. Object references
x = 5
y = x
x = 10
print("x:", x)  # x: 10
print("y:", y)  # y: 5
# Explanation: y keeps the reference to the old value (5).


# 8. Swapping values
a, b = 5, 10
a, b = b, a
print("a:", a)  # a: 10
print("b:", b)  # b: 5


# 9. String length
word = "Python"
length = len(word)
print("Length of string:", length)  # Length of string: 6


# 10. Scope
x = "global"

def my_func():
    x = "local"
    print("In function:", x)

my_func()                    # In function: local
print("Outside function:", x)  # Outside function: global
# Explanation: the function defines a local variable x,
# which does not change the global x.
