import functions
import PySimpleGUI as sg
import time

themes = ["Black", "Default", "DarkBlue3", "LightBlue3",
          "LightBrown2", "LightBrown8", "LightBrown11",
          "LightGreen", "DarkGreen", "GreenMono",
          "DarkTeal7", "SandyBeach"]          # for colorblind people and less distracting purpose
current_theme_index = 0


def create_window(theme):
    sg.theme(theme)

    clock = sg.Text('', key="clock")
    label = sg.Text("Add your To-Do")
    input_box = sg.InputText(tooltip="Enter todo", key="todo")
    add_button = sg.Button("Add")
    list_values = [f"{i + 1}. {todo}" for i, todo in enumerate(functions.get_todos())]  # add numbered list items
    list_box = sg.Listbox(values=list_values, key='todos',
                          enable_events=True, size=[40, 8])   # changed size
    edit_button = sg.Button("Edit")
    remove_button = sg.Button("Remove")
    theme_dropdown = sg.Combo(themes, default_value=theme, key='theme_dropdown', readonly=True, enable_events=True)
    exit_button = sg.Button("Exit")

    timer_text = sg.Text('00:00:00', key='timer')
    start_button = sg.Button("Start")
    pause_button = sg.Button("Pause")
    stop_button = sg.Button("Stop")

    layout = [
        [sg.Column([[exit_button, theme_dropdown]], justification='right')], #place on the right side
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, remove_button],
        [timer_text],
        [start_button, pause_button, stop_button],  # clear the code with listing to make it more visible
    ]

    return sg.Window('To-Do List and Time Tracker App', layout, font=('Helvetica', 17))


window = create_window(themes[current_theme_index])                 # must be at lease 1 selected theme

timer_running = False
timer_start_time = 0
elapsed_time = 0

while True:
    event, values = window.read(timeout=200)

    window["clock"].update(value=time.strftime("%b, %d, %Y, %H:%M:%S"))  # always update clock

    if timer_running:  #  timer update
        elapsed_time = int(time.time() - timer_start_time)
        window['timer'].update(f'{elapsed_time // 3600:02}:{(elapsed_time % 3600) // 60:02}:{elapsed_time % 60:02}')

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    print(1, event)
    print(2, values)
    if 'todos' in values:
        print(3, values['todos'])
    else:
        print(3, 'No todos key in values')

    match event:
        case "Add":
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.get_todos()
                todos.append(new_todo)
                functions.write_todos(todos)
                list_values = [f"{i + 1}. {todo}" for i, todo in enumerate(todos)] # enumerate for list with numb
                window['todos'].update(values=list_values)
                window['todo'].update(value='')  # emepties the list
            else:
                sg.popup("Please enter a todo item", font=("Helvetica", 16))

        case "Edit":
            try:
                if values['todos']:
                    selected_index = int(values['todos'][0].split('.')[0]) - 1
                    todos = functions.get_todos()
                    todo_to_edit = todos[selected_index].strip()

                    new_todo = sg.popup_get_text(f"Edit Todo Item", default_text=todo_to_edit.strip(),
                                                 font=("Helvetica", 16)) #size changed
                    if new_todo is not None:
                        todos[selected_index] = new_todo.strip()
                        functions.write_todos(todos)
                        list_values = [f"{i + 1}. {todo}" for i, todo in enumerate(todos)]   # enumarated for better visuality
                        window['todos'].update(values=list_values)
                        window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16))  # if eror with number
            except ValueError:                                                     # expected errors here
                sg.popup("Invalid selection", font=("Helvetica", 16))

        case "Remove":                  # name changed from complete to remvoe
            try:
                if values['todos']:
                    selected_index = int(values['todos'][0].split('.')[0]) - 1
                    todos = functions.get_todos()
                    todo_to_remove = todos[selected_index]

                    confirm_remove = sg.popup_yes_no(f"Are you sure you want to remove:\n\n{todo_to_remove}",
                                                     font=("Helvetica", 16))
                    if confirm_remove == 'Yes':     # user friendly ,to check up if the action really needed to be done
                        todos.pop(selected_index)
                        functions.write_todos(todos)
                        list_values = [f"{i + 1}. {todo.strip()}" for i, todo in enumerate(todos)]
                        window['todos'].update(values=list_values)
                        window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16))
            except ValueError:
                sg.popup("Invalid selection", font=("Helvetica", 16))

        case 'theme_dropdown':   # added dropdown button, changed from usual button
            selected_theme = values['theme_dropdown']
            current_theme_index = themes.index(selected_theme)
            new_theme = themes[current_theme_index]   # changing to new one
            window.close()
            window = create_window(new_theme)   # save the theme

        case "Start":
            if not timer_running:
                timer_running = True
                timer_start_time = time.time() - elapsed_time   # error fixed

        case "Pause":
            if timer_running:
                timer_running = False
                elapsed_time = int(time.time() - timer_start_time)

        case "Stop":
            timer_running = False
            elapsed_time = 0
            window['timer'].update('00:00:00') # timer visuality here

        case 'todos':
            timer_running = False
            elapsed_time = 0
            window['timer'].update('00:00:00')
            if values['todos']:
                window['todo'].update(value=values['todos'][0].split('. ')[1])  # d isplaying selected item in input box
            else:
                window['todo'].update(value='')  # leave empty

window.close() # added ) as it wasn't here
