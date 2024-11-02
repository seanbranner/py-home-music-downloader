import os
import unittest
import sys
from pathlib import Path
from dotenv import load_dotenv
import getpass
from py_home_music_downloader import utils_path

load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

test_path = project_path.joinpath("tests")
test_resource_path = test_path.joinpath("resources")

output_dir_path = test_resource_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")

music_dir = Path("/CHANSEY/Music")



class TestUpdateMetadata(unittest.TestCase):


    def test_reading_album_name(self):
        expected = "title name"
        actual = "somthing else"
        print(music_dir)
        self.assertEqual(expected, actual)

    def test_reading_download(self):
        download_path = utils_path.get_home_download_dir()
        download_files = os.listdir(download_path)
        determine_file_types(download_files)


if __name__ == "__main__":
    unittest.main()
