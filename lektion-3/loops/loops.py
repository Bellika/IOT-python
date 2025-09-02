# for loop - used to iterate over a sequence (for example a list or string)

# simple for loop
n = 4
for i in range(0, n):
    print(i)

# loop backwards
for i in range(5, 0, -1):
    print('Backwards:', i)

# iterate over list, string and dictionaty
li = ['iterate', 'over', 'list']
for i in li:
    print(i)

s = 'Python'
for i in s:
    print(i)

d = {'x':123, 'y':345}
for key, value in d.items():
    print(f'{key} {value}')

# keys() - only keys
# values() - only values
# items() - keys and values

# iterate by index in sequence 
li = ['snakes', 'and', 'arrows']
for index in range(len(li)):
    print(li[index])

# enumerate - gives both index and value
for index, value in enumerate(li):
    print(index, value)

# else statement and for loop
for index in range(len(li)):
    print(li[index])
else:
    print('This will execute when the loop is done')

# while loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print('Python', cnt)

# break while loop
cnt = 0
while cnt < 5:
    cnt += 1
    if cnt == 3:
        print('Breaking the loop at 3')
        break
    print(cnt)

# else statement and while loop - the else condition executen when while becomes false
cnt = 0
while (cnt < 3):
    cnt += 1
    print('Snakes', cnt)

# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=' ')
    print()

# continue/break statement
for letter in 'snakes':
    if letter == 'a' or letter == 's':
        continue
        #break    
    print('Current Letter :', letter)

# pass statement
for letter in 'snakes':
    pass
print('The last letter gets printed because its the last value of the sequence: ', letter)

# list comprehension
squares = [x**2 for x in range(5)]
print(squares)









