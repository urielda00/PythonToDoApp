FILE_PATH = "todos.txt"

# Read a text file and return this list of to-do items
def get_todos(filepath=FILE_PATH):
    """Read a text file and return this list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

# Write the to-do items list in the text file
def write_todos(todos_arg, filepath=FILE_PATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


# print(help(get_todos))
# print(help(write_todos))