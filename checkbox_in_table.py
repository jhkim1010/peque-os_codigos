
#!/usr/bin/env python3
import PySimpleGUI as sg

sg.theme('Dark Red')
TaggerList = ["viking", "saddle", "beast", "ze", "princess", "vet", "art", "two", "hood", "mosaic",
              "viking1", "saddle1", "beast1", "ze1", "princess1", "vet1", "art1", "two1", "hood1", "mosaic1"]

TaggerListLen = len(TaggerList)
Tags1 = TaggerList[:int(TaggerListLen/3)]
Tags2 = TaggerList[int(TaggerListLen/3):int(TaggerListLen/3*2)]
Tags3 = TaggerList[int(TaggerListLen/3*2):]


def CBtn(BoxText):
    return sg.Checkbox(BoxText, size=(8, 1), default=False)

column2 = [[sg.Text('Column 2', justification='center', size=(10, 1))], [CBtn(Bx) for Bx in Tags2]]

column5 = sg.Column([[sg.Checkbox("BoxText1", size=(12, 1), default=False)],
            [sg.Checkbox("BoxText2", size=(12, 1), default=False)],
            [sg.Checkbox("BoxText3", size=(12, 1), default=False)],
            [sg.Checkbox("BoxText4", size=(12, 1), default=False)]])

menu_def = ['file',['save', 'open'],]

layout = [
    [sg.Menu(menu_def)],
    [sg.Text('Image Tagger', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Your Folder', size=(15, 1), justification='right'),
        sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Column(column2)],
    [column5]
]

window = sg.Window('Everything bagel', layout)


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
                
window.close()