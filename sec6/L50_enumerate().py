
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
            for item in todos:
                print(item)
        case'edit':
            number= int(input("Enter the nuber of a todo to edit: "))
            number = number -1
            new_todo = input(enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case _: # 1. for any other input discluding the offered ones
             print("The command is unknown.")
print("Bye!")

