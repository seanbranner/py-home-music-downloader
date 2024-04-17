from youtube_dl import YoutubeDL
import sys
from pathlib import Path
import subprocess

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = (Path(__file__).parents[1])

# audio_downloder = YoutubeDL({'format': 'bestaudio[ext=m4a]/best[ext=mp4]/best'})
audio_downloder = YoutubeDL({'format': 'bestaudio[ext=mmp4]/best[ext=mp4]/best'})

config_path = project_path.joinpath("youtube-dl.conf")

def download_url(url_to_download):
    try:
        audio_downloder.extract_info(
            url = url_to_download,
        )
    except:
        print("Didnt work for:" + url_to_download)

def run_youtube_dl_cmd():
    updating_config_cmd = f"youtube-dl --config-location {config_path}"
    subprocess.run(updating_config_cmd)
