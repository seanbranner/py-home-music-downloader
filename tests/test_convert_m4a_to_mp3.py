file_path = 'example_file_path.m4a'
new_file_path = 'example_new_file_path.mp3'

cmd_string = "\"C:\\Program Files\\VideoLAN\VLC\\vlc.exe\" -I dummy \"" + str(
    file_path) + "\" \":sout=#transcode{acodec=mpga,ab=192}:std{dst=\'" + str(
    new_file_path) + "\',access=file}\" vlc://quit"

