import shutil
from py_home_music_downloader import os_utils

def get_vlc_home(os):
    if 'Darwin' in os:
        return '/Applications/VLC.app/Contents/MacOS/VLC'
    if 'Windows' in os:
        return 'C:\\Program Files\\VideoLAN\VLC\\vlc.exe'
    else:
        print("VLC not found.")