from youtube_dl import YoutubeDL

# audio_downloder = YoutubeDL({'format': 'bestaudio[ext=m4a]/best[ext=mp4]/best'})
audio_downloder = YoutubeDL({'format': 'bestaudio[ext=mmp4]/best[ext=mp4]/best'})


def download_url(url_to_download):
    try:
        audio_downloder.extract_info(url_to_download)
    except:
        print("Didnt work for:" + url_to_download)
