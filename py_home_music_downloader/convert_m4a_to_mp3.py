import subprocess
import os
from pathlib import Path
import sys
import time

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

# project_music_dir = Path("/CHANSEY/Music/Aminé/TWOPOINTFIVE/")
project_music_dir = Path("D:\\Music\\KOTA The Friend\\Lyrics to Go Vol Three\\")


# vlc_path = Path("/snap/bin/vlc")
vlc_path = Path("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

def main():

    cmd_string_list = get_mp3_convert_cmd_list(project_music_dir)

    for cmd in cmd_string_list:
        print(cmd)
        subprocess.run(cmd)

def input_file_is_m4a(file):
    extension = file.split(".")[-1]
    return extension == "m4a"


def input_file_is_mp4(file):
    extension = file.split(".")[-1]
    return extension == "mp4"


def get_mp3_convert_cmd_list(output_dir_path):
    cmd_string_list = []
    original_file_list = []

    music_file_list = os.listdir(output_dir_path)

    for original_file in music_file_list:
        original_music_file_path = output_dir_path.joinpath(original_file)

        new_music_file_name = original_file[:-4] + ".mp3"
        new_music_file_path = output_dir_path.joinpath(new_music_file_name)

        file_is_dir = os.path.isdir(original_music_file_path)
        file_is_mp3 = input_file_is_mp3(original_file)
        file_is_m4a = input_file_is_m4a(original_file)
        file_is_mp4 = input_file_is_mp4(original_file)


        if not file_is_dir:
            #TODO
            if file_is_m4a:
                original_file_list.append(original_music_file_path)
                #vlc -I dummy input.wav ":sout=#transcode{acodec=mpga,ab=192}:std{dst=output.mp3,access=file}" vlc://quit
                #using sout chain=`transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:std{access=file{no-overwrite},mux=mp3,dst='//chansey/Home_Storage/Music/Amin├⌐/TWOPOINTFIVE/Between The Lines-4ESErHIoG6w.mp3'}'
                cmd_string = (
                    '"C:\\Program Files\\VideoLAN\VLC\\vlc.exe" -I dummy "'
                    + str(original_music_file_path)
                    + '" ":sout=#transcode{acodec=mpga,ab=192}:std{dst=\''
                    + str(new_music_file_path)
                    + "',access=file}\" vlc://quit"
                )
                cmd_string_list.append(cmd_string)
            if file_is_mp4:
                original_file_list.append(original_music_file_path)
                cmd_string = (
                    f'"{str(vlc_path)}" -I dummy "{str(original_music_file_path)}" :sout=#transcode'
                    + '{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:std{access=file{no-overwrite},mux=mp3,dst='
                    + f'"{str(new_music_file_path)}"'
                    + '} vlc://quit'
                #:std{access=file{no-overwrite},mux=mp3,dst=
                )
                cmd_string_list.append(cmd_string)
        else:
            print(f"File is not converted: {original_file}")
    return cmd_string_list


def input_file_is_mp3(file):
    extension = file.split(".")[-1]
    return extension == "mp3"

#2024
#"C:\Program Files (x86)\VideoLAN\VLC\vlc" -I dummy "%%a" --sout=#transcode{acodec=mp3,ab=128,vcodec=dummy}:std{access="file",mux="raw",dst="%%a.mp3"} vlc://quit

# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy 'D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.m4a'  --sout=#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:std{access=file{no-overwrite},mux=mp4,dst='D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.mp3'} vlc://quit
#
# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy 'D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.m4a' --sout=#transcode{acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst='D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.mp3'}

# PLays song without gui
# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy --dummy-quiet "D:\Documents\Projects\Python\pyhomemusicdownloader\pyHomeMusicDownloader\output\idontwannabeyou.m4a"

if __name__ == "__main__":
    main()
