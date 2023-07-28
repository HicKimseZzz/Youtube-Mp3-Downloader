from pytube import YouTube
from colorama import Fore,init,Back,Style
from time import sleep
import os

dirr = r"C:\Users\YourPcName\Desktop\PlaceWhereYouWillStoreYourMp3s"
dir2 = r"C:\Users\YourPcName\Desktop"
dirD = r"C:\Users\YourPcName\Desktop\ProjectFile"

init(autoreset=False)

while True:
    link = input(Fore.RED + Back.WHITE + "Please Write Youtube Link: ")

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
            shutil.move(dir2 + f"\{file1}",dirr)
            break
    choise = input("To Download Again Write y.To Close Write n.To Make MP3s Write m: ")
    sleep(1)
    if choise == "y":
        print("Oke")
    elif choise == "n":
        exit()
    elif choise == "m":
        print("Deneme")
        for file in os.listdir(dirr):
            os.rename(dirr + f"\{file}",dirr + f"\{file}".replace("mp4","mp3"))
        print("Finished!")
        sleep(1)
        exit()
    else:
        print("Error")
        sleep(1)
        exit()
