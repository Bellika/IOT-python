# if (this condition is true):
    # This block of code will execute
# else:
    # This block of code will execute


age = 25

if age >= 18:
    print('Can vote')


# short form if 
if age > 18: print('Cannot vote')


# if - else 
age = 10
if age <= 12:
    print('Can travel for free')
else: 
    print('Pay for ticket')


# short form if - else 
points = 35
res = 'Pass' if  points >= 35 else 'Fail'


# if - elif (stands for else if)
age = 25

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young adult")
else:
    print("Adult")

# and/or statement
has_id = True

if age >= 18 and has_id:
    print("Can vote")
else:
    print("Cannot vote")

# not statement
is_raining = True

if not is_raining:
    print('Go outside')
else:
    print('Write code')

# nested if - else
age = 60
is_member = True

if age >= 50:
    if is_member:
        print('Discount: 50%')
    else:
        print('Discount: 30%')
else: 
    print('Regular price')


# match-case / switch-case
number = 2

match number:
    case 1:
        print('one')
    case 2 | 3:
        print('two or three')
    case _:
        print('other number')





