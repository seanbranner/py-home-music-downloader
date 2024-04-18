import os
from pathlib import Path
import sys

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

project_music_dir = project_path.joinpath("output")


def main():
    list_of_files_in_music_folder = os.listdir(project_music_dir)

    for music_file in list_of_files_in_music_folder:
        original_name_path = project_music_dir.joinpath(music_file)
        new_name_path = project_music_dir.joinpath(convert_name(music_file))
        os.rename(str(original_name_path), str(new_name_path))


def convert_name(initial_name):
    extension = initial_name.split(".")[-1]

    new_name_list = initial_name.split("-")[0].strip()

    return f"{new_name_list}.{extension}"


if __name__ == "__main__":
    main()
