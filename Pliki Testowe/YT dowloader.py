from pytube import YouTube
import tkinter as tk
from threading import Thread 
import os

link = "https://www.youtube.com/watch?v=sVx1mJDeUjY&list=PLEy8KUItrBuYTOmKItDRwaK1Yo27HtP1z&index=13"


class Work:
    
    
    def Download(self,link):
        link ="https://www.youtube.com/watch?v=sVx1mJDeUjY&list=PLEy8KUItrBuYTOmKItDRwaK1Yo27HtP1z&index=13"
        user = os.path.expanduser('~')
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
        destination = user+"\Desktop\Filmy"
        try:
            out_file = youtubeObject.download(output_path=destination)
            base = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("Download is completed successfully")
            
        except:
            print("An error has occurred")
        
            
    
        
class App:
    
    def __init__(self, master):
        self.master = master
        master.title("YT Downloader")
        
        self.label = tk.Label(master, text="Rozpocznij pobieranie")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.button = tk.Button(master, text="Wygeneruj", command=Work().Download(link))
        self.button.pack()
        
    def Threaded(self):
        #link_var = self.get()
        #print (link_var)
        Thread.start(Work().Download(link))

    def get(self):
        global  link_var
        link_var = self.entry.get()
        return link_var

        
        
root = tk.Tk()
app = App(root)
root.geometry("300x200")
root.mainloop()