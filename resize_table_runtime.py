import PySimpleGUI as sg
from http import HTTPStatus

my_table = [[int(k), k.description] for _, k in enumerate(HTTPStatus)]
headings = ["HTTP Result Code", "HTTP Result Description"]
layout = [[sg.Text('Please enter Something Interesting')],
          [sg.Text('Input Field'), sg.InputText('name', key='_NAME_')],
          [sg.Table(values=my_table, headings=headings, auto_size_columns=True,
                    display_row_numbers=True, num_rows=20, enable_events=True,
                    justification='left', key='_TABLE_')],
          [sg.Submit(), sg.Cancel(key='Cancel')]]

window = sg.Window('Simple data entry GUI', auto_size_text=True, auto_size_buttons=True,
                   grab_anywhere=False, resizable=True,
                   layout=layout, finalize=True)
window['_TABLE_'].expand(True, True)
window['_TABLE_'].table_frame.pack(expand=True, fill='both')
while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break
    print(f"Event:{event}; Values:{values}")

window.Close()