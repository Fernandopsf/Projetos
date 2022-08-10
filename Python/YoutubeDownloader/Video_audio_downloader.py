from pytube import YouTube
import PySimpleGUI as sg

sg.theme('DarkBlue')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [
    
    [sg.Text('URL',size=(15,0)),sg.Input(size=(15,0),key='url')],
    [sg.Text('Salvar na Pasta',size=(15,0)),sg.Input(size=(15,0),key='save'), sg.FolderBrowse()],
    [sg.Button ('Video'),sg.Button ('Audio'),sg.Button ('Sair')]]


# Create the Window
window = sg.Window('Youtube Download', layout)
# Event Loop to process "events"


while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
   
            
            
    url = values['url']
    saving = values['save']
    
    if event == 'Video':
        yt = YouTube(url)
        y_res = yt.streams.get_highest_resolution()
        y_res.download(saving)
    
    if event == 'Audio':
        yt = YouTube(url)
        y_res = yt.streams.get_audio_only()
        y_res.download(saving)


window.close()

