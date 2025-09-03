from functools import reduce
import asyncio

 # def function_name(parameters):
    # function body

# define a function
def greeting():
    print('Hello, World')

# call a function
greeting()

# function arguments - you can add data_type for arguments and return_type
def even_odd(x: int) -> str:
    if x % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(even_odd(4))
print(even_odd(3))

# types of function arguments
# default argument
def default_args(x, y=10):
    print('x:', x)
    print('y:', y)

default_args(20)

# keyword arguments
def student(fname, lname):
    print(fname, lname)

student(fname='John', lname='Doe')

# arbitrary keyword arguments - *args and **kwargs
def my_fun(*args):
    print(args)

my_fun(1, 2, 3)
my_fun('a', 'b')

def my_fun2(**kwargs):
    print(kwargs)

my_fun2(name='Jane', age=60)
my_fun2(city='Stockholm', country='Sweden')


# docstring
def print_doc():
    """This text should describe the function
    """
    print(print_doc.__doc__)

print_doc()

# inner function / nested function
def outer_fun():
    s = 'Snakes'
    def inner_fun():
        print(s)
    inner_fun()

outer_fun()

# return - ends function and (opt) returns value 
# anonymous function
def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(7))

# reference value
# if you update a value, it will change outside the function
def ref_fun(x):
    x[0] = 20

li = [10, 11, 12, 13, 14, 15]
ref_fun(li)
print(li)

# if you assign a new value the link to the old object is broken
def ref_fun2(x):
    x = [20, 30, 40]

li = [10, 11, 12, 13, 14, 15]
ref_fun2(li)
print(li)

# recursive functions - a function that calls itself
def countdown(n):
    if n == 0:
        print('Done')
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# calling function from function
def multiply(a, b):
    return a * b

def rectangle_area(width, heigth):
    return multiply(width, heigth)

print(rectangle_area(5, 5))

# map - filter - reduce
# map - adds 10 on every element
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x + 10, numbers))
print(result)

# filter - filters elements that meets condition
result = list(filter(lambda x: x > 3, numbers))
print(result)

# reduce - adds all the numbers togheter
result = reduce(lambda a, b: a + b, numbers)
print(result)

# assigning function to variable
def a():
    print('Python')

snake = a
snake()

# local and global variable
x = 123

def display():
    x = 42
    print(x)
    print(globals()['x'])

print(x)
display()

# async functions
async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return f"{name} result"

async def task_main():
    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )
    print("Results:", results)

asyncio.run(task_main())









