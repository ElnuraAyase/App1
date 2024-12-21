# wrong version 
user_promt = "enter the task: "

while True:
  todo = input(user_promt)  
  todos = [todo]  # this will clean the list and overwrite when loop is renewed
print(todos)


"""
corrected by adding method append, methods like functions have () , but written with .
and attached to datatypes, here the append method is a part of variable
"""


user_promt = "enter the task: "

todos [] #empty listoutside the loop 

while True:
  todo = input(user_promt)  
  todos.append(todo) #add all todo to a list with todos


'''
Mistake if you append method .append  to a string , it will give an error as it can append the list ,not the string
print(todos)
'''
# we can use different method for a string , let it be capitalize method 

user_promt = "enter the task: "

todos [] #empty listoutside the loop 

while True:
  todo = input(user_promt)  
  print(todo.capitalize())  # don't forget print as a function to show the results
  todos.append(todo) #add all todo to a list with todos
