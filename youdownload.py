import os
from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))
#videos = yt.get_videos()

videos = yt.streams.all()

s = 1
for v in videos:
    print(str(s)+". "+str(v))
    s += 1

n = int(input("Enter the number of the video: "))
vid = videos[n-1]

home = os.path.expanduser('~')
destination = os.path.join(home, 'Downloads')
#destination = (r"C:\Users\win\Desktop\Youtube")
vid.download(destination)

print("\n Successfully downloaded")
