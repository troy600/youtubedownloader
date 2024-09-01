import os
import subprocess

delfile = '/tmp/21.png'
delfile2 = "/tmp/imafile.webp"

for keycontext in os.listdir("/tmp"):
    if keycontext == '21.png':
        os.remove(f"{delfile}")
    elif keycontext == 'imafile.webp':
        os.remove(delfile2)
    elif keycontext == 'pske.m4a':
        os.remove("/tmp/pske.m4a")
    elif keycontext == "pske.mp3":
        os.remove("/tmp/pske.mp3")


#magic wahahahah
print("type the youtube link you want to download. \n")

link = input('>>')

namemusi = input("name of the music\n >>")
namemusic = f'"{namemusi}"'

flink = f'{link}'
print("Downloading the thumbnail")

os.system(f"/usr/bin/yt-dlp '{flink}' --embed-thumbnail --no-download  -o /tmp/imafile")



os.system(f'ffmpeg -i /tmp/imafile.webp -vf "crop=w=min(min(iw\,ih)\,720):h=min(min(iw\,ih)\,720),scale=720:720,setsar=1" -vframes 1 /tmp/21.png')

os.system(f'yt-dlp -f140 "{flink}" --embed-metadata --parse-metadata "playlist_index:%(track_number)s" -o /tmp/pske.m4a')
os.system("ffmpeg -i /tmp/pske.m4a -c:a libmp3lame /tmp/pske.mp3")
os.system(f"ffmpeg -i /tmp/pske.mp3 -i /tmp/21.png -map 1:0 -map 0:0 -c copy {namemusic}")

print("success :)")
