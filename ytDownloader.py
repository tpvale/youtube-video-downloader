from pytube import YouTube
from sys import argv
import os

# link recebe como valor o segundo argumento passado ao rodar o sript no caso (python ytDownloader.py "youtube.com/video-xpto")
link = argv[1]

# Monta o objeto contendo o link obtido no passo anterior
yt = YouTube(link)
print(yt)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(os.getcwd()+'/downloadedVideos')