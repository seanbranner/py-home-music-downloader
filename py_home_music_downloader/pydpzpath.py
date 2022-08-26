from pathlib import Path
import sys
import os
import shutil

def get_root_path():
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = (Path(__file__).parents[1])

    return Path(base_path)

def create_dir(dir_name):
    os.mkdir(dir_name)

def convert_string_to_path(path_string):
    return Path(path_string)

def delete_path(delete_path):
    # pathlibPath.exists()
    try:
        if os.path.isdir(delete_path):
            # os.rmdir(delete_path)
            shutil.rmtree(delete_path)
        if os.path.isfile(delete_path):
            os.remove(delete_path)
        print("NOTE: Removed: " + str(delete_path))
    except OSError as e:
        print("Error: %s : %s" % (delete_path, e.strerror))

def isdir(input_path):
    return os.path.isdir(input_path)