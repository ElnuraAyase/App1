file = open("bear.txt")
content = file.read()
print(content)
file.close()   # not forget to close, otherwise data leakacge 
'''
task 
On the side panel there's a bear.txt file. The existing code opens that file in read mode.

Below that code, please read the file content and print out the content.
'''

with open("bear.txt", 'r') as file:
    content = file.read()
    print(content)

