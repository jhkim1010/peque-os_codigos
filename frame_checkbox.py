import PySimpleGUI as sg

def Text(text, size, justification, expand_x=None, key=None):
    return sg.Text(text, size=size, pad=(1, 1), expand_x=expand_x,
        justification=justification, key=key)

def line_frame(index, number, description, amount):
    font1 = ("Courier New", 16)
    frame_layout = [
        [Text("Product #", 10, 'c'), Text(number, 12, 'l', key='t'),
         Text("Amount",     7, 'c'), Text(amount, 10, 'r'),],
        [Text(description, (39, 3), 'l', expand_x=True)],
    ]
    layout = [
        [sg.Checkbox('Print', font=font1, enable_events=True, key=f'Print {index}'),
         sg.Frame('', frame_layout, pad=((0, 5), (0, 5)), relief=sg.RELIEF_FLAT, background_color='#4b5a69'),],
    ]
    return sg.Frame(f'Line {index:0>4d}', layout, pad=((0, 5), 0))

data = [
    ('REQ0011118', 'USB', 1),
    ('REQ0011932', 'Tire Disposal '*5, 2),
    ('REQ0011476', 'Labor', 4.5),
    ('4500236642', 'None', 'None' ),
    ('4500221028', 'Toner', 1),
    ('4500253427', 'None', 'None'),
    ('REQ0013911', 'HP 35A BLACK TONER '*4, 30),
    ('12-64006.01', 'Radiation Oncology '*3, 1),
    ('REQ0014515', 'Black Toner Cartridge for CLJ 4700 '*5, 16),
    ('4500200308', '1" ss 90* elbow , threaded', 4),
]

font = ("Courier New", 11)
sg.theme("DarkBlue3")
sg.set_options(font=font, )

column_layout = [
    [line_frame(i+1, number, description, amount)]
        for i, (number, description, amount) in enumerate(data)
]
layout = [
    [sg.Column(column_layout, scrollable=True, vertical_scroll_only=True)],
]
window = sg.Window("test", layout, margins=(0, 0), finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    print(event, values)
window.close()