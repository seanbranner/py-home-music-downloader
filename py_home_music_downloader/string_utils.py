def extract_album_name(title):
    split_album = title.split("-")
    split_album.pop(0)
    return "-".join(split_album).strip()

def extract_song_title(song_title):
    split_album = song_title.split("[")
    split_album.pop(-1)
    new_song_title = "-".join(split_album).strip()
    return f"{new_song_title}"

if __name__ == '__main__':
    example_title = "Everything Black [7OQ0I7nc15c].mp3"
    print(extract_song_title(example_title))