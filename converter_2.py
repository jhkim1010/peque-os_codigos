# converte 2 sample

import PySimpleGUI as sg 

layer = [
    [sg.Text("Cantidad"), sg.Input('input_cantidad', size=(10)), sg.Text("Codigo"), sg.Input('input_codigo', size=(10)), sg.Text("Descripcion"), sg.Input('input_descripcion'), sg.Button('Agregar', key = 'agregar_boton')],
    [sg.Listbox(values=[''], select_mode='single', key = 'list1', size = (100, 5) )],
    [sg.Text("Msg", key = 'msg_status', size = (100))]
]

window = sg.Window("Colibri", layer)

while True:
    event, value = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break 
    
    if event == 'agregar_boton':
        # msg_status = f'Good'
        window['msg_status'].update('Good')
        # print(msg_status)
        
    


window.close()