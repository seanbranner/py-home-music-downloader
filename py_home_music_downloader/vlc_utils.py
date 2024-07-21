import shutil
from py_home_music_downloader import os_utils

def get_vlc_home(os_name):
    if 'Darwin' in os_name:
        return '/Applications/VLC.app/Contents/MacOS/VLC'
    if 'Windows' in os_name:
        return 'C:\\Program Files\\VideoLAN\VLC\\vlc.exe'
    else:
        print("VLC not found.")