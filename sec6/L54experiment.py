
#example 1
todos = []
while True:
    user_action = input("Type add, edit,  show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo= input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):                   
                row = f"{index+1}-{item}"                          
                print(row)
            print ("Hello!", index, item)            # output will print hello and last index and  item           
# output 
'''
1-work
2-write
3-eat
Hello! 3 eat 
'''

# example 2
myList= ['a','s', 'd']
for index,item in enumerate(myList):
    row = f"{index+1}-{item}"
    print(row)
print('Hello!', index, item)
# output
'''
1-a
2-s
3-d
Hello 2 d
'''
