# Imports
import PySimpleGUI as sg

sg.theme('DarkGrey9')


#Global Values
global smoker
global probe
global req_smoker
global req_probe



#smoker will be coded to read the temperature of internal smoker probe
smoker = 180

#probe will be coded to read the temperature of meat probe
probe = 100

req_smoker = int(input("Enter Desired Smoker Temperature: "))

req_probe = int(input("Enter Desired Finish Temperature: "))




if smoker < req_smoker and probe < req_probe:
#activate heating element
    print("Heating")
elif smoker >= req_smoker and probe < req_probe:
#turn off heating element
    print("maintain heat")
elif probe >= req_probe:
    req_smoker = req_probe
    print("Your meat is done!")


col1 = sg.Column([
    [sg.Frame('Smoker Temperature', [[sg.Text("10", font=["Helvetica", 100], text_color="#FF0000", justification="center")],
                                     [sg.Text("Heat Status", font=[48], justification="center", )]], size=(200, 300))],

    [sg.Frame('Req_Smoker Temperature', [[sg.Text("200", font=["Helvetica", 150])]], size=(200, 300))]
                ])

col2 = sg.Column([
    [sg.Frame('Probe Temperature', [[sg.Text("300", font=["Helvetica", 120])]], size=(200,300))],

    [sg.Frame('Finish Temperature', [[sg.Text("40", font=["Helvetica", 180])]], size=(200, 300))]
                ])

col3 = sg.Column([
    [sg.Frame("Options", [[sg.Button('Data-log'), sg.Button("Close"), ]], element_justification="center", size=(500, 100))]
                ])



layout = [[col1, col2], [col3]]

window = sg.Window('Smoker Display', layout, grab_anywhere=True, )

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break



window.close()