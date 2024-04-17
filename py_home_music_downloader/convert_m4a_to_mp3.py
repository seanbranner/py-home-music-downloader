import subprocess
import os
from pathlib import Path
import sys


def main():
    try:
        project_path = Path(sys._MEIPASS)
    except Exception:
        project_path = (Path(__file__).parents[1])

    project_log_dir = project_path.joinpath("logs")
    project_music_dir = project_path.joinpath("output")

    cmd_string_list = get_all_file_paths(project_music_dir)[0]
    original_file_list = get_all_file_paths(project_music_dir)[1]

    for cmd in cmd_string_list:
        subprocess.run(cmd)

    # for file in original_file_list:
    #     pydpzpath.delete_path(file)


def file_is_video(file):
    return file[-4:] == '.m4a'


def get_all_file_paths(project_music_dir):
    cmd_string_list = []
    original_file_list = []

    music_list = os.listdir(project_music_dir)

    for file in music_list:
        new_file = file[:-4] + ".mp3"
        file_path = project_music_dir.joinpath(file)
        new_file_path = project_music_dir.joinpath(new_file)

        file_is_dir = os.path.isdir(file_path)
        file_is_mp3 = input_file_is_mp3(file)
        file_is_audio_file = file_is_video(file)

        if not file_is_dir:
            if not file_is_mp3 and file_is_audio_file:
                original_file_list.append(file_path)
                cmd_string = "\"C:\\Program Files\\VideoLAN\VLC\\vlc.exe\" -I dummy \"" + str(
                    file_path) + "\" \":sout=#transcode{acodec=mpga,ab=192}:std{dst=\'" + str(
                    new_file_path) + "\',access=file}\" vlc://quit"
                cmd_string_list.append(cmd_string)
        else:
            album_list = os.listdir(file_path)

            for album in album_list:
                new_artist_dir_song = album[:-4] + ".mp3"
                artist_dir_song_path = file_path.joinpath(album)
                new_artist_dir_song_path = file_path.joinpath(new_artist_dir_song)

                file_is_dir = os.path.isdir(artist_dir_song_path)
                file_is_mp3 = input_file_is_mp3(album)
                file_is_audio_file = file_is_video(album)
                file_is_mp4 = file_is_mp4(album)

                if not file_is_dir:
                    if not file_is_mp3 and file_is_audio_file:
                        original_file_list.append(artist_dir_song_path)
                        cmd_string = "\"C:\\Program Files\\VideoLAN\VLC\\vlc.exe\" -I dummy \"" + str(
                            artist_dir_song_path) + "\" \":sout=#transcode{acodec=mpga,ab=192}:std{dst=\'" + str(
                            new_artist_dir_song_path) + "\',access=file}\" vlc://quit"
                        cmd_string_list.append(cmd_string)

                    if file_is_mp4 and file_is_audio_file:
                        original_file_list.append(artist_dir_song_path)
                        cmd_string = "\"C:\\Program Files\\VideoLAN\VLC\\vlc.exe\" -I dummy \"" + str(
                            artist_dir_song_path) + "\" \":sout=#transcode{acodec=mpga,ab=192}:std{dst=\'" + str(
                            new_artist_dir_song_path) + "\',access=file}\" vlc://quit"
                        cmd_string_list.append(cmd_string)

                else:
                    song_list = os.listdir(artist_dir_song_path)

                    for song in song_list:
                        new_file = song[:-4] + ".mp3"
                        song_file_path = artist_dir_song_path.joinpath(song)
                        new_song_file_path = artist_dir_song_path.joinpath(new_file)

                        file_is_dir = os.path.isdir(song_file_path)
                        file_is_mp3 = input_file_is_mp3(song)
                        file_is_audio_file = file_is_video(song)

                        if not file_is_dir:
                            if not file_is_mp3 and file_is_audio_file:
                                original_file_list.append(song_file_path)
                                cmd_string = "\"C:\\Program Files\\VideoLAN\VLC\\vlc.exe\" -I dummy \"" + str(
                                    song_file_path) + "\" \":sout=#transcode{acodec=mpga,ab=192}:std{dst=\'" + str(
                                    new_song_file_path) + "\',access=file}\" vlc://quit"
                                cmd_string_list.append(cmd_string)
                        else:
                            print("done")

    return cmd_string_list, original_file_list


def input_file_is_mp3(file):
    file_is_mp3 = file[-4:] == '.mp3'
    return file_is_mp3


# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy 'D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.m4a'  --sout=#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:std{access=file{no-overwrite},mux=mp4,dst='D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.mp3'} vlc://quit
#
# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy 'D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.m4a' --sout=#transcode{acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst='D:/Documents/Projects/Python/pyhomemusicdownloader/pyHomeMusicDownloader/output/idontwannabeyou.mp3'}

# PLays song without gui
# "C:\Program Files\VideoLAN\VLC\vlc" -I dummy --dummy-quiet "D:\Documents\Projects\Python\pyhomemusicdownloader\pyHomeMusicDownloader\output\idontwannabeyou.m4a"

if __name__ == '__main__':
    main()
