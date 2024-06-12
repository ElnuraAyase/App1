def get_todos(filepath = 'todos.txt'):
    ''' read a text file and return the list
     of the todo items.
    '''
    with open(filepath, 'r') as file_local:    #instead of read , we go to the filepath itself
        todos_local = file_local.readlines()
    return todos_local


# Function to write todos to file
def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos)

