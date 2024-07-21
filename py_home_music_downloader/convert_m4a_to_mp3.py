import subprocess
import os
from pathlib import Path
import sys
from py_home_music_downloader import os_utils,vlc_utils

os_name = os_utils.get_operating_system()
vlc_home = vlc_utils.get_vlc_home(os_name)

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

project_music_dir = project_path.joinpath("output")


def run_conversion(project_music_dir):
    cmd_string_list = get_mp3_convert_cmd_list(project_music_dir)
    for cmd in cmd_string_list:
        subprocess.run(cmd)


def input_file_is_m4a(file):
    extension = file.split(".")[-1]
    return extension == "m4a"


def get_mp3_convert_cmd_list(output_dir_path):
    cmd_string_list = []
    original_file_list = []

    music_file_list = os.listdir(output_dir_path)

    try:
        music_file_list.remove("jsons")
    except:
        pass

    for file in music_file_list:
        original_music_file_path = output_dir_path.joinpath(file)

        new_music_file_name = file[:-4] + ".mp3"
        new_music_file_path = output_dir_path.joinpath(new_music_file_name)

        file_is_dir = os.path.isdir(original_music_file_path)
        file_is_mp3 = input_file_is_mp3(file)
        file_is_m4a = input_file_is_m4a(file)

        if not file_is_dir:
            if file_is_m4a:
                original_file_list.append(original_music_file_path)
                cmd_string = (
                    '"'+vlc_home+'" -I dummy "'
                    + str(original_music_file_path)
                    + '" ":sout=#transcode{acodec=mpga,ab=192}:std{dst=\''
                    + str(new_music_file_path)
                    + "',access=file}\" vlc://quit"
                )
                cmd_string_list.append(cmd_string)
        else:
            print(f"File is not converted: {file}")
    return cmd_string_list


def get_ffmpeg_cmd(output_dir_path):
    cmd_string_list = []
    original_file_list = []

    music_file_list = os.listdir(output_dir_path)

    try:
        music_file_list.remove("jsons")
    except:
        pass

    for file in music_file_list:
        original_music_file_path = output_dir_path.joinpath(file)
        new_music_file_name = file[:-4] + ".mp3"
        new_music_file_path = output_dir_path.joinpath(new_music_file_name)

        file_is_dir = os.path.isdir(original_music_file_path)
        file_is_mp3 = input_file_is_mp3(file)
        file_is_m4a = input_file_is_m4a(file)

        if not file_is_dir:
            if file_is_m4a:
                original_file_list.append(original_music_file_path)
                cmd_string = [
                    'ffmpeg', '-i', f'{original_music_file_path}', '-c:v', 'copy', '-c:a', 'libmp3lame',
                    '-q:a', '4', f'{new_music_file_path}'
                ]
                cmd_string_list.append(cmd_string)
        else:
            print(f"File is not converted: {file}")
    return cmd_string_list

def input_file_is_mp3(file):
    extension = file.split(".")[-1]
    return extension == "mp3"


# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy 'D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.m4a'  --sout=#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:std{access=file{no-overwrite},mux=mp4,dst='D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.mp3'} vlc://quit
#
# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy 'D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.m4a' --sout=#transcode{acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst='D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.mp3'}

# PLays song without gui
# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy --dummy-quiet "D:\Documents\Projects\Python\pyhomemusicdownloader\pyHomeMusicDownloader\output\idontwannabeyou.m4a"
def run_ffmpeg_conversion(output_music_dir):
    cmd_string_list = get_ffmpeg_cmd(output_music_dir)
    for cmd in cmd_string_list:
        subprocess.call(cmd)
    return 1