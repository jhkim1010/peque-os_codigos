import PySimpleGUI as sg

smile_signos = [
    'happy', [':)', 'xD', ':D', '<3'], 
    'sad', [':(', 'T_T'], 
    'other', [':3']
]

smile_evnets = smile_signos[1] + smile_signos[3] + smile_signos[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit'], 
    ['Tools', ['Word Count']], 
    ['Add', smile_signos]
]

sg.theme('GrayGrayGray')

layout = [
    [sg.Menu(menu_layout)]
    [sg.Text('Untitled', key = 'document_name')], 
    [sg.Multiline( no_scrollbar = True, size = (40, 30), key = 'document_context')]
    ]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if event == 'Word Count':
        full_text = values['document_context']
        word_count = full_text.replace('\n', '').split(' ')
        sg.popup(word_count)
        
window.close()