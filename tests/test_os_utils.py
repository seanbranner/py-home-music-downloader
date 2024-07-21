import pickle
import unittest
import sys
from pathlib import Path
from dotenv import load_dotenv
import os
from youtube_dl import YoutubeDL
import urllib.request
from py_home_music_downloader import os_utils



def load_pkl_object(file_path):
    with open(file_path, "rb") as file:
        test_json = pickle.load(file)
    return test_json


def save_pkl_object(file_name, object_to_save):
    with open(file_name, "wb") as file:
        pickle.dump(object_to_save, file)
        print("Object Saved")


class TestOsUtils(unittest.TestCase):

    def test_get_os(self):
        expected = 'Darwin'
        actual = os_utils.get_operating_system()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
