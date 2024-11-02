import unittest
import sys
from pathlib import Path
from dotenv import load_dotenv
from py_home_music_downloader import utils_path

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

class TestUpdateMetadata(unittest.TestCase):

    def test_reading_url(self):
        title = "testing-Actual Album - somthing_else"
        exected = "Actual Album - somthing_else"

        actual = string_utils.extract_album_name(title)
        self.assertEqual(exected, actual)

    def test_reading_album_name(self):
        title = "Album - Now You're Gone - The Album"
        exected = "Now You're Gone - The Album"

        actual = string_utils.extract_album_name(title)

        self.assertEqual(exected, actual)


    def test_reading_song_name(self):
        title = "Test song Name - ft. artist (152kbit_Opus).mp3"
        exected = "Test song Name - ft. artist.mp3"

        actual = string_utils.extract_song_title(title)

        self.assertEqual(exected, actual)


if __name__ == "__main__":
    unittest.main()
