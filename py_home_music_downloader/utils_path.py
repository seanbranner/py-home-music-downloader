import getpass
from pathlib import Path
import os
import platform
from dotenv import load_dotenv
import mimetypes

load_dotenv()

def extract_album_name(title):
    if "- Album – " in title:
        split_album = title.split("-")
        split_album.pop(0)
        title = title.replace("- Album – ", "")
        return title
    else:
        split_album = title.split("-")
        split_album.pop(0)
        return "-".join(split_album).strip()

def get_audio_files_from_file_list(list_of_files):
    audio_list = []
    for file in list_of_files:
        file_exstension = file.split('.')[-1]
        audio_file_extension_list = os.getenv("MUSIC_EXTENSION_LIST")
        if file_exstension in audio_file_extension_list:
            audio_list.append(file)
    return audio_list

def get_albums_from_file_list(list_of_files):
    audio_list = []
    for file in list_of_files:
        file_exstension = file.split('.')[-1]
        audio_file_extension_list = os.getenv("MUSIC_EXTENSION_LIST")
        if file_exstension in audio_file_extension_list:
            audio_list.append(file)
    return audio_list

def extract_song_title(song_title):
    has_bit_tag = "(" in song_title and ")" in song_title and "bit" in song_title

    extension = song_title.split('.')[-1]

    if has_bit_tag:
        new_song_title = song_title.split('(')[0]
        new_song_title = new_song_title.strip()

    else:
        split_album = song_title.split("[")
        split_album.pop(-1)
        new_song_title = "-".join(split_album).strip()

    return f"{new_song_title}.{extension}"


def local_download_to_chansey_music():
    pass


def get_home_download_dir():
    operating_system = platform.platform()
    user = getpass.getuser()
    print(operating_system)
    if 'Linux' in operating_system:
        home_download_directory = Path(f"/home/{user}/Downloads")
    else:
        home_download_directory = Path("/Downloads")

    return home_download_directory


def determine_file_types(file_list):
    path_organization_json = {
        "music": [],
        "movies": [],
        "tv": [],
        "yt": []
    }

    for file_name in file_list:
        file_is_dir = os.path.isdir(file_name)
        if file_is_dir:
            file_path = file_name.joinpath(file_name)
            internal_file = os.listdir(file_path)
            extension = internal_file.split('.')[-1]
        else:
            internal_file = os.listdir(file_path)
            extension = internal_file.split('.')[-1]

        if "mp3" in extension or 'opus' in extension or "jpg" in extension:
            path_organization_json['music'].append(file_name)
        if "m4A" in extension:
            path_organization_json['movie'].append(file_name)
