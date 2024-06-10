
todos = []

while True:
    user_action = input("Type add, edit,  show, remove or exit: ").lower().strip()
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo= input("Enter a todo or press 'x' to go back: ")
            if todo.lower() != 'x':
                todos.append(todo)
        case 'show':
            if todos:
                for index, item in enumerate(todos):   # enumerate() gives an index of the item
                    row = f"{index + 1}-{item}"         #f string - formated string literal, for python 3.6
                    print(row)
            else:
                print("The list is empty, try add a todo ")
                todo = input("enter a todo, (or press 'x' to go back): ").strip()
                if todo.lower() !='x':
                    todos.append(todo)
        case'edit':
            if todos:
                while True:
                    number = input("Enter the number of a todo to edit(or press 'x' to go back): ")
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
        case 'remove':                                                                              # remove - delete statment
            if todos:
                while True:
                    try:
                        number = input("Enter number of todo to delete: ")  # for number, as pop removes numbers
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

