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
import download_youtube_link_audio

load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = (Path(__file__).parents[1])

project_music_dir = project_path.joinpath("output")

project_music_dir_exists = os.path.exists(project_music_dir)

music_list = os.getenv("URL_LIST").split()

album_to_song_dictionary = {}

artist_to_album_to_song_dict ={}

def main():
    print("Starting Main...")

    if not project_music_dir_exists:
        os.mkdir(str(project_music_dir))

    params = {
        'format': 'bestaudio[ext=m4a]/best[ext=mp4]/best',
        '--write-info-json': True
    }

    audio_downloder = YoutubeDL(params=params)
    # audio_downloder = YoutubeDL({'format': 'bestaudio[ext=mmp4]/best[ext=mp4]/best'})

    os.chdir(project_music_dir)

    for music_url in music_list:
        try:
            results_from_youtube = audio_downloder.extract_info(music_url)
            title = try_dict(results_from_youtube, 'title')
            if 'Album - ' in title:
                type = try_dict(results_from_youtube, '_type')
                entries = try_dict(results_from_youtube, 'entries')
                id = try_dict(results_from_youtube, 'id')
                extractor = try_dict(results_from_youtube, 'extractor')
                extractor_key = try_dict(results_from_youtube, 'extractor_key')

                for song in entries:
                    title = song['title']
                    album = song['album']
                    artist = song['artist'].split(',')[0]
                    track = song['track']
                    release_date = song['release_date']
                    release_year = song['release_year']
                    playlist = song['playlist']
                    playlist_title = song['playlist_title']

                    # print(
                    #     f"type = {type}\n",
                    #     f"entries = {entries}\n",
                    # )

                    if artist not in artist_to_album_to_song_dict:
                        artist_to_album_to_song_dict[artist] = {}

                    artist_json = artist_to_album_to_song_dict[artist]

                    if album not in artist_json:
                        artist_json[album] = []

                    title_list = artist_json[album]

                    if title not in title_list:
                        title_list.append(f"{title}.mp3")

            else:
                album = try_dict(results_from_youtube, 'album')
                artist = try_dict(results_from_youtube, 'artist')
                track = try_dict(results_from_youtube, 'track')
                release_date = try_dict(results_from_youtube, 'release_date')
                release_year = try_dict(results_from_youtube, 'release_year')
                playlist = try_dict(results_from_youtube, 'playlist')
                playlist_index = try_dict(results_from_youtube, 'playlist_index')

                print(
                    f"title = {title}\n",
                    f"album = {album}\n",
                    f"artist = {artist}\n",
                    f"track = {track}\n",
                    f"release_date = {release_date}\n",
                    f"release year = {release_year}\n",
                    f"playlist = {playlist}\n",
                    f"playlist_index {playlist_index}\n",
                )

                if artist not in artist_to_album_to_song_dict:
                    artist_to_album_to_song_dict[artist] = {}

                artist_json = artist_to_album_to_song_dict[artist]

                if album not in artist_json:
                    artist_json[album] = []

                title_list = artist_json[album]

                if title not in title_list:
                    title_list.append(f"{title}.mp3")

        except:
            print("Didnt work for:" + music_url)

    convert_m4a_to_mp3.main()

    delete_m4a_files_from_output()

    update_music_file_naming.main()

    move_songs_to_their_respective_album()

def move_songs_to_their_respective_album():
    for artist in artist_to_album_to_song_dict:
        album_list = artist_to_album_to_song_dict[artist]
        artist_dir_path = project_music_dir.joinpath(artist)
        os.mkdir(artist_dir_path)

        for album in album_list:
            album_dir_path = artist_dir_path.joinpath(album)
            os.mkdir(album_dir_path)
            song_list = album_list[album]

            for song_title in song_list:
                original_song_path = project_music_dir.joinpath(song_title)
                new_song_path = album_dir_path.joinpath(song_title)
                os.rename(original_song_path,new_song_path)

def main2():
    try:
        project_path = Path(sys._MEIPASS)
    except Exception:
        project_path = (Path(__file__).parents[1])

    project_music_dir = project_path.joinpath("output")

    project_music_dir_exists = os.path.exists(project_music_dir)

    if not project_music_dir_exists:
        os.mkdir(str(project_music_dir))

    os.chdir(project_music_dir)

    download_youtube_link_audio.run_youtube_dl_cmd()


def delete_m4a_files_from_output():
    output_dir_list = os.listdir(project_music_dir)
    for file in output_dir_list:
        extenstion = file.split('.')[-1]
        if extenstion == 'm4a':
            os.remove(file)


def try_dict(dictionary_name, key):
    try:
        value = dictionary_name[key]
        return value
    except:
        print(f"Dictionary key: {key} doesn't exist in given dictionary.")
        return


if __name__ == '__main__':
    main()
