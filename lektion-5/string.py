# string
s = 'Python'

s = '''This is a multi-line
string in Python'''

print(s)

# accessing string index
s = 'Python is fun'
print(s[3])
print(s[-1])

# string slicing
# string_name[start:end:step]
print(s[7:9])
print(s[:6])
print(s[::-1])
print(s[::-2]) # every other char backwards

# string immutability - strings cannot be changed after creation
# updating string - creates a new string

s = 'python'
s1 = 'P' + s[1:]
s2 = s.replace('python', 'snakes')

print(s1)
print(s2)

# string functions
print(s.upper())

whitespace_s = '   snake    '
print(whitespace_s.strip(), s)

print(len(s))

# concatenating strings
s1 = 'Python'
s2 = 'and'
s3 = 'Snake'
print(s1 + ' ' + s3)
print(s1 + s2 * 3 + s3)
print(f'{s1} {s2 * 3} {s3}')

print(f'My name is {s1} {s2} im a {s3}')

s4 = s1 + s2 + s3
print('and' in s4)
print('if' in s4)

