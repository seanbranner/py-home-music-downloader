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

json_dir_path = project_music_dir.joinpath("jsons")


def load_pkl_object(file_path):
    with open(file_path, "rb") as file:
        test_json = pickle.load(file)
    return test_json


test_json_path = json_dir_path.joinpath("Album - GOOD NUMBERS.pkl")

test_json = load_pkl_object(test_json_path)
print("test_json_loaded")
print(test_json)
