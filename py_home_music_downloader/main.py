import os
from dotenv import load_dotenv
from pathlib import Path
import sys
import pydpzpath
import convert_m4a_to_mp3
import download_youtube_link_audio
import update_metadata
import pkl_utils
load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

output_dir_path = project_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")

output_dir_exists = os.path.exists(output_dir_path)
json_dir_path_exists = os.path.exists(json_dir_path)

if not output_dir_exists:
    os.mkdir(output_dir_path)

if not json_dir_path_exists:
    os.mkdir(json_dir_path)

def main():
    print("Starting Main...")

    # list_of_json_paths = download_youtube_link_audio.download_songs_and_save_detail_json()
    #
    # pkl_utils.save_all_jsons_from_json_path(list_of_json_paths)
    #
    # convert_m4a_to_mp3.main()
    #
    # pydpzpath.delete_m4a_files_from_output()

    # pydpzpath.build_music_directories()

    # pydpzpath.move_songs_to_their_respective_album()

    update_metadata.update_all_tags()


if __name__ == "__main__":
    main()
