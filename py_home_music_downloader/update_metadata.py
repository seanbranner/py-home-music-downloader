import os
from mutagen.oggopus import OggOpus
from mutagen.easyid3 import EasyID3
from mutagen.mp4 import MP4

import mutagen
from pathlib import Path
import sys

from py_home_music_downloader import utils_dict, utils_pkl, utils_path

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

project_music_dir = project_path.joinpath("output")


def update_all_tags():
    album_json_list = get_album_json_list()

    for album_json in album_json_list:
        entries = album_json["entries"]
        title = album_json["title"]

        artist = entries[0]["artist"].split(",")[0].strip().replace('/','-')
        album = extract_album_name(title)

        artist_path = output_dir_path.joinpath(artist)
        album_path = artist_path.joinpath(album)

        for song in entries:
            title = try_dict(song, "title").replace('?','')

            song_file_name = f"{title}.mp3"
            song_path = album_path.joinpath(song_file_name)

            all_artists = try_dict(song, "artist")
            release_year = try_dict(song, "release_year")
            playlist_index = try_dict(song, "playlist_index")
            webpage_url = try_dict(song, "webpage_url")
            tags = try_dict(song, "tags")

            update_tags(
                file_path=song_path,
                title=title,
                tracknumber=playlist_index,
                website=webpage_url,
                date=release_year,
                album=album,
                conductor=tags,
                artist=all_artists,
                albumartist=artist,
            )


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
    website=None,
):

    if not os.path.exists(file_path):
        print(f"Path doesnt exist, did not add tags: {file_path}")
        return

    try:
        file_object = mutagen.File(file_path)
        file_object.add_tags()
        file_object.save()
    except Exception as e:
        print(f"{e}: {file_path}")

    file_type = str(file_path).split('.')[-1]

    file_is_mp3 = 'mp3' in file_type
    file_is_mp4 = 'mp4' in file_type
    file_is_opus = 'opus' in file_type
    file_is_m4a = 'm4a' in file_type

    if file_is_opus:
        tags = OggOpus(file_path)

    if file_is_mp3:
        tags = EasyID3(file_path)

    if file_is_mp4 or file_is_m4a:
        tags = MP4(file_path)
        if title:
            tags["\xa9nam"] = str(title)

        if albumartist:
            tags["\xa9ART"] = str(albumartist)

        if albumartist:
            tags["aART"] = str(albumartist)

        if tracknumber:
            tags["trkn"] = str(tracknumber)

        if album:
            tags["\xa9alb"] = str(album)

        tags.save()
        print(tags)


    if album:
        tags["album"] = str(album)

    if bpm:
        tags["bpm"] = str(bpm)

    if compilation:
        tags["compilation"] = str(compilation)

    if composer:
        tags["composer"] = str(composer)

    if encodedby:
        tags["encodedby"] = str(encodedby)

    if title:
        tags["title"] = str(title)

    if version:
        tags["version"] = str(version)

    if artist:
        tags["artist"] = str(artist)

    if albumartist:
        tags["albumartist"] = str(albumartist)

    if conductor:
        tags["conductor"] = str(conductor)

    if discnumber:
        tags["discnumber"] = str(discnumber)

    if organization:
        tags["organization"] = str(organization)

    if tracknumber:
        tags["tracknumber"] = str(tracknumber)

    if genre:
        tags["genre"] = str(genre)

    if date:
        tags["date"] = str(date)

    if website:
        tags["website"] = str(website)

    tags.save()

