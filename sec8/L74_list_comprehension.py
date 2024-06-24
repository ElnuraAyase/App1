
#todos = []      # delete this list as we don't need it, for storing files in a new txt file

while True:
    user_action = input("Type add, edit,  show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"   # back slash n is a break line, it is better to use it in print( 'hi' + '\n'

            file = open('todo.txt', 'r')           # to read the file that stored items
            todos = file.readlines()               # reads and create lists of each line
            file.close()
            todos.append(todo)

            file = open('todo.txt', 'w')            # 'w' overwrites the file ,doesn't store the previous # open function for file object, for read you add 'r' for write 'w'
            file.writelines(todos)                  #file method for file objects
            file.close()
        case 'show':
            file = open('todo.txt', 'r')           # to read the file that stored items
            todos = file.readlines()  # reads and create lists of each line
            file.close()
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number= int(input("Enter the nuber of a todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter number of todo to delete: "))
            todos.pop(number -1 )
        case 'exit':
            break
        case _: # 1. for any other input discluding the offered ones
             print("The command is unknown.")
print("Bye!")
