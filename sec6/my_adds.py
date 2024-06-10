
# replacing todo for the edit choice
todos = []

while True:
    user_action = input("Type add, edit,  show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo= input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            if todos:
                for index, item in enumerate(todos) :
                    print(index +1, '-', item)# enumerate()
            else:
                print("The list is empty, try add a todo ")
                todo = input("enter a todo, (or press 'x' to go back): ").strip()
                if todo.lower() !='x':
                    todos.append(todo)
        case'edit':
            if todos:
                while True:
                    try:
                        number = int(input("Enter the number of a todo to edit: "))
                        number = number -1
                        if 0 <= number < len(todos):                             
                            new_todo = input("Enter new todo: ")
                            todos[number] = new_todo
                            break
                          # all new lines 
                        else:
                            print("Invalid number, enter a lower number ")               
                    except ValueError:
                        retry = input("Enter a valid number or enter 'x',to go back: ").lower().strip()
                        if retry == 'x':
                            break
                else:
                    print("list is empty,there is nothing to edit, try to add a todo")
                    todo = input("enter a todo, (or press 'x' to go back): ").strip()
                    if todo.lower() !='x':
                        todos.append(todo)

        case 'exit':
            break
        case _: # 1. for any other input discluding the offered ones
             print("The command is unknown.")
print("Bye!")

