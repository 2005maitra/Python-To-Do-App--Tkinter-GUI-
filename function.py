FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the todo items from the file."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath=FILEPATH):
    """Write the todo items back to the file."""
    with open(filepath, "w") as file:
        file.writelines(todos)
