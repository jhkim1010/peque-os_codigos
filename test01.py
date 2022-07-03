import PySimpleGUI as sg

txt2=""
#Initialize a holder variable 
fruits=['apple', 'orange', 'pears', 'tomatoes']

#Convert from List to Text with New line
for i in fruits:txt2=f"{fruits}{i}\n"

#Create layout
layout2 = [[sg.Multiline(txt2,size=(28,28),key='-Items-'),],[sg.Ok()] ]

#Single shot Popup Window
sg.Window('Scroll to see the whole list of fruits', layout2,finalize=True).read(close=True)