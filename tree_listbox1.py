import PySimpleGUI as sg
import random
import string

def LBox(values, key):
    return sg.Listbox(values, enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED , size=(10,len(values)), pad=(0,0), no_scrollbar=True, key=key)

values = [''.join(random.choice(string.ascii_lowercase) for i in range(10)) for _ in range(6)]

layout = [  [LBox(values, 10),LBox(values, 11), LBox(values, 12)],
            [sg.Button('Do Something'), sg.Button('Exit')] ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event in (10,11,12):
        indexes = window[event].GetIndexes()
        for key in (10,11,12):
            window[key].Update(set_to_index=indexes)              
window.Close()