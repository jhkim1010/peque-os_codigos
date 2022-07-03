import PySimpleGUI as sg 

sg.theme('Light Blue 2')

def collapse(layout, key, visible):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this section visible / invisible
    :param visible: visible determines if section is rendered visible or invisible on initialization
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layout, key=key, visible=visible, pad=(0,0)))

section1 = [[sg.Text('SVAS Log File', size=(15,1), key= 'txt_svas'), sg.Input(key='svas'), sg.FileBrowse(target= 'svas')]]
section2 = [[sg.Text('HSS Log File', size=(15,1)),                   sg.Input(key='hss'),  sg.FileBrowse()]]

layout = [[sg.Text('Choose files to get started', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
          [sg.Text('Select Logs you wish to validate', size=(30, 1), justification='left', font=("Helvetica", 15), relief=sg.RELIEF_RIDGE)],
          [sg.Text('_'  * 100, size=(65, 1))], 
          [sg.Checkbox('SVAS Log', size=(10,1), key='chk_svas', enable_events=True),  sg.Checkbox('HSS Log', size=(10,1), key = 'chk_hss', enable_events=True), sg.Checkbox('AOTA Log', size=(10,1), key = 'chk_aota'), sg.Checkbox('Nexus Log', size=(10,1), key = 'chk_nexus')],
          [sg.Button('Get Inputs')],
          [sg.Text('_'  * 100, size=(65, 1))], 
          [sg.Text('Request File', size=(15,1)), sg.Input(key='req'), sg.FileBrowse()],
          [collapse(section1, 'sec_1', False)],
          [collapse(section2, 'sec_2', False)],
          [sg.Text('AOTA Log File', size=(15,1)), sg.Input(key='aota'), sg.FileBrowse()],
          [sg.Text('Nexus Log File', size=(15,1)), sg.Input(key='nexus'), sg.FileBrowse()],
          [sg.Submit('Generate Logs'), sg.Cancel('Quit'), sg.Button('Reset')],
          [sg.Text('Generating Validation Logs...', size=(30,1), visible = False, key = 'progbar_head')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar', visible = False)]]

window = sg.Window('Provident Logs Validator', layout, size=(600, 400))

toggle_sec1 = toggle_sec2 = False

while True:
    event, values = window.read()

    if event == 'chk_svas':
        toggle_sec1 = not toggle_sec1
        window['sec_1'].update(visible=toggle_sec1)

    if event == 'chk_hss':
        toggle_sec2 = not toggle_sec2
        window['sec_2'].update(visible=toggle_sec2)

    if event == 'Quit':
        break
    print(event, values)