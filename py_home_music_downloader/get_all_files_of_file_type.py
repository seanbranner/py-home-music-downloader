import os
from pathlib import Path
def input_file_is_mp3(file):
    extension = str(file).split(".")[-1]
    return extension == "mp3"


def input_file_is_mp4(file):
    extension = str(file).split(".")[-1]
    return extension == "mp4"


def input_file_is_m4a(file):
    extension = str(file).split(".")[-1]
    return extension == "m4a"


def input_file_is_opus(file):
    extension = str(file).split(".")[-1]
    return extension == "opus"

def input_file_is_audio(file):
    if input_file_is_opus(file) or input_file_is_mp4(file) or input_file_is_m4a(file) or input_file_is_mp3(file):
        return True
    return False

def get_all_files_of_file_type(dir_path = None):
    file_path_list = []
    input_dir_file_list = os.listdir(dir_path)

    for file_name in input_dir_file_list:
        file_path = dir_path.joinpath(file_name)
        file_is_dir = os.path.isdir(file_path)
        file_is_audio = input_file_is_audio(file_path)
        if file_is_dir:
            file_path_list.extend(get_all_files_of_file_type(file_path))

        else:
            if input_file_is_m4a(file_path):
                file_path_list.append(file_path)
            else:
                pass
    return file_path_list

if __name__ == '__main__':
    input_file = Path("D:\Music")
    mp3_files = get_all_files_of_file_type(dir_path=input_file)
    print(len(mp3_files))
    print(mp3_files)
