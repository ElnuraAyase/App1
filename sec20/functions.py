FILEPATH = "todos.txt"  # for easy name change from todos.txt ot todos_reach.txt etc


def get_todos(filepath=FILEPATH):                 # change here
    '''  read a text file and return the list
     of the todo items.
    '''
    with open(filepath, 'r') as file_local:    #instead of read , we go to the filepath itself
        todos_local = file_local.readlines()
    return [todo.strip() for todo in todos_local]


# Function to write todos to file
def write_todos(todos_arg, filepath=FILEPATH):           # change here
    with open(filepath, 'w') as file:
        file.writelines([todo + "\n" for todo in todos_arg])

if __name__ == "__main__":   # fixed typo  from "__name__" to
    print(get_todos())