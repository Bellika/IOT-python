# ==========================
# Python Data Types - Solutions
# ==========================

# 1. Numeric Datatypes
int_var = 10
float_var = 10.5
complex_var = 3 + 4j

print(int_var, type(int_var))         # 10 <class 'int'>
print(float_var, type(float_var))     # 10.5 <class 'float'>
print(complex_var, type(complex_var)) # (3+4j) <class 'complex'>


# 2. Strings
my_string = "Python is fun"
print(my_string[0])  # P
print(my_string[1])  # y
print(my_string[-1]) # n


# 3. Lists
my_list = [1, 2, 3, 'Python', 'AI']
print(my_list[0])    # 1
print(my_list[-1])   # AI
print(my_list[-2])   # Python


# 4. Tuples
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # apple
print(my_tuple[-1]) # cherry
# my_tuple[0] = "orange"  # This will raise TypeError because tuples are immutable


# 5. Booleans
is_true = True
is_false = False
print(type(is_true))  # <class 'bool'>
print(type(is_false)) # <class 'bool'>


# 6. Sets
my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)  # {'banana', 'apple', 'cherry'} (order may vary, no duplicates)
my_set.add("orange")
print(my_set)  # {'banana', 'apple', 'cherry', 'orange'}


# 7. Dictionaries
my_dict = {1: "One", 2: "Two", 3: "Three"}
print(my_dict[2])       # Two
print(my_dict.get(3))   # Three
