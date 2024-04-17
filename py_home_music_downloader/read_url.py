import urllib.request

target_url = "https://music.youtube.com/playlist?list=OLAK5uy_mJ8FwUHZ2hnUcnIETTnwvKUeH6FU0FrZw&si=qh8UERifG405va5F"

f = urllib.request.urlopen(target_url)
myfile = f.read()
print(myfile)
