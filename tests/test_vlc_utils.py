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

    def test_get_vlc_home_windows(self):
        expected = 'C:\\Program Files\\VideoLAN\VLC\\vlc.exe'
        actual = vlc_utils.get_vlc_home('Windows')
        self.assertEqual(expected, actual)

    def test_get_vlc_home_mac(self):
        expected = '/Applications/VLC.app/Contents/MacOS/VLC'
        actual = vlc_utils.get_vlc_home('Darwin')
        print(actual)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()