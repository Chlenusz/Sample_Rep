import os
import tkinter as tk
from threading import Thread 
from pytube import YouTube






class App:
    
    def __init__(self, master):
        self.master = master
        master.title("YT Downloader")
        
        self.label = tk.Label(master, text="Rozpocznij pobieranie")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.button = tk.Button(master, text="Wygeneruj", command=self.Download)
        self.button.pack()
        
        
    def get_url(self):
        link = self.entry.get()
        return link
        
        
    def Download(self):
        try:
            self.link = self.get_url()
            user = os.path.expanduser('~')
            destination = user+"\Desktop\Filmy\\"
            youtubeObject = YouTube(self.link)
            youtubeObject = youtubeObject.streams.filter(only_audio=True,bitrate="128kbps").get_audio_only()
            self.name = YouTube(self.link).title
            self.name += ".mp3"
            replacements = [('/', '_'),('*', '_'),('"', '_')]
            for char, replacement in replacements:
                if char in self.name:
                    self.name = self.name.replace(char, replacement)
            self.file = Thread.start(youtubeObject.download(output_path=destination,filename=self.name))
        except:
            print("Błąd z wątkiem")

        
    def test(self):
        self.name = YouTube(self.get_url()).title
        self.name += ".mp3"
        print(self.name)




root = tk.Tk()
app = App(root)
root.geometry("300x200")
root.mainloop()