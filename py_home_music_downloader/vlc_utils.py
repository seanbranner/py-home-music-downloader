import shutil

def get_vlc_home():
    vlc_path = shutil.which("vlc")
    if vlc_path:
        return vlc_path
    else:
        print("VLC not found.")