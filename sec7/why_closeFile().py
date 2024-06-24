'''
some parts of the code may interract with each other and change the content of the file.
so it is better to close thr file or use with statement:
'''
a = open("essay.txt", 'r')
b = a.read()
print(b.title())

a.close()
