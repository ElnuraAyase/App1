'''
some parts of the code may interract with each other and change the content of the file.
so it is better to close thr file or use with statement:
'''
a = open("essay.txt", 'r')
b = a.read()
print(b.title())

a.close()

# other examples

file = open("bear.txt")
content = file.read()
print(content)
file.close()   # not forget to close, otherwise data leakacge 

'''
task 
On the side panel there's a bear.txt file. The existing code opens that file in read mode.

Below that code, please read the file content and print out the content.
'''

with open("bear.txt", 'r') as file:   # with statement
    content = file.read()
    print(content)
