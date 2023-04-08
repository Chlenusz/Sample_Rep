""""
from pytube import YouTube
from tkinter import * 
from tkinter import ttk
from threading import Thread
from tqdm import tqdm
import requests
import os

user = os.path.expanduser('~')

window = Tk()


pole1 = Entry(window,text="Entry link here:")
pole1.place(x=20,y= 60, width=250)



def Download_Video():
    link = pole1.get()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(user+"\Desktop\Filmy")
        valid = True
        
    except:
        print("An error has occurred")
        valid = False
        
    if valid == True:
        print("Download is completed successfully")
    

def Download_Audio():
    link = pole1.get()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    destination = user+"\Desktop\Filmy"
    try:
        out_file = youtubeObject.download(output_path=destination)
        base = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        valid = True
    except:
        print("An error has occurred")
        valid = False
        
    if valid == True:
        print("Download is completed successfully")
        
        
    

def update_progress_bar(stream,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = bytes_downloaded / total_size * 100
    progress['value'] = percent


title1 = Label(window,text='Welcome in YT downloader.')
title1.place(x=70,y= 20)

progress = ttk.Progressbar(window, orient='horizontal', mode='determinate')
progress.place(x=10, y=160, width=280)

Button1 = Button(window,text="Pobierz Film",command=Download_Video)
Button1.place(x=110,y=100)

Button2 = Button(window,text="Pobierz Muzyke",command=Download_Audio)
Button2.place(x=100,y=130)

window.title('Video Downloader')
window.geometry("300x200")
window.mainloop()
"""





from tkinter import *
from tkinter import ttk
from pytube import YouTube
from threading import Thread
from tqdm import tqdm
import requests
import os

user = os.path.expanduser('~')

window = Tk()
window.title('Video Downloader')
window.geometry("300x200")

# Utworzenie widgetu Entry do wprowadzenia linku do pobrania
pole1 = Entry(window,text="Entry link here:")
pole1.place(x=20,y= 60, width=250)

# Utworzenie widgetu Progressbar do wyświetlania postępu pobierania
progress = ttk.Progressbar(window, orient='horizontal', mode='determinate')
progress.place(x=10, y=160, width=280)

# Funkcja obsługująca przycisk "Pobierz Film"
def Download_Video():
    link = pole1.get()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    url = youtubeObject.url
    filename = youtubeObject.default_filename
    destination = user + "\Desktop\Filmy\\" + filename
    try:
        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(destination, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
                progress['value'] = progress_bar.n / progress_bar.total * 100
                window.update_idletasks() # odświeżanie GUI
        progress_bar.close()
        print("Download is completed successfully")
    except:
        print("An error has occurred")
    
    

# Funkcja obsługująca przycisk "Pobierz Muzyke"
def Download_Audio():
    link = pole1.get()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    filename = youtubeObject.default_filename
    url = youtubeObject.url
    destination = user + "\Desktop\Filmy\\"+filename
    try:
        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(destination, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
                progress['value'] = progress_bar.n / progress_bar.total * 100
                window.update_idletasks() # odświeżanie GUI
        progress_bar.close()
        print("Download is completed successfully")
    except:
        print("An error has occurred")
    

# Funkcja wyświetlająca postęp pobierania w Progressbar
def update_progress_bar(stream, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = bytes_downloaded / total_size * 100
    progress['value'] = percent


def thread_Dwonload_Audio():
    Thread(target=Download_Audio).start()

def thread_Dwonload_Video():
    Thread(target=Download_Video).start()


label1 = Label(window,text="Wprowadź link do filmu:")
label1.place(x=20,y= 30)

# Utworzenie widgetu Button do pobierania filmu
Button1 = Button(window,text="Pobierz Film",command=thread_Dwonload_Video)
Button1.place(x=110,y=100)

# Utworzenie widgetu Button do pobierania muzyki
Button2 = Button(window,text="Pobierz Muzyke",command=thread_Dwonload_Audio)
Button2.place(x=100,y=130)


window.title('Video Downloader')
window.geometry("300x200")
window.mainloop()



