from mutagen.easyid3 import EasyID3
import mutagen
from pathlib import Path
import sys

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = (Path(__file__).parents[1])

project_music_dir = project_path.joinpath("output")
example_artist_path = project_music_dir.joinpath("Shiro SAGISU")
example_album_path = example_artist_path.joinpath("Number One - Bankai")
example_music_file_path = example_album_path.joinpath("Number One.mp3")

try:
    file_object = mutagen.File(example_music_file_path)
    file_object.add_tags()
    file_object.save()
except:
    print('Already has tags')
tags = EasyID3(example_music_file_path)

tags['album']= u'Number One'
example = "example"
print(f"u'{example}'")

tags['bpm']= example
tags['compilation']= u'0'
tags['composer']= u'composer_example'
tags['encodedby']= u'encoded_by_example'
tags['title']= u'Number One'
tags['version']= u'subtitle_example'
tags['artist']= u'contribute_artist_example'
tags['albumartist']= u'Shiro SAGISU'
tags['conductor']= u'conductor_example'
tags['discnumber']= u'part_of_set_flag?'
tags['organization']= u'publishers_example'
tags['tracknumber']= u'2'
tags['genre']= u'Anime'
tags['date']= '2022'
tags['website']= u'author_url_example'

print(tags)

tags.save()

