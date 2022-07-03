#!/usr/bin/env python3
import PySimpleGUI as sg

print ('GUI')
window = sg.Window('test', default_element_size=(40, 1), grab_anywhere=False)      
frame_layout = [
    [sg.Checkbox('On', change_submits = True, enable_events=True, default='0',key='print_output')],
    [sg.Listbox(values=[1,2,3], background_color='gray', disabled = False, key='_printer_pref_', size=(60, 6))],
]
layout = [
	[sg.Frame('Nataveni', frame_layout, font='Any 12', title_color='black')], 		     
	[sg.Submit(), sg.Cancel()]
	]
event, values = window.Layout(layout).Read()
# window.FindElement('_printer_pref_').Update(disabled = True)
print (event, values)
while True:
	button, values = window.Read()
	if event == 'print_output':
		window.FindElement('_printer_pref_').Update(disabled = True)
	elif event != 'print_output':
		window.FindElement('_printer_pref_').Update(disabled = False)
		# window.FindElement('print_output').Update(disabled= True)
window.Close()
print (values['print_output'])