import unittest
import sys
from pathlib import Path
from dotenv import load_dotenv
from ShazamAPI import Shazam
load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = Path(__file__).parents[1]

test_path = project_path.joinpath("tests")
test_resource_path = test_path.joinpath("resources")

output_dir_path = test_resource_path.joinpath("output")
json_dir_path = output_dir_path.joinpath("jsons")

music_dir = Path("/CHANSEY/Music")
download_dir = Path('/home/someoneover9000/Downloads')

def get_test_response():
    test_response = (18.0, {'matches': [{'id': '261694679', 'offset': 9.991035156, 'timeskew': -5.2690506e-05, 'frequencyskew': 0.0}],
        'location': {'accuracy': 0.01},
        'timestamp': 1716072198380,
        'timezone': 'Europe/Moscow',
        'track': {
            'layout': '5',
            'type': 'MUSIC',
            'key': '50410163',
            'title': 'Brick By Boring Brick',
            'subtitle': 'Paramore',
            'images': {
                'background': 'https://is1-ssl.mzstatic.com/image/thumb/Music122/v4/3f/96/79/3f96799e-b6e5-0d32-c39f-475523d928f6/pr_source.png/800x800cc.jpg',
                'coverart': 'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/42/48/29/424829a6-42fe-77e7-770e-a760f54ec3de/dj.qnyuzqoy.jpg/400x400cc.jpg',
                'coverarthq': 'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/42/48/29/424829a6-42fe-77e7-770e-a760f54ec3de/dj.qnyuzqoy.jpg/400x400cc.jpg',
                'joecolor': 'b:f0e9e3p:010000s:3d250ft:312e2dq:604c39'
            },
            'share': {
                'subject': 'Brick By Boring Brick - Paramore',
                'text': 'Brick By Boring Brick от Paramore',
                'href': 'https://www.shazam.com/track/50410163/brick-by-boring-brick',
                'image': 'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/42/48/29/424829a6-42fe-77e7-770e-a760f54ec3de/dj.qnyuzqoy.jpg/400x400cc.jpg',
                'twitter': 'Мое открытие на @Shazam: Paramore – Brick By Boring Brick.',
                'html': 'https://www.shazam.com/snippets/email-share/50410163?lang=ru&country=RU',
                'avatar': 'https://is1-ssl.mzstatic.com/image/thumb/Music122/v4/3f/96/79/3f96799e-b6e5-0d32-c39f-475523d928f6/pr_source.png/800x800cc.jpg',
                'snapchat': 'https://www.shazam.com/partner/sc/track/50410163'
            },
            'hub': {
                'type': 'APPLEMUSIC',
                'image': 'https://images.shazam.com/static/icons/hub/ios/v5/applemusic_{scalefactor}.png',
                'actions': [
                    {'name': 'apple', 'type': 'applemusicplay', 'id': '604800417'},
                    {
                        'name': 'apple',
                        'type': 'uri',
                        'uri': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/cb/57/5e/cb575e86-6cac-06ec-f23d-ea1290dfe1bb/mzaf_3373440840509376472.plus.aac.ep.m4a'
                    }],
                'options': [{'caption': 'ОТКРЫТЬ В', 'actions': [{'name': 'hub:applemusic:deeplink', 'type': 'applemusicopen', 'uri': 'https://music.apple.com/ru/album/brick-by-boring-brick/604800411?i=604800417&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios'}, {'name': 'hub:applemusic:deeplink', 'type': 'uri', 'uri': 'https://music.apple.com/ru/album/brick-by-boring-brick/604800411?i=604800417&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios'}], 'beacondata': {'type': 'open', 'providername': 'applemusic'}, 'image': 'https://images.shazam.com/static/icons/hub/ios/v5/overflow-open-option_{scalefactor}.png', 'type': 'open', 'listcaption': 'Открыть в Apple Music', 'overflowimage': 'https://images.shazam.com/static/icons/hub/ios/v5/applemusic-overflow_{scalefactor}.png', 'colouroverflowimage': False, 'providername': 'applemusic'}, {'caption': 'КУПИТЬ', 'actions': [{'type': 'uri', 'uri': 'https://itunes.apple.com/ru/album/brick-by-boring-brick/604800411?i=604800417&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=itunes&itsct=Shazam_ios'}], 'beacondata': {'type': 'buy', 'providername': 'itunes'}, 'image': 'https://images.shazam.com/static/icons/hub/ios/v5/itunes-overflow-buy_{scalefactor}.png', 'type': 'buy', 'listcaption': 'Купить на iTunes', 'overflowimage': 'https://images.shazam.com/static/icons/hub/ios/v5/itunes-overflow-buy_{scalefactor}.png', 'colouroverflowimage': False, 'providername': 'itunes'}], 'providers': [{'caption': 'Открыть в Spotify', 'images': {'overflow': 'https://images.shazam.com/static/icons/hub/ios/v5/spotify-overflow_{scalefactor}.png', 'default': 'https://images.shazam.com/static/icons/hub/ios/v5/spotify_{scalefactor}.png'}, 'actions': [{'name': 'hub:spotify:searchdeeplink', 'type': 'uri', 'uri': 'spotify:search:Brick%20By%20Boring%20Brick%20Paramore'}], 'type': 'SPOTIFY'}, {'caption': 'Открыть в Deezer', 'images': {'overflow': 'https://images.shazam.com/static/icons/hub/ios/v5/deezer-overflow_{scalefactor}.png', 'default': 'https://images.shazam.com/static/icons/hub/ios/v5/deezer_{scalefactor}.png'}, 'actions': [{'name': 'hub:deezer:searchdeeplink', 'type': 'uri', 'uri': 'deezer-query://www.deezer.com/play?query=%7Btrack%3A%27Brick+By+Boring+Brick%27%20artist%3A%27Paramore%27%7D'}], 'type': 'DEEZER'}], 'explicit': False, 'displayname': 'APPLE MUSIC'},
            'sections': [
                {
                    'type': 'SONG',
                    'metapages': [
                        {
                            'image': 'https://is1-ssl.mzstatic.com/image/thumb/Music122/v4/3f/96/79/3f96799e-b6e5-0d32-c39f-475523d928f6/pr_source.png/800x800cc.jpg',
                            'caption': 'Paramore'
                        }, {'image': 'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/42/48/29/424829a6-42fe-77e7-770e-a760f54ec3de/dj.qnyuzqoy.jpg/400x400cc.jpg',
                            'caption': 'Brick By Boring Brick'
                            }],
                    'tabname': 'Песня',
                    'metadata': [{'title': 'Альбом', 'text': 'Brand New Eyes'}, {'title': 'Лейбл', 'text': 'Fueled By Ramen'}, {'title': 'Выпущено', 'text': '2009'}]}, {'type': 'RELATED', 'url': 'https://cdn.shazam.com/shazam/v3/ru/RU/iphone/-/tracks/track-similarities-id-50410163?startFrom=0&pageSize=20&connected=', 'tabname': 'Похожие'}], 'url': 'https://www.shazam.com/track/50410163/brick-by-boring-brick', 'artists': [{'id': '42', 'adamid': '75950796'}], 'isrc': 'USAT21300101', 'genres': {'primary': 'Альтернатива'}, 'urlparams': {'{tracktitle}': 'Brick+By+Boring+Brick', '{trackartist}': 'Paramore'}, 'myshazam': {'apple': {'actions': [{'name': 'myshazam:apple', 'type': 'uri', 'uri': 'https://music.apple.com/ru/album/brick-by-boring-brick/604800411?i=604800417&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios'}]}}, 'highlightsurls': {}, 'relatedtracksurl': 'https://cdn.shazam.com/shazam/v3/ru/RU/iphone/-/tracks/track-similarities-id-50410163?startFrom=0&pageSize=20&connected=', 'albumadamid': '604800411'}, 'tagid': '7445F482-A967-4D53-B1EC-7C026F1C6D42'})
    return test_response

class TestGetMusicDetails(unittest.TestCase):


    def test_shazam_collection_result(self):
        music_file_path = music_dir.joinpath("Paramore").joinpath("4. Brick by Boring Brick - Paramore.mp3")
        file_content_to_recognize = open(music_file_path,'rb').read()

        shazam = Shazam(file_content_to_recognize)
        recognize_generator = shazam.recognizeSong()
        response = next(recognize_generator)

        title = response()

        expected = "title name"
        actual = "somthing else"
        print(music_dir)
        self.assertEqual(expected, actual)

    def test_read_shazam_result(self):

        response = get_test_response()

        track = response[1]['track']
        keys = track.keys()
        title = track['title']
        artist = track['subtitle']
        album = track['sections'][0]['metadata'][0]['text']
        record_label = track['sections'][0]['metadata'][1]['text']

        print(keys,"\n",title,artist,album,record_label)
        # self.assertEqual(expected, actual)

    def test_read_all_new(self):

        music_file_path = download_dir.joinpath("- Album – Metallica").joinpath("Of Wolf And Man (128kbit_AAC).m4a")
        file_content_to_recognize = open(music_file_path,'rb').read()

        shazam = Shazam(file_content_to_recognize)
        recognize_generator = shazam.recognizeSong()
        response = next(recognize_generator)

        track = response[1]['track']
        keys = track.keys()
        title = track['title']
        artist = track['subtitle']
        album = track['sections'][0]['metadata'][0]['text']
        record_label = track['sections'][0]['metadata'][1]['text']

        print(f"""
            {keys}
            title = {title},
            artist = {artist},
            album = {album},
            record_label = {record_label}
        """)
        # self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
