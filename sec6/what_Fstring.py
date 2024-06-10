'''
Readability: F-strings are easier to read and write compared to older methods like str.format() or % formatting.
Performance: F-strings are generally faster than the other string formatting methods because they are evaluated at runtime.
Flexibility: You can include any valid Python expression inside the curly braces, not just variable
'''

name = "Alice"
age = 30

# Using an f-string to include variables in a string
greeting = f"Hello, my name is {name} and I am {age} years old."

print(greeting)

#another example on Console
item = 'place'
row = f"{index}-{item}"
row
#output
'1-place'
