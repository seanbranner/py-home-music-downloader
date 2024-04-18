import json
import urllib.request
from pathlib import Path
import sys
import os
import shutil
import py_home_music_downloader
import string_utils
import pkl_utils

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

output_dir_path = project_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")


def delete_path(delete_path):
    # pathlibPath.exists()
    try:
        if os.path.isdir(delete_path):
            # os.rmdir(delete_path)
            shutil.rmtree(delete_path)
        if os.path.isfile(delete_path):
            os.remove(delete_path)
        print("NOTE: Removed: " + str(delete_path))
    except OSError as e:
        print("Error: %s : %s" % (delete_path, e.strerror))


def isdir(input_path):
    return os.path.isdir(input_path)


def build_music_directories():
    album_json_list = pkl_utils.get_album_json_list()

    for album_json in album_json_list:
        entries = album_json["entries"]
        title = album_json["title"]

        entry_artist = entries[0]["artist"]
        artist = entry_artist.split(",")[0].strip().replace('/','-')

        album = string_utils.extract_album_name(title)

        thumbnail = entries[0]["thumbnail"]

        artist_path = output_dir_path.joinpath(artist)
        album_path = artist_path.joinpath(album)
        thumbnail_path = album_path.joinpath(f"{album}_thumbnail.jpg")

        artist_path_exists = os.path.exists(artist_path)
        album_path_exists = os.path.exists(album_path)

        if not artist_path_exists:
            os.mkdir(str(artist_path))

        if not album_path_exists:
            os.mkdir(str(album_path))

        urllib.request.urlretrieve(url=thumbnail, filename=thumbnail_path)


def move_songs_to_their_respective_album():
    output_file_list = os.listdir(output_dir_path)
    song_file_path_list = []

    for file in output_file_list:
        file_path = output_dir_path.joinpath(file)
        if os.path.isfile(file_path):
            song_file_path_list.append(file_path)

    album_json_list = pkl_utils.get_album_json_list()

    for album_json in album_json_list:
        entries = album_json["entries"]

        list_of_songs_in_album = []
        for song_details in entries:
            song_title = song_details["title"]
            if song_title not in list_of_songs_in_album:
                list_of_songs_in_album.append(song_title)

        artist = entries[0]["artist"].split(",")[0].strip()
        artist = artist.replace('/','-')

        artist_dir_path = output_dir_path.joinpath(artist)

        album_list = os.listdir(artist_dir_path)

        for album in album_list:
            album_dir_path = artist_dir_path.joinpath(album)

            for original_song_file_path in song_file_path_list:
                original_song_file_name = str(original_song_file_path).split("\\")[-1]
                original_song_file_name_shortend = string_utils.extract_song_title(original_song_file_name)

                for song_name in list_of_songs_in_album:

                    if original_song_file_name_shortend in song_name:
                        new_song_path = album_dir_path.joinpath(f"{song_name}.mp3")
                        os.rename(original_song_file_path, new_song_path)



def delete_m4a_files_from_output():
    output_dir_list = os.listdir(output_dir_path)

    for music_file_name in output_dir_list:
        music_file_path = output_dir_path.joinpath(music_file_name)
        extenstion = music_file_name.split(".")[-1]

        if extenstion == "m4a":
            os.remove(music_file_path)
