import os
import sys
from pathlib import Path
import update_metadata


try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

output_dir_path = project_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")
music_dir_path = Path("\\\\CHANSEY\\Home_Storage\\Music")

def main():
    print('starting')
    # artist_name_list = os.listdir(music_dir_path)
    # for artist_name in artist_name_list:
    #
    #     artist_path = music_dir_path.joinpath(artist_name)
    #     artist_is_dir = os.path.isdir(artist_path)
    #
    #     if artist_is_dir:
    #         album_list = os.listdir(artist_path)
    #
    #         for album_name in album_list:
                #\\CHANSEY\Home_Storage\Music\Clubland\Clubland X-Treme Hardcore 2 - CD2

                # album_path = artist_path.joinpath(album_name)
    album_path = Path("\\\\CHANSEY\\Home_Storage\\Music\\Clubland\\Clubland X-Treme Hardcore 2 - CD3")
    album_is_dir = os.path.isdir(album_path)

    if album_is_dir:
        song_list = os.listdir(album_path)

        for song_name in song_list:
            song_path = album_path.joinpath(song_name)

            try:
                update_metadata.update_tags(
                        song_path,
                        discnumber=3,

                )
                print('updated')
            except Exception as e:
                print(e)


# def get_needed_paths(artist_name=None,album_name=None,song_name = None):
#

# def get_artist_paths(artist_name = None):
#     if artist_name:
#         artist_path = music_dir_path.joinpath(artist_name)
#         return [artist_path]
#     else:
#         artist_path_list = os.listdir(music_dir_path)
#         return artist_path_list
#
# def get_album_paths(album_name=None):
#     if artist_name:
#         artist_path = music_dir_path.joinpath(artist_name)
#         return [artist_path]
#     else:
#         artist_path_list = os.listdir(music_dir_path)
#         return artist_path_list

if __name__ == '__main__':
    main()
