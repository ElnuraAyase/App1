import datetime
import os
from functions import  get_todos, write_todos
"""
or use : MODULE
import functions 
and in line 14 
functions.get_todos()
"""
while True:
    user_action = input("Type add, edit, show, remove, start, stop, or exit: ").lower().strip()
    if user_action.startswith("add"):          #startswith    to simplify the code
        todo = user_action[4:]                 # if conditional slicing
        if todo.lower() != 'x':
            todos = get_todos()    # for import function
            todos.append(todo + '\n')
            write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        if todos:
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item.strip()}"
                print(row)
        else:
            print("The list is empty, try adding a todo.")
    elif user_action.startswith("edit"):
        todos = get_todos()
        if todos:
            while True:
                number = input("Enter the number of a todo to edit (or press 'x' to go back): ")
                if number.lower() == 'x':
                    break
                try:
                    number = int(number) - 1
                    if 0 <= number < len(todos):
                        new_todo = input("Enter new todo, or 'x' to go back: ").strip()
                        if new_todo.lower() == 'x':
                            break
                        todos[number] = new_todo + "\n"
                        write_todos(todos)
                        break
                    else:
                        print("Invalid number, enter a valid number.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("The list is empty, there is nothing to edit. Try adding a todo.")
    elif user_action.startswith("remove", "delete"):
        todos = get_todos()
        if todos:
            while True:
                number = input("Enter the number of a todo to delete (or press 'x' to go back): ")
                if number.lower() == 'x':
                    break
                try:
                    number = int(number) - 1
                    if 0 <= number < len(todos):
                        todos.pop(number)
                        write_todos(todos)
                        break
                    else:
                        print("Invalid number, enter a valid number.")
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("The list is empty, there is nothing to remove. Try adding a todo.")
    elif user_action.startswith("start"):
        todos = get_todos()
        if todos:
            number = input("Enter the number of a todo to start timing: ")
            try:
                number = int(number) - 1
                if 0 <= number < len(todos):
                    start_time = datetime.datetime.now()
                    with open('timer.txt', 'w') as timer_file:
                        timer_file.write(f"{number}\n{start_time}\n")
                    print(f"Timer started for: {todos[number].strip()}")
                else:
                    print("Invalid number, enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("The list is empty, there is nothing to time. Try adding a todo.")

    elif user_action.startswith("stop"):
        try:
            with open('timer.txt', 'r') as timer_file:
                lines = timer_file.readlines()
            number = int(lines[0].strip())
            start_time = datetime.datetime.fromisoformat(lines[1].strip())
            end_time = datetime.datetime.now()
            elapsed_time = end_time - start_time
            print(f"Time spent on '{todos[number].strip()}': {elapsed_time}")
            os.remove('timer.txt')
        except FileNotFoundError:
            print("No timer is running.")
        except ValueError:
            print("Error reading timer data.")

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("_"):
        print("The command is unknown.")
print("Bye!")

