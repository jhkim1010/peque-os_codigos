import PySimpleGUI as sg
from time import time
from random import randint

# game constantes   
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM

def convert_pos_to_pixel(cell):
    top_left = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE #(100, 100)
    button_right = top_left[0] + CELL_SIZE, top_left[1] + CELL_SIZE
    return top_left, button_right

def put_new_apple():
    apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    while apple_pos in snake_body:
        apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    return apple_pos
    
    
# snake 
snake_body = [(4,4), (3,4), (2,4)]
DIRECTIONS = {'left':(-1, 0), 'right':(1,0), 'up':(0, 1), 'down':(0,-1)}
current_direction = DIRECTIONS['up']
#APPLE 
apple_pos = (0,0)
apple_eaten = False

field = sg.Graph(
    canvas_size= (FIELD_SIZE,FIELD_SIZE), 
    graph_bottom_left=(0,0), 
    graph_top_right=(FIELD_SIZE,FIELD_SIZE), 
    background_color = 'black'
)

layout = [
    [sg.Text('k : Up, j : Down, l : Right, h  : Left', font = 'Calibri 20', expand_x = True, justification='center')],
    [field]
    ]

window = sg.Window('Snake', layout, return_keyboard_events=True)

start_time = time()

while True:
    event, values = window.read(timeout = 10)
#    print(event, values)
    
    if event == sg.WIN_CLOSED:        break
    if event in ('Left:37', 'h'):  current_direction = DIRECTIONS['left']
    if event in ('Up:38',   'k'):  current_direction = DIRECTIONS['up']
    if event in ('Right:39','l'):  current_direction = DIRECTIONS['right']
    if event in ('Down:40', 'j'):  current_direction = DIRECTIONS['down']
    
    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()
        
        if snake_body[0] == apple_pos: 
            apple_eaten = True
            # snake should grow up
            apple_pos = put_new_apple()

        # apple drawing
        tl, br = convert_pos_to_pixel(apple_pos)
        field.DrawRectangle(tl, br, 'red')

        tl, br = convert_pos_to_pixel(snake_body[-1])
        field.DrawRectangle(tl, br, 'black')
        
        # snake drawing
        # snake should move ... on ... depe nding timer...    
        new_head_x = snake_body[0][0] + current_direction[0]
        new_head_y = snake_body[0][1] + current_direction[1]
        
        if new_head_x > CELL_NUM :  new_head_x = 0
        if new_head_x == -1 :       new_head_x = CELL_NUM - 1 
        if new_head_y > CELL_NUM :  new_head_y = 0
        if new_head_y == -1 :       new_head_y = CELL_NUM - 1 
        
        new_head = ( new_head_x, new_head_y)
         
        if new_head in snake_body : 
            sg.popup('Dead...')
            break
            
        # print(current_direction)
        # print(new_head)
        snake_body.insert(0, new_head)
        if apple_eaten == False: snake_body.pop()
        print(snake_body)
        
        for index, part in enumerate(snake_body):
            tl, br = convert_pos_to_pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(tl, br, color)
        
        apple_eaten = False

window.close()