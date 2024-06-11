

#todos = []  # delete this list as we don't need it, for storing files in a new txt file

while True:
    user_action = input("Type add, edit,  show, remove or exit: ").lower().strip()
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"      # back slash n is a break line, it is better to use it in print( 'hi' + '\n'
            if todo.lower() != 'x':
                file = open('todo.txt', 'r')           # to read the file that stored items
                todos = file.readlines()                # reads and create lists of each line
                file.close()
                todos.append(todo)

                file = open('todo.txt',
                            'w')                             # 'w' overwrites the file ,doesn't store the previous # open function for file object, for read you add 'r' for write 'w'
                file.writelines(todos)                       # file method for file objects
                file.close()    
        case 'show':
            with open('todo.txt', 'r') as file:                # to read the file that stored items
                todos = file.readlines()                         # reads and creates lists of each line
            if todos:
                for index, item in enumerate(todos):
                    row = f"{index + 1}-{item}"
                    print(row)
            else:
                print("The list is empty, try add a todo ")
                todo = input("enter a todo, (or press 'x' to go back): ").strip()
                if todo.lower() !='x':
                    todos.append(todo)
        case'edit':
            with open('todo.txt', 'r') as file:                     # to read the file that stored items
                todos = file.readlines()                            # reads and creates lists of each line
            if todos:
                while True:
                    number = (input("Enter the number of a todo to edit(or press 'x' to go back): "))
                    if number.lower() == 'x':
                        break
                    try:
                        number = int(number) -1
                        if 0 <= number < len(todos):
                            new_todo = input("Enter new todo, or 'x' to go back: ").strip()
                            todos[number] = new_todo
                            break
                        else:
                            print("Invalid number, enter a lower number ")
                    except ValueError:
                        retry = input("Enter a valid number or enter 'x',to go back: ").lower().strip()
            else:
                print("list is empty,there is nothing to edit, try to add a todo")
                todo = input("enter a todo, (or press 'x' to go back): ").strip()
                if todo.lower() !='x':
                    todos.append(todo)
        case 'remove':                                             
            with open('todo.txt', 'r') as file:                       # to read the file that stored items
                todos = file.readlines()                              # reads and creates lists of each line
            if todos:
                while True:
                    try:
                        number = (input("Enter number of todo to delete: "))  
                        if number.lower() == 'x':
                            break
                        number = int(number)-1
                        if 0 <= number < len(todos):
                            new_todo = input("Enter new todo, or 'x' to go back: ").strip()
                            todos[number]= new_todo
                            break
                        else:
                            print("Invalid number, enter a lower number ")
                    except ValueError:
                        retry = input("Enter a valid number or enter 'x',to go back: ")

            todos.pop(number)
        case 'exit':
            break
        case _: # 1. for any other input discluding the offered ones
             print("The command is unknown.")
print("Bye!")

