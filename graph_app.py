import PySimpleGUI as sg
import matplotlib as pl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import axes

def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y, 'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()
    
sg.theme('DarkTeal6')
table_content = []

layout = [
    [sg.Table(
        headings = ['Observation', 'Result'], 
        values = table_content, 
        expand_x = True, 
        hide_vertical_scroll= True,
        key= '-table-')], 
    [sg.Input(key = '-Input-', expand_x = True, ), sg.Button('Submit')], 
    [sg.Canvas(key = '-CANVAS-')]
    ]

window = sg.Window('Graph App', layout, finalize=True)

# matplotlib
fig = pl.figure.Figure(figsize=(5,4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Submit':
        new_value = values['-Input-']
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            sg.Print(table_content)
            window['-table-'].update(table_content)
            window['-Input-'].update('')
            update_figure(table_content)
            
window.close()