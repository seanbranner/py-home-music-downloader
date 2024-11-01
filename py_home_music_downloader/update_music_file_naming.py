import os
from pathlib import Path
import sys
from py_home_music_downloader import update_metadata, utils_path, utils_path

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

project_music_dir = Path("/mnt/CHANSEY/Music")


def main():
    # list_of_artists_in_music_dir = os.listdir(project_music_dir)
    # print(list_of_artists_in_music_dir)
    # exit()

    # update_artist_metadata(list_of_artists_in_music_dir)

    update_artist_metadata(['Reggie and the Full Effect'])


def update_artist_metadata(list_of_files_in_music_folder):
    for artist_name in list_of_files_in_music_folder:
        artist_path = project_music_dir.joinpath(artist_name)
        artist_is_dir = os.path.isdir(artist_path)
        if artist_is_dir:
            album_name_list = os.listdir(artist_path)
            update_album_metadata(
                album_name_list=album_name_list,
                artist_path=artist_path,
                artist_name=artist_name
            )


def update_album_metadata(album_name_list, artist_name, artist_path):
    for album_name in album_name_list:
        album_path = artist_path.joinpath(album_name)
        album_path_is_dir = os.path.isdir(album_path)
        if album_path_is_dir:
            song_name_list = os.listdir(album_path)
            update_song_metadata(
                album_name=album_name,
                album_path=album_path,
                artist_name=artist_name,
                song_name_list=song_name_list)


def update_song_metadata(album_name, album_path, artist_name, song_name_list):
    for song_file_name in song_name_list:

        song_name = utils_path.extract_song_title(song_file_name)

        song_path = album_path.joinpath(song_file_name)

        track_number = None

        try:
            track_number = int(song_file_name.split('.')[0])
        except Exception as e:
            pass

        try:
            track_number = int(song_file_name.split('-')[0])
        except Exception as e:
            pass

        try:
            track_number = int(song_file_name.split(' ')[0])
        except Exception as e:
            pass

        try:
            update_metadata.update_tags(
                file_path=song_path,
                title=song_name.strip(),
                tracknumber=track_number,
                album=album_name,
                artist=artist_name,
                albumartist=artist_name,
            )

        except Exception as e:
            print(f"{song_path} probably not song {e}")


if __name__ == "__main__":
    main()
