import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
                [sg.pin(sg.Text('\n\nText sample', key = '_text_', visible = True))],
                [sg.Text('Second sample: ', key = '_text2_'), sg.InputText(key='_IN_', size=(10, 1))],
                [sg.Text()],

                [sg.Button('Confirm', key = '_CONFIRM_', visible=True),
                sg.pin(sg.Button('1', key = '_1_', visible=False)),
                sg.pin(sg.Button('2', key = '_2_', visible=False)),
                sg.pin(sg.Button('3', key = '_3_', visible=False)),
                sg.Cancel('Exit', key = '_EXIT_')],

            ]

window = sg.Window('Window', layout)


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '_EXIT_'):
        break

    elif '_CONFIRM_' in event:
        window['_text_'].Update(visible = False)
        window['_text2_'].Update('Second text updated')


        window['_EXIT_'].Update(visible = False)
        window['_CONFIRM_'].Update(visible = False)

        window['_1_'].Update(visible = True)
        window['_2_'].Update(visible = True)
        window['_3_'].Update(visible = True)
        window['_EXIT_'].Update(visible = True)

window.close()