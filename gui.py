import time
import functions
import FreeSimpleGUI

# Configurations:
FreeSimpleGUI.theme("DarkGrey")
label = FreeSimpleGUI.Text("Type in a to-do")
clock = FreeSimpleGUI.Text("", key="clock")
input_box = FreeSimpleGUI.InputText(tooltip="Enter to-do", key="todo")

# Buttons:
add_button = FreeSimpleGUI.Button("Add")
exit_button = FreeSimpleGUI.Button("Exit")
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")

list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(),
                                 key="todos",
                                 enable_events=True,
                                 size=[45, 10])

window = FreeSimpleGUI.Window("My to-do App",
                              layout=[[clock],
                                      [label], [input_box, add_button],
                                      [list_box, edit_button, complete_button],
                                      [exit_button]],

                              font=("Helvetica", 20))

while True:
    event, values = window.read()  # timeout=200
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    print(event)
    print(values)
    print(values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)

            except IndexError:
                FreeSimpleGUI.popup("please select an item first", font=("Helvica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todos"].update(value="")

            except IndexError:
                FreeSimpleGUI.popup("please select an item first", font=("Helvica", 20))
        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case FreeSimpleGUI.WINDOW_CLOSED:
            break

window.close()
