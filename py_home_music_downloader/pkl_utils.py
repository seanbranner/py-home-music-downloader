import os
import pickle
from pathlib import Path
import sys
import dict_utils

class Pickle:
    pass


try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

output_dir_path = project_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")


def load_pkl_object(file_path):
    with open(file_path, "rb") as file:
        test_json = pickle.load(file)
    return test_json


def save_pkl_object(file_name, object_to_save):
    with open(file_name, "wb") as file:
        # pickle.dump(object_to_save, file)
        pickle.dump(object_to_save, file, protocol=1)
        print("Object Saved")
        file.close()


def get_album_json_list():
    json_dir_path = output_dir_path.joinpath("jsons")
    json_list = os.listdir(json_dir_path)

    album_json_list = []
    for pkl in json_list:
        pkl_path = json_dir_path.joinpath(pkl)
        pkl_json_object = load_pkl_object(pkl_path)
        album_json_list.append(pkl_json_object)
    return album_json_list


def save_all_jsons_from_json_path(list_of_json_objects):
    for result_json_object in list_of_json_objects:
        title = dict_utils.try_dict(result_json_object, "title")
        album_json_path = json_dir_path.joinpath(f"{title}.pkl")
        save_pkl_object(album_json_path, result_json_object)
    return
