from pytube import YouTube
from time import sleep
import os
import shutil

dir1 = r""
dir2 = r""

while True:
    dir2 = input("Please Write The Directory That This File Is In: ")
    dir1 = input("Please Write The Directory Where The Mp3s Will Go: ")
    link = input("Please Write Youtube Link: ")

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
    choise = input("To Download Again Write y.To Close Write n.To Make MP3s Write m: ")
    if choise == "y":
        print("Oke")
    elif choise == "n":
        exit()
    elif choise == "m":
        for file in os.listdir(dir1):
            os.rename(dir1 + f"\{file}",dir1 + f"\{file}".replace("mp4","mp3"))
        print("Finished!")
        sleep(1)
        exit()
    else:
        print("Error")
        sleep(1)
        exit()
