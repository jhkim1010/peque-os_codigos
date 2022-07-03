import PySimpleGUI as sg

layout = [
        [
            sg.Input(key='input_value'), 
            sg.Spin(['km to mile', 'kg to pound', 'secound to min'], key = 'unidades'),
            sg.Button('Convert', key = 'Button_convert')
        ],
        [sg.Text('Msg', key = 'result_string')]
        ]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Button_convert':
        original_value_to_convert = values['input_value']
        if original_value_to_convert.isnumeric():
            if values['unidades'] == 'km to mile':
                output =round(float(original_value_to_convert) * 0.6214, 2) 
                str_msg = f'{original_value_to_convert} km = {output} miles'
                # window['result_string'].update(str_msg)
            if values['unidades'] == 'kg to pound':
                output =round(float(original_value_to_convert) * 2.20462, 2) 
                str_msg = f'{original_value_to_convert} kg = {output} pound'
                # window['result_string'].update(str_msg)
            if values['unidades'] == 'secound to min':
                output =round(float(original_value_to_convert) / 60, 2) 
                str_msg = f'{original_value_to_convert} sec = {output} min'
            
            window['result_string'].update(str_msg)
        else:
            window['result_string'].update('Input value must be numeric')
        
window.close()