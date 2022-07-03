import PySimpleGUI as sg
from pathlib import Path 

smile_signos = [
    'happy',[':)', ':P'], 
    'sad', [':<', 'T_T']
    ]

smile_evnets = smile_signos[1] + smile_signos[3]

file_menu_def = ['&File', ['Open', 'Save', '---', 'Exit']]
tools_menu_def= ['&Tools', ['Word Count']]
add_menu_def  = ['&Add', smile_signos]

layout = [
  #  [sg.Menu([file_menu_def, tools_menu_def, add_menu_def], tearoff=False, pad = (0,0))], 
    [sg.ButtonMenu('File', file_menu_def, key = 'file_menu'), sg.ButtonMenu('Tools', tools_menu_def, key = 'tools_menu'), sg.ButtonMenu('Add', add_menu_def, key = 'add_menu')],
    [sg.Text('FileName', key = 'file_name_msg')], 
    [sg.Multiline(no_scrollbar = True, size = (40,30), key = 'contenido_text_box')]
    ]

window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()
    print (event, values)
#    if event == 'file_menu':
    if values[event] == 'Exit':
        break

    if values[event] == 'Word Count':
        full_text = values['contenido_text_box']
        words_only = full_text.replace('\n', ' ').split(' ')
        word_count = len(words_only)
        char_count = len(''.join(words_only))
        sg.popup(f'words : {word_count}, char count :  {char_count} ')
        
    if values[event] in smile_evnets:
        print(values[event])
        full_text = values['contenido_text_box']
        full_text += ' '
        full_text += values[event]
        window['contenido_text_box'].update(full_text)
    
    if values[event] == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as =True)
        tmp_string = file_path.split('.')
        if len(tmp_string) == 1:
            # .txt 확장자가 없이 파일 이름만 들어옴. 
            file_path += '.txt'
        print(file_path, tmp_string)
#        file_path = sg.popup_get_file('Open', no_window=True)
        # if file_path:
        file_pointer = Path(file_path)
        file_pointer.write_text(values['contenido_text_box'])
        tmp_string = file_path.split('/')
        window['file_name_msg'].update(tmp_string[-1])
        #     contenido_de_archivo = file_pointer.read_text()
        #     tmp_string = file_path.split('/')
        #     print(tmp_string)
        #     window['file_name_msg'].update(tmp_string[-1])
        #     window['contenido_text_box'].update(contenido_de_archivo)
    
    if values[event] == 'Open':
        file_path = sg.popup_get_file('Open', no_window=True)
#        file_path = sg.popup_get_file('Open', no_window=True)
        if file_path:
            file_pointer = Path(file_path)
            contenido_de_archivo = file_pointer.read_text()
            tmp_string = file_path.split('/')
            print(tmp_string)
            window['file_name_msg'].update(tmp_string[-1])
            window['contenido_text_box'].update(contenido_de_archivo)

    if event == sg.WIN_CLOSED:
        break
    
window.close()