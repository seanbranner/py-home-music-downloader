import os
import sys
from pathlib import Path
import subprocess
from yt_dlp import YoutubeDL
import pkl_utils
from dotenv import load_dotenv
import dict_utils

load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

output_dir_path = project_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")

config_path = project_path.joinpath("youtube-dl.conf")

music_list = os.getenv("URL_LIST").split()

audio_downloder = YoutubeDL({"format": "bestaudio[ext=mmp4]/best[ext=mp4]/best"})

incomplete_file_path = project_path.joinpath("incomplete.txt")


def download_url(url_to_download):
    try:
        audio_downloder.extract_info(
            url=url_to_download,
        )
    except:
        print("Didnt work for:" + url_to_download)


def run_youtube_dl_cmd():
    updating_config_cmd = f"youtube-dl --config-location {config_path}"
    subprocess.run(updating_config_cmd)


def download_songs_and_save_detail_json():
    list_of_youtube_results = []

    params = {"format": "bestaudio[ext=m4a]/best[ext=mp4]/best"}
    audio_downloder = YoutubeDL(params=params)
    os.chdir(output_dir_path)

    for music_url in music_list:
        try:
            results_from_youtube = audio_downloder.extract_info(music_url)
            list_of_youtube_results.append(results_from_youtube)
        except:
            with open(incomplete_file_path, "w") as file1:
                file1.write(f"\n{music_url}")
                file1.close()
            print("Didnt work for:" + music_url)

    return list_of_youtube_results
