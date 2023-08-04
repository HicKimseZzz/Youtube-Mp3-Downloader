from tkinter import *
from tkinter import ttk
import tkinter as tk
from ctypes import windll
from pytube import YouTube
import os
import shutil


def get_dir1():
    dir1 = entry_dir1.get()
    return dir1

def get_dir2():
    dir2 = entry_dir2.get()
    return dir2

def download():
    link = entry_link.get()
    yt = YouTube(link)
    downYt = yt.title + ".mp4"
    yr = yt.streams.get_highest_resolution()

    yr.download()
    for file1 in os.listdir(get_dir2()):
        if file1 == downYt:
            shutil.move(get_dir2() + f"\{file1}",get_dir1())
            break

def convert():
    for file in os.listdir(get_dir1()):
            os.rename(get_dir1() + f"\{file}",get_dir1() + f"\{file}".replace("mp4","mp3"))

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

frame_dir1 = Frame(master=window,bg="#242424")
dir1Str = tk.StringVar()
entry_dir1 = Entry(master=frame_dir1,width=45,font=("Cascadia Code",10),textvariable=dir1Str)
dir1But = Button(master=frame_dir1,command=get_dir1,text="Submit",font=("Cascadia Code",10),fg="#e8e8e8",bg="#222222",activebackground="#1D1D1D",activeforeground="#FAFBFB",relief=FLAT)

frame_dir2 = Frame(master=window,bg="#242424")
dir2Str = tk.StringVar()
entry_dir2 = Entry(master=frame_dir2,width=45,font=("Cascadia Code",10),textvariable=dir2Str)
dir2But = Button(master=frame_dir2,command=get_dir2,text="submit",font=("Cascadia Code",10),fg="#e8e8e8",bg="#222222",activebackground="#1D1D1D",activeforeground="#FAFBFB",relief=FLAT)

mp3But = Button(master=window,command=convert,text="Convert",font=("Cascadia Code",10),fg="#e8e8e8",bg="#222222",activebackground="#1D1D1D",activeforeground="#FAFBFB",relief=FLAT)

frame_dir2.pack(pady=30)
entry_dir2.pack(side = "left",padx= 10)
dir2But.pack(padx=10)
dir2_text = Label(master=frame_dir2,text="Dir This File Is In",font=("Cascadia Code",10))
dir2_text.pack(pady=5)

frame_dir1.pack(pady=30)
entry_dir1.pack(side = "left",padx= 10)
dir1But.pack(padx=10)
dir1_text = Label(master=frame_dir1,text="Dir Where Mp3s Go",font=("Cascadia Code",10))
dir1_text.pack(pady=5)


frame_link.pack(pady=30)
entry_link.pack(side = "left",padx= 10)
linkBut.pack(padx=10)
link_text = Label(master=frame_link,text="Youtube Link",font=("Cascadia Code",10))
link_text.pack(pady=5)

mp3But.pack(pady=10)

window.mainloop()
