import PySimpleGUI as sg
 
print(sg.Window('Get One Value', [[sg.Input(key = '-ONE_VALUE-'), sg.Button('OK'), sg.Button('Cancel')]]).read()) 
