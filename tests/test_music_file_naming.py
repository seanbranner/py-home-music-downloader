example_file_name = "WAKE UP-fCd78KkOrFc.mp4"

def convert_name(initial_name):

    new_name_list = initial_name.split("-")

    return f"{new_name_list[0]}.mp4"

print(convert_name(example_file_name))

os.rename('a.txt', 'b.kml')
