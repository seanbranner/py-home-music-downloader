from youtube_dl import YoutubeDL
from pyHomeMusicDownloader import pydpzpath
import pydpzpath
# change the format to bestaudio to get mp3 file.
import convert_m4a_to_mp3
import os

def main():
    project_dir = pydpzpath.get_root_path()
    project_music_dir = project_dir.joinpath("output")

    artist = None
    album = None
    song_name = None

    video_list_path = project_dir.joinpath("video_list.txt")

    if not project_log_dir.exists():
        pydpzpath.create_dir("logs")

    if not project_music_dir.exists():
        pydpzpath.create_dir("output")

    video_list_file = open(video_list_path, "r")

    # audio_downloder = YoutubeDL({'format': 'bestaudio[ext=m4a]/best[ext=mp4]/best'})
    audio_downloder = YoutubeDL({'format': 'bestaudio[ext=mmp4]/best[ext=mp4]/best'})


    os.chdir(project_music_dir)
    for video_url in video_list_file:
        try:
            audio_downloder.extract_info(video_url)
        except:
            print("Didnt work for:" + video_url)

    convert_m4a_to_mp3.main()

if __name__ == '__main__':
    main()
    HotgirlClass.function1()