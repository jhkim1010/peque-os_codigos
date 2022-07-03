import PySimpleGUI as sg
from pytube import YouTube
# import get_one_value as g1

start_layout = [[sg.Input(key = '-INPUT-'), sg.Button('Submit')]]

sg.set_options(font = 'Calibri 16')
#sg.Print(start_layout)

info_tab = [
    [sg.Text('Title :'), sg.Text('', key = '-TITLE-')], 
    [sg.Text('Length :'), sg.Text('', key = '-LENGTH-')], 
    [sg.Text('Views :'), sg.Text('', key = '-VIEWS-')], 
    [sg.Text('Author :'), sg.Text('', key = '-AUTHOR-')], 
    [sg.Text('Description :'), sg.Multiline('', key = '-DESCRIPTION-', size =(40,20), no_scrollbar = True, disabled =True)], 
]

download_tab = [
    [sg.Frame('Best Quality',  [[sg.Button('Download', key = '-BEST-'),  sg.Text('', key = '-BEST_RES-'),  sg.Text('', key = '-BEST_SIZE-')]])], 
    [sg.Frame('Worst Quality', [[sg.Button('Download', key = '-WORST-'), sg.Text('', key = '-WORST_RES-'), sg.Text('', key = '-WORST_SIZE-')]])], 
    [sg.Frame('Audio',         [[sg.Button('Download', key = '-AUDIO-'),                                   sg.Text('', key = '-AUDIO_SIZE-')]])], 
    [sg.VPush()], 
    [sg.Progress(100, size = (20,20), expand_x = True, key = '-PROGRESS_BAR-')]
]

layout = [
    [sg.TabGroup([[
        sg.Tab('Info', info_tab), sg.Tab('Download', download_tab)
    ]])]
    ]

window = sg.Window('Youtube Downloader', start_layout)
 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Submit': 
        video_url = values['-INPUT-']
        window.close()
#        print('URL : ', video_url)
        
        if video_url == '' : 
            sg.popup('NO info entrado..\nPrograma va a ser cerrado..')
            break 

        window = sg.Window('Youtube Downloader', layout, finalize = True)
        video_object = YouTube(video_url)
  
        # info
        play_time_min = 0
        window['-TITLE-'].update(       video_object.title)
        play_time_hour = int(round(     video_object.length / 3600, 0))
        play_time_min  = (video_object.length - (play_time_hour * 3600)) / 60
# #        print(play_time_hour, play_time_min)
        window['-LENGTH-'].update(f'{play_time_hour} hours {round(play_time_min, 2)} min') # hours {round(video_object.length / 60, 2)} minutes')
        window['-VIEWS-'].update(       video_object.views)
        window['-AUTHOR-'].update(      video_object.author)
        window['-DESCRIPTION-'].update( video_object.description)

        # download
#        filesize_highest = video_object.streams.get_highest_resolution().filesize   / 1048576
#        print(filesize_highest)
#        window['-BEST_SIZE-'].update( f'{round( filesize_highest , 1 )} MB') 
#        window['-BEST_RES-'].update(             video_object.streams.get_highest_resolution().resolution ) 
        
#        print(video_object.title)
#        window['-LENGTH-'].update(video_object.length)
    if event == '-BEST-': 
        video_object.streams.get_highest_resolution().download()
    #     pass
    
    if event == '-WORST-': 
        video_object.streams.get_lowest_resolution().download()
    #     pass
    
    if event == '-AUDIO-': 
        video_object.streams.get_audio_only().download()
    #     pass
    
window.close()