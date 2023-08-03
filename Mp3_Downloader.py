from tkinter import *
from tkinter import ttk
import tkinter as tk
from ctypes import windll
from pytube import YouTube
import os
import shutil

dir1 = r""
dir2 = r""

def download():
    yt = YouTube(link)
    downYt = yt.title + ".mp4"
    yr = yt.streams.get_highest_resolution()
    print(yr)

    print("Your Video Is Downloading")
    yr.download()
    print("Video Is Downloaded!")
    for file1 in os.listdir(dir2):
        if file1 == downYt:
            print(file1)
            print("Finded")
            shutil.move(dir2 + f"\{file1}",dir1)
            break

def close():
    exit()

def convert():
    for file in os.listdir(dir1):
            os.rename(dir1 + f"\{file}",dir1 + f"\{file}".replace("mp4","mp3"))

window = Tk()
windll.shcore.SetProcessDpiAwareness(1)
window.geometry("850x525")
window.title("Youtube Mp3 Downloader")
window.config(background="#242424") 

maintext = Label(window,text="Mp3 Downloader",font=("Cascadia Code",40,"bold"),fg="#e8e8e8",bg="#242424")
maintext.pack()


frame_link = Frame(master=window,bg="#242424")
linkStr = tk.StringVar()
entry_link = Entry(master=frame_link,width=45,font=("Cascadia Code",10),textvariable=linkStr)
linkBut = Button(master=frame_link,text="Download",command=download,font=("Cascadia Code",10),fg="#e8e8e8",bg="#222222",activebackground="#1D1D1D",activeforeground="#FAFBFB",relief=FLAT)

mp3But = Button(master=window,text="Convert",font=("Cascadia Code",10),fg="#e8e8e8",bg="#222222",activebackground="#1D1D1D",activeforeground="#FAFBFB",relief=FLAT)

frame_link.pack(pady=100)
entry_link.pack(side = "left",padx= 10)
linkBut.pack(padx=10)
mp3But.pack(pady=10)

window.iconbitmap("app.ico")

window.mainloop()
