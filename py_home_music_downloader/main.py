import pickle

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
from mutagen.easyid3 import EasyID3
import mutagen
import urllib.request
from mutagen.id3 import ID3, TIT2
load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = (Path(__file__).parents[1])

output_dir_path = project_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")

output_dir_exists = os.path.exists(output_dir_path)
json_dir_path_exists = os.path.exists(json_dir_path)

if not output_dir_exists:
    os.mkdir(output_dir_path)

if not json_dir_path_exists:
    os.mkdir(json_dir_path)

music_list = os.getenv("URL_LIST").split()

album_to_song_dictionary = {}

artist_to_album_to_song_dict = {}

song_path_to_details_json = {}


def main():
    print("Starting Main...")

    download_songs_and_save_detail_json()

    convert_m4a_to_mp3.main()

    delete_m4a_files_from_output()

    build_music_directories()

    move_songs_to_their_respective_album()

    update_all_tags()


def download_songs_and_save_detail_json():
    params = {
        'format': 'bestaudio[ext=m4a]/best[ext=mp4]/best'
    }

    audio_downloder = YoutubeDL(params=params)

    os.chdir(output_dir_path)

    for music_url in music_list:
        try:
            results_from_youtube = audio_downloder.extract_info(music_url)
            title = try_dict(results_from_youtube, 'title')
            album_json_path = json_dir_path.joinpath(f"{title}.pkl")

            save_pkl_object(album_json_path, results_from_youtube)

        except:
            print("Didnt work for:" + music_url)


def load_pkl_object(file_path):
    with open(file_path, 'rb') as file:
        test_json = pickle.load(file)
    return test_json


def save_pkl_object(file_name, object_to_save):
    with open(file_name, 'wb') as file:
        pickle.dump(object_to_save, file)
        print('Object Saved')


def build_music_directories():
    album_json_list = get_album_json_list()

    for album_json in album_json_list:
        entries = album_json['entries']
        title = album_json['title']

        artist = entries[0]['artist'].split(',')[0].strip()
        album = title.split('-')[-1].strip()
        thumbnail = entries[0]['thumbnail']

        artist_path = output_dir_path.joinpath(artist)
        album_path = artist_path.joinpath(album)
        thumbnail_path = album_path.joinpath(f'{album}_thumbnail.jpg')

        artist_path_exists = os.path.exists(artist_path)
        album_path_exists = os.path.exists(album_path)

        if not artist_path_exists:
            os.mkdir(str(artist_path))

        if not album_path_exists:
            os.mkdir(str(album_path))

        urllib.request.urlretrieve(url=thumbnail, filename=thumbnail_path)


def update_all_tags():
    album_json_list = get_album_json_list()

    for album_json in album_json_list:
        entries = album_json['entries']
        title = album_json['title']

        artist = entries[0]['artist'].split(',')[0].strip()
        album = title.split('-')[-1].strip()

        artist_path = output_dir_path.joinpath(artist)
        album_path = artist_path.joinpath(album)

        for song in entries:
            title = try_dict(song, 'title')

            song_file_name = f"{title}.mp3"
            song_path = album_path.joinpath(song_file_name)

            all_artists = try_dict(song, 'artist')
            release_year = try_dict(song, 'release_year')
            playlist_index = try_dict(song, 'playlist_index')
            webpage_url = try_dict(song, 'webpage_url')
            tags = try_dict(song, 'tags')

            update_tags(
                file_path=song_path,
                title=title,
                tracknumber=playlist_index,
                website=webpage_url,
                date=release_year,
                album=album,
                conductor=tags,
                artist=all_artists,
                albumartist=artist
            )


def move_songs_to_their_respective_album():
    output_file_list = os.listdir(output_dir_path)
    song_file_path_list = []

    for file in output_file_list:
        file_path = output_dir_path.joinpath(file)
        if os.path.isfile(file_path):
            song_file_path_list.append(file_path)

    album_json_list = get_album_json_list()

    for album_json in album_json_list:
        entries = album_json['entries']

        list_of_songs_in_album = []
        for song_details in entries:
            song_title = song_details['title']
            if song_title not in list_of_songs_in_album:
                list_of_songs_in_album.append(song_title)

        artist = entries[0]['artist'].split(',')[0].strip()

        artist_dir_path = output_dir_path.joinpath(artist)

        album_list = os.listdir(artist_dir_path)

        for album in album_list:
            album_dir_path = artist_dir_path.joinpath(album)

            for original_song_file_path in song_file_path_list:
                original_song_file_name = str(original_song_file_path).split('\\')[-1]
                original_song_file_name_shortend = original_song_file_name.split('-')[0]
                for song_name in list_of_songs_in_album:
                    if original_song_file_name_shortend in song_name:
                        new_song_path = album_dir_path.joinpath(f'{song_name}.mp3')
                        os.rename(original_song_file_path, new_song_path)


