import PySimpleGUI as sg
from time import time

def create_window():        
    sg.theme('black')

    layout = [
#        [sg.Push(), sg.Image('cross.png', pad = 0, enable_events=True, key = 'close_img')],
#        [sg.VPush()],
        [sg.Text('0.0', font='Young 50', key = 'current_time_msg')], 
        [
            sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width=0, key = 'start_button'), 
            sg.Button('Lap',   button_color = ('#FFFFFF', '#FF0000'), border_width=0, key = 'lap_button', visible= False)
        ],
        [sg.Column([[]], key = 'msg_time_history')],
        [sg.VPush()]
        ]
    return sg.Window(
        'Stopwatch', 
        layout, size=(300, 300), 
        no_titlebar=True, 
        element_justification='center'
        )


window = create_window()

start_time = 0
activado = False
counter = 1 

while True:
    event, values = window.read(timeout=10)
    if event == (sg.WIN_CLOSED):
        break
    
    if event == 'start_button':
        if activado:
            # from activado to stop
            activado = False
            window['start_button'].update('Reset')
            window['lap_button'].update(visible = False)
            pass
        else :
            # from start to active
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                counter = 1
                pass
            else: 
                start_time = time()
                activado = True
                window['start_button'].update('Stop')
                window['lap_button'].update(visible = True)

    if event == 'lap_button':
        window.extend_layout(window['msg_time_history'], [[sg.Checkbox(counter), sg.VSeparator(), sg.Text(elapsed_time)]])
        counter += 1
       
    if activado:
        msg_time = time() - start_time
        print(msg_time)
        elapsed_time = round(time() - start_time, 1)
        print(elapsed_time)
        window['current_time_msg'].update(elapsed_time)
    
window.close()