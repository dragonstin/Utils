from difflib import SequenceMatcher
from  tkinter import *
import os
import glob


myDir= 'John Mayer'

# Playlist Url need to have the format below
# https://www.youtube.com/playlist?list=RDCLAK5uy_lGEOjy5U8xV41C8_LyqNnAZKOH6sGyutI
playlist = 'https://www.youtube.com/playlist?list=OLAK5uy_lx7e5iEu9P3h1YbwPbh67WJ6MksezihF8'


os.system('youtube-dl --download-archive downloaded.txt -w -i -o "./'+myDir+'/%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --socket-timeout 5 '+ playlist)

# Version python 2.7
# os.system('youtube-dl --download-archive downloaded.txt --no-overwrites -i -o "./'+myDir+'/%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --socket-timeout 5 '+ playlist)
   
'''
    Parameters on youtube-dl

    -i - ignore errors

    -c - continue

    -t - use video title as file name

    --extract-audio - extract audio track

    --audio-format mp3 - convert to mp3

    --audio-quality 0 - the best audio quality

    --yes-playlist - affirm that url points to a playlist

    YT_URL - video url from youtube

    # Download single entry
    youtube-dl -i --extract-audio --audio-format mp3 --audio-quality 0 YT_URL

    # Download playlist
    youtube-dl -ict --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 https://www.youtube.com/playlist?list=UUCvVpbYRgYjMN7mG7qQN0Pg

    # Download playlist, --download-archive downloaded.txt add successfully downloaded files into downloaded.txt
    youtube-dl --download-archive downloaded.txt --no-overwrites -ict --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --socket-timeout 5 https://www.youtube.com/playlist?list=UUCvVpbYRgYjMN7mG7qQN0Pg

    # Retry until success, no -i option
    while ! youtube-dl --download-archive downloaded.txt --no-overwrites -ct --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --socket-timeout 5 <YT_PlayList_URL>; do echo DISCONNECTED; sleep 5; done
'''