def get_album_json_list():
    json_dir_path = output_dir_path.joinpath("jsons")
    json_list = os.listdir(json_dir_path)

    album_json_list = []
    for pkl in json_list:
        pkl_path = json_dir_path.joinpath(pkl)
        pkl_json_object = load_pkl_object(pkl_path)
        album_json_list.append(pkl_json_object)
    return album_json_list


def delete_m4a_files_from_output():
    output_dir_list = os.listdir(output_dir_path)

    for music_file_name in output_dir_list:
        music_file_path = output_dir_path.joinpath(music_file_name)
        extenstion = music_file_name.split('.')[-1]

        if extenstion == 'm4a':
            os.remove(music_file_path)


def try_dict(dictionary_name, key):
    try:
        value = dictionary_name[key]
        return value
    except:
        print(f"Dictionary key: {key} doesn't exist in given dictionary.")
        return


def update_tags(
        file_path,
        album=None,
        bpm=None,
        compilation=None,
        composer=None,
        encodedby=None,
        title=None,
        version=None,
        artist=None,
        albumartist=None,
        conductor=None,
        discnumber=None,
        organization=None,
        tracknumber=None,
        genre=None,
        date=None,
        website=None
):
    try:

        file_object = mutagen.File(file_path)
        file_object.add_tags()
        file_object.save()
    except Exception as e:
        print(e)

    tags = EasyID3(file_path)

    if album:
        tags['album'] = str(album)

    if bpm:
        tags['bpm'] = str(bpm)

    if compilation:
        tags['compilation'] = str(compilation)

    if composer:
        tags['composer'] = str(composer)

    if encodedby:
        tags['encodedby'] = str(encodedby)

    if title:
        tags['title'] = str(title)

    if version:
        tags['version'] = str(version)

    if artist:
        tags['artist'] = str(artist)

    if albumartist:
        tags['albumartist'] = str(albumartist)

    if conductor:
        tags['conductor'] = str(conductor)

    if discnumber:
        tags['discnumber'] = str(discnumber)

    if organization:
        tags['organization'] = str(organization)

    if tracknumber:
        tags['tracknumber'] = str(tracknumber)

    if genre:
        tags['genre'] = str(genre)

    if date:
        tags['date'] = str(date)

    if website:
        tags['website'] = str(website)

    tags.save()


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


if __name__ == '__main__':
    main()
# if 'Album - ' in title:
#     type = try_dict(results_from_youtube, '_type')
#     entries = try_dict(results_from_youtube, 'entries')
#     id = try_dict(results_from_youtube, 'id')
#     extractor = try_dict(results_from_youtube, 'extractor')
#     extractor_key = try_dict(results_from_youtube, 'extractor_key')
#
#     for song in entries:
#         title = song['title']
#         new_title = title.split("-")[0].strip()
#
#         album = song['album']
#         artist = song['artist'].split(',')[0]
#
#         if artist not in artist_to_album_to_song_dict:
#             artist_to_album_to_song_dict[artist] = {}
#
#         artist_json = artist_to_album_to_song_dict[artist]
#
#         if album not in artist_json:
#             artist_json[album] = {}
#
#         title_json = artist_json[album]
#
#         if new_title not in title_json:
#             title_json[f"{new_title}.mp3"] = song
#
#         title_path = output_dir_path.joinpath(artist).joinpath(album).joinpath(f"{new_title}.mp3")
#
#         song_path_to_details_json[title_path] = song
#
# else:
#     album = try_dict(results_from_youtube, 'album')
#     artist = try_dict(results_from_youtube, 'artist')
#
#     if artist not in artist_to_album_to_song_dict:
#         artist_to_album_to_song_dict[artist] = {}
#
#     artist_json = artist_to_album_to_song_dict[artist]
#
#     if album not in artist_json:
#         artist_json[album] = {}
#
#     title_json = artist_json[album]
#
#     if new_title not in title_json:
#         title_json[f"{new_title}.mp3"] = results_from_youtube
#
#     title_path = output_dir_path.joinpath(artist).joinpath(album).joinpath(f"{new_title}.mp3")
#
#     song_path_to_details_json[title_path] = results_from_youtube
