from youtube_dl import YoutubeDL
import pydpzpath
import json
import os
# change the format to bestaudio to get mp3 file.
import convert_m4a_to_mp3
import os
from dotenv import load_dotenv
from pathlib import Path
import sys
import update_music_file_naming

load_dotenv()

def main():
    print("Starting Main...")

    try:
        project_path = Path(sys._MEIPASS)
    except Exception:
        project_path = (Path(__file__).parents[1])

    project_log_dir = project_path.joinpath("logs")
    project_music_dir = project_path.joinpath("output")

    project_music_dir_exists = os.path.exists(project_music_dir)

    music_list = os.getenv("URL_LIST").split()

    if not project_music_dir_exists:
        os.mkdir(str(project_music_dir))

    audio_downloder = YoutubeDL({'format': 'bestaudio[ext=m4a]/best[ext=mp4]/best'})
    # audio_downloder = YoutubeDL({'format': 'bestaudio[ext=mmp4]/best[ext=mp4]/best'})

    os.chdir(project_music_dir)
    for music_url in music_list:
        try:
            audio_downloder.extract_info(music_url)
        except:
            print("Didnt work for:" + music_url)

    convert_m4a_to_mp3.main()

    update_music_file_naming.main()

if __name__ == '__main__':
    main()