import sys
from time import sleep

import pytubefix
from pytubefix.cli import on_progress
import os

from pip._internal.cli import progress_bars

user_name = os.getlogin()

print(f"Hos Geldiniz {user_name}")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n 1. Youtubedan video indirin \n 2. Youtubedan ses indirin \n 3. Cikis\n\n")


    selection_input = input("Yapmak Istediginiz Islemi Tuslayin:")

    if selection_input == "1" :
        try:
            video_url = input("Video URL: ")
            youtube_connection = pytubefix.YouTube(video_url,on_progress_callback=on_progress)
            youtube_connection.streams.get_highest_resolution().download(output_path="./videos")
            print("Indirme tamamlandi")
        except Exception as e:
            print(f"Video indirilirken hata olustu!!! \n {e}")

    elif selection_input == "2" :
        try:
            video_url = input("Audio URL: ")
            youtube_connection = pytubefix.YouTube(video_url,on_progress_callback=on_progress)
            youtube_connection.streams.get_audio_only().download(output_path="./audio")
            print("Indirme tamamlandi")
        except Exception as e:
            print(f"Ses indirilirken hata olustu!!!\n{e}")

    elif selection_input == "3" :
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Iyi Gunler")
        break
    else:
        print("Yanlis Tuslama Yaptiniz !!!")

sleep(3.0)

if os.name == 'nt':
    os.system('exit')
else:

    os.system('kill -9 $PPID')

