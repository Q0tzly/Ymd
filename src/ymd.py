#!/usr/bin/env python3
import sys
from yt_dlp import YoutubeDL

f_path = sys.argv[1]
d_path = '$HOME/Downloads'

opts = {
    'outtmpl': f'{d_path}/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # to mp3
        'preferredquality': '320',  # kbps
    }],
}

with open(f_path, 'r') as f:
    for url in f:
       with YoutubeDL(opts) as ydl:
           result = ydl.download([url])
