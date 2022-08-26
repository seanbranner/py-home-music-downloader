from youtube_dl import YoutubeDL
from pyHomeMusicDownloader import pydpzpath
import pydpzpath
import json
# change the format to bestaudio to get mp3 file.
import convert_m4a_to_mp3
import os

def main():
    print("Starting Main...")

    try:
        project_path = Path(sys._MEIPASS)
    except Exception:
        project_path = (Path(__file__).parents[1])

    json_path = project_path.joinpath('config.json')

    with open(json_path, 'r') as f:
        config = json.load(f)

    music_list = config['MUSIC']['URL_LIST']

    if not project_log_dir.exists():
        project_path.create_dir("logs")

    if not project_music_dir.exists():
        project_path.create_dir("output")

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