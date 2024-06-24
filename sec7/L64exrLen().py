
# Write a program that reads the essay.txt file and returns the number of characters contained in the file.


a = open("essay.txt", 'r')
b = a.read()
print(len(b))
a.close()

     # another version

file = open("essay.txt", 'r')
content = file.read()
nr_chars = len(content)
print(nr_chars)

 # alternative 

# Use 'with' statement to open and read the file
with open("essay.txt", 'r') as a:
    b = a.read()
    print(len(b))
