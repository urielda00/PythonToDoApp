# this project work on the terminal, managing task's list.
import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add" or "new"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            task_number = int(user_action[5:])
            task_number = task_number - 1
            todos = functions.get_todos()
            new_todo = input("Enter a new todo: ")
            todos[task_number] = new_todo + "\n"
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")  # for commands like "edit add ........."
            continue

    elif user_action.startswith('complete'):
        try:
            task_number = int(user_action[9:])
            todos = functions.get_todos()
            index = task_number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")  # error handling

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")
print("Bye!")
