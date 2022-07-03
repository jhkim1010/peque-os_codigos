import PySimpleGUI as sg

menu_def = [['Layout', ['Layout1', 'Layout2']]]

font = ('Courier New', 11)
sg.set_options(font=font)

layout1 = [[sg.Text("Layout 1 text"), sg.Button('Test')]]
layout2 = [[sg.Text("Layout 2 text")], [sg.Button('Test')]]

layout = [
    [sg.Menu(menu_def, key='MENU')],
    [sg.Column(layout1, key='COL1'),
     sg.Column(layout2, key='COL2', visible=False)],
]
window = sg.Window("Title", layout, finalize=True)

col, col1, col2 = 1, window['COL1'], window['COL2']

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    print(event, values)
    if event == 'Layout1' and col != 1:
        col = 1
        col1.update(visible=True)
        col2.update(visible=False)
    elif event == 'Layout2' and col != 2:
        col = 2
        col2.update(visible=True)
        col1.update(visible=False)

window.close()