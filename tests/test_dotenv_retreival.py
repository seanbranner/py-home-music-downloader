import os
from dotenv import load_dotenv

load_dotenv()

music_list = os.getenv("URL_LIST")
print(music_list.split())