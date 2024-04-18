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


def extract_album_name(title):
    split_album = title.split("-")
    split_album.pop(0)
    return "-".join(split_album).strip()


class TestUpdateMetadata(unittest.TestCase):

    def test_reading_url(self):
        title = "testing-Actual Album - somthing_else"
        exected = "Actual Album - somthing_else"

        actual = extract_album_name(title)
        self.assertEqual(exected, actual)

    def test_reading_album_name(self):
        title = "Album - Now You're Gone - The Album"
        exected = "Now You're Gone - The Album"

        actual = extract_album_name(title)

        self.assertEqual(exected, actual)

    def test_reading_album_name_2(self):
        title = "Album - Now You're Gone"
        exected = "Now You're Gone"

        actual = extract_album_name(title)
        self.assertEqual(exected, actual)


if __name__ == "__main__":
    unittest.main()
