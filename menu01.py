#!/usr/bin/env python
import PySimpleGUI as sg
"""
    Demonstration of MENUS!
    How do menus work?  Like buttons is how.
    Check out the variable menu_def for a hint on how to 
    define menus
"""
dropdown1 = [[sg.Combo(['Choice 1', 'Choice 2', 'Choice 3'], default_value='Choice 1', enable_events=True, 
             key='drop1')]]

dropdown2= [[sg.Combo(['Choice A', 'Choice B', 'Choice C'], default_value='Choice A', enable_events=True, 
             key='drop2')]]

layout = [[sg.Column(dropdown1), sg.Column(dropdown2), sg.Button('Submit', enable_events = True, 
          key='Submit')]]

window = sg.Window('window',layout)

def choice1_choiceA():
    print('you chose 1 and A')

def choice1_choiceB():
    print('you chose 1 and B')

def choice1_choiceC():
    print('you chose 1 and C')

def other_choicecombos:
    print('etc')


while True:
     
     event, values = window.read()
     
     if event == ***choice 1*** and event == ***choice A*** and event =='Submit':
    
        choice1_choiceA
     
    if event == ***choice 1*** and event == ***choice B*** and event == 'Submit':
    
        choice1_choiceB

#### and so on and so forth for the rest of the options. I just don't know how to make it do this. I'm a novice programmer.

window.close()