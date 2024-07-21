import unittest
from py_home_music_downloader import convert_m4a_to_mp3
from pathlib import Path
import sys

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

test_dir = project_path.joinpath("tests")
test_output_dir = test_dir.joinpath('output')


class TestM4aToMp3(unittest.TestCase):

    def test_get_mp3_convert_cmd_list(self):
        file_path = "/Users/seanyb05/Documents/Projects/Python/py-home-music-downloader/tests/output/test_file.m4a"
        new_file_path = "/Users/seanyb05/Documents/Projects/Python/py-home-music-downloader/tests/output/test_file.mp3"
        expected = [(
                '"/Applications/VLC.app/Contents/MacOS/VLC" -I dummy "'
                +str(file_path)
                +'" ":sout=#transcode{acodec=mpga,ab=192}:std{dst=\''
                +str(new_file_path)
                +"',access=file}\" vlc://quit"
        )]
        actual = convert_m4a_to_mp3.get_mp3_convert_cmd_list(test_output_dir)
        self.assertEqual(expected, actual)

    def test_run_conversion(self):
        expected = 1
        actual = convert_m4a_to_mp3.run_conversion()
        self.assertEqual(expected, actual)

    def test_convert_ffmpeg(self):
        expected = 1
        actual = convert_m4a_to_mp3.run_ffmpeg_conversion(test_output_dir)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()