import PySimpleGUI as sg

def main():
    
    MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY        # multiline element's key. Indicate it's an output only element
    MLINE_KEY2 = '-ML2-'+sg.WRITE_ONLY_KEY        # multiline element's key. Indicate it's an output only element
    MLINE_KEY3 = '-ML3-'+sg.WRITE_ONLY_KEY        # multiline element's key. Indicate it's an output only element

    output_key = MLINE_KEY


    layout = [  [sg.Text('Multiline Color Print Demo', font='Any 18')],
                [sg.Multiline('Multiline\n', size=(80,20), key=MLINE_KEY)],
                [sg.Multiline('Multiline2\n', size=(80,20), key=MLINE_KEY2)],
                [sg.Text('Text color:'), sg.Combo(list(color_map.keys()), size=(12,20), key='-TEXT COLOR-'),
                 sg.Text('on Background color:'), sg.Combo(list(color_map.keys()), size=(12,20), key='-BG COLOR-')],
                [sg.Input('Type text to output here', size=(80,1), key='-IN-')],
                [sg.Button('Print', bind_return_key=True), sg.Button('Print short'),
                 sg.Button('Force 1'), sg.Button('Force 2'),
                 sg.Button('Use Input for colors'), sg.Button('Toggle Output Location'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout)

    sg.cprint_set_output_destination(window, output_key)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Print':
            sg.cprint(values['-IN-'], text_color=values['-TEXT COLOR-'], background_color=values['-BG COLOR-'])
        elif event == 'Print short':
            sg.cprint(values['-IN-'], c=(values['-TEXT COLOR-'], values['-BG COLOR-']))
        elif event.startswith('Use Input'):
            sg.cprint(values['-IN-'], colors=values['-IN-'])
        elif event.startswith('Toggle'):
            output_key = MLINE_KEY if output_key == MLINE_KEY2 else MLINE_KEY2
            sg.cprint_set_output_destination(window, output_key)
            sg.cprint('Switched to this output element', c='white on red')
        elif event == 'Force 1':
            sg.cprint(values['-IN-'], c=(values['-TEXT COLOR-'], values['-BG COLOR-']), key=MLINE_KEY)
        elif event == 'Force 2':
            sg.cprint(values['-IN-'], c=(values['-TEXT COLOR-'], values['-BG COLOR-']), key=MLINE_KEY2)

    window.close() 
    
