import unittest
from py_home_music_downloader import vlc_utils
from pathlib import Path
import sys

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

test_dir = project_path.joinpath("tests")
test_output_dir = test_dir.joinpath('output')


class TestM4aToMp3(unittest.TestCase):

    def test_get_vlc_home(self):
        expected = 'some_path'
        actual = vlc_utils.get_vlc_home()
        print(actual)
        self.assertEqual(expected, actual)


    def test_original_test(self):
        file_path = "example_file_path.m4a"
        new_file_path = "example_new_file_path.mp3"

        cmd_string = (
                '"C:\\Program Files\\VideoLAN\VLC\\vlc.exe" -I dummy "'
                + str(file_path)
                + '" ":sout=#transcode{acodec=mpga,ab=192}:std{dst=\''
                + str(new_file_path)
                + "',access=file}\" vlc://quit"
        )


if __name__ == "__main__":
    unittest.main()