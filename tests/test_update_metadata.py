import pickle
import unittest
import sys
from pathlib import Path
from dotenv import load_dotenv
import os
from youtube_dl import YoutubeDL
import urllib.request

load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

project_music_dir = project_path.joinpath("output")

test_path = project_path.joinpath("tests")
test_resource_path = test_path.joinpath("resources")

output_dir_path = test_resource_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")


def load_pkl_object(file_path):
    file_name = test_resource_path.joinpath(file_path)
    with open(file_name, "rb") as file:
        test_json = pickle.load(file)
    return test_json


def save_pkl_object(file_name, object_to_save):
    with open(file_name, "wb") as file:
        pickle.dump(object_to_save, file)
        print("Object Saved")


def build_music_directories():
    output_dir_path = project_path.joinpath("output")
    json_dir_path = output_dir_path.joinpath("jsons")
    json_list = os.listdir(json_dir_path)

    pkl_json_list = []
    for pkl in json_list:
        pkl_path = json_dir_path.joinpath(pkl)
        pkl_json_object = load_pkl_object(pkl_path)
        pkl_json_list.append(pkl_json_object)

    for input_json in pkl_json_list:
        type = input_json["_type"]
        entries = input_json["entries"]
        id = input_json["id"]
        title = input_json["title"]
        extractor = input_json["extractor"]
        webpage_url = input_json["webpage_url"]
        webpage_url_basename = input_json["webpage_url_basename"]
        extractor_key = input_json["extractor_key"]

        artist = entries[0]["artist"].split(",")[0].strip()
        album = title.split("-")[-1].strip()
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

        print(album_path)

        urllib.request.urlretrieve(url=thumbnail, filename=thumbnail_path)

        # for song_details in entries:
        #     title = song_details['title']
        #     print(title)
        #     playlist_index = song_details['playlist_index']  # tracknumber
        #     print(playlist_index)
        #     webpage_url = song_details['webpage_url']#website
        #     print(webpage_url)
        #     release_year = song_details['release_year']
        #     print(release_year)
        #     tags = song_details['tags']  # conductor
        #     print(tags)
        #     id = song_details['id']
        #     formats = song_details['formats']
        #     thumbnails = song_details['thumbnails']
        #     description = song_details['description']
        #     upload_date= song_details['upload_date']
        #     uploader= song_details['uploader']
        #     uploader_id = song_details['uploader_id']
        #     uploader_url = song_details['uploader_url']
        #     channel_id = song_details['channel_id']
        #     channel_url = song_details['channel_url']
        #     duration = song_details['duration']
        #     view_count = song_details['view_count']
        #     average_rating = song_details['average_rating']
        #     age_limit= song_details['age_limit']
        #     webpage_url= song_details['webpage_url']
        #     categories= song_details['categories']
        #     tags= song_details['tags']
        #     is_live= song_details['is_live']
        #     album= song_details['album']
        #     track= song_details['track']
        #     release_date= song_details['release_date']
        #     release_year= song_details['release_year']
        #     channel= song_details['channel']
        #     creator = song_details['creator']
        #     alt_title= song_details['alt_title']
        #     extractor= song_details['extractor']
        #     webpage_url_basename= song_details['webpage_url_basename']
        #     extractor_key= song_details['extractor_key']
        #     n_entries= song_details['n_entries']
        #     playlist= song_details['playlist']
        #     playlist_id= song_details['playlist_id']
        #     playlist_title= song_details['playlist_title']
        #     playlist_uploader= song_details['playlist_uploader']
        #     playlist_uploader_id= song_details['playlist_uploader_id']
        #     playlist_index= song_details['playlist_index']
        #     thumbnail= song_details['thumbnail']
        #     display_id= song_details['display_id']
        #     requested_subtitles= song_details['requested_subtitles']
        #     asr= song_details['asr']
        #     filesize= song_details['filesize']
        #     format_id= song_details['format_id']
        #     format_note= song_details['format_note']
        #     fps = song_details['fps']
        #     height= song_details['height']
        #     quality= song_details['quality']
        #     tbr= song_details['tbr']
        #     url= song_details['url']
        #     width= song_details['width']
        #     ext= song_details['ext']
        #     vcodec= song_details['vcodec']
        #     acodec= song_details['acodec']
        #     abr= song_details['abr']
        #     downloader_options= song_details['downloader_options']
        #     container= song_details['container']
        #     format= song_details['format']
        #     protocol= song_details['protocol']
        #     http_headers= song_details['http_headers']

        # exit('manual exit')


class TestUpdateMetadata(unittest.TestCase):

    def test_reading_url(self):
        youtube_dl_object = load_pkl_object(example_playlist_path)
        build_music_directories()

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
