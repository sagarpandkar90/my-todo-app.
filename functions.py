def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

