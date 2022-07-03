from ctypes import alignment
import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibri 14', button_element_size= (6,3) )
    button_size_1 = (16,3)
    button_size_2 = (5,3)

    layout = [
        [sg.Text('', key="full_operation_str")], 
        [sg.Text(
            '0', 
            font = 'Calibri 50', 
            justification= 'right', 
            expand_x = True, 
            pad = (10, 30), 
            right_click_menu= theme_menu, 
            key = 'result_str'
            )], 
        [sg.Button('Clear', expand_x= True), sg.Button('Enter', expand_x= True)],
        [sg.Button('7', size = button_size_2), sg.Button('8', size = button_size_2), sg.Button('9', size = button_size_2), sg.Button('*', size = button_size_2)],
        [sg.Button('4', size = button_size_2), sg.Button('5', size = button_size_2), sg.Button('6', size = button_size_2), sg.Button('/', size = button_size_2)],
        [sg.Button('1', size = button_size_2), sg.Button('2', size = button_size_2), sg.Button('3', size = button_size_2), sg.Button('-', size = button_size_2)],
        [sg.Button('0', expand_x= True), sg.Button('.', size = button_size_2), sg.Button('+', size = button_size_2)]
        ]
    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['LigthGreay1', 'dark', 'DarkGray8', 'random']]
window = create_window('dark')
current_number = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
        
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.' ]:
        current_number.append(event)
        print(current_number)
        str_number = ''.join(current_number)
        print(str_number)
        window['result_str'].update(str_number)
        
    if event in ['+', '-', '/', '*']:
        full_operation.append(''.join(current_number))
        current_number = []
        full_operation.append(event)
        print(full_operation)
        window['result_str'].update('')
        result_str1 = ''.join(full_operation)
        window['full_operation_str'].update(result_str1)

    if event in ['Clear']:
        current_number = []
        full_operation = []
        window['result_str'].update('')
        window['full_operation_str'].update('')

    if event in ['Enter']:
        print(full_operation)
        full_operation.append(''.join(current_number))
        print(full_operation)
        window['result_str'].update('')
        result_str1 = ''.join(full_operation)
        window['full_operation_str'].update(result_str1)
        result = eval(result_str1)
        window['result_str'].update(result)
        
        
window.close()