from pytube import Playlist, YouTube
from moviepy.editor import *
import os


def choose(a, b, title="Choose"):
    print(f"{title}: ")
    print(f"a. {a}")
    print(f"b. {b}")
    print("Which one a or b?    \t", end="")
    c = input()
    if 'a' in c:
        return True
    else:
        return False


def cvtm(file):
    # convert video to music
    mp4_file = file
    mp3_file = mp4_file.replace('mp4', 'mp3')

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()


def dv(url, path, convert=False):
    # download video
    yt = YouTube(url)
    vd = yt.streams.get_highest_resolution()  # TODO change to select resolution
    vd.download(path)
    print(f"Download Done: {vd.title}")
    if convert == True:
        cvtm(f"{path}\{vd.title}.mp4")
        os.remove(f"{path}\{vd.title}.mp4")


print("ENTER URL: ", end="")
url = input()


if "playlist" in url:
    pl = Playlist(url)
    # path = f"D:\Personal Assets\Videos\\test\{pl.title}"
    print(f'Number of videos in playlist: {len(pl.video_urls)}')
    if choose("Full playlist", "Some of the videos"):
        print("Path where to download: ", end="")
        path = f"{input()}\{pl.title}"
        if choose("mp4", "mp3", "Choose Format"):
            for url in pl.video_urls:
                dv(url, path)
        else:
            for url in pl.video_urls:
                dv(url, path, True)
    else:
        print("Start: ", end="")
        start = int(input())
        print("End: ", end="")
        end = int(input())
        print("Path where to download: ", end="")
        path = f"{input()}\{pl.title}"
        # download form start to end numbers
        if choose("mp4", "mp3", "Choose Format"):
            for index in range(start, end):
                url = pl.video_urls[index - 1]
                dv(url, path)
        else:
            for index in range(start, end):
                url = pl.video_urls[index - 1]
                dv(url, path, True)
else:
    print("Path where to download: ", end="")
    path = input()
    if choose("mp4", "mp3", "Choose Format"):
        dv(url, path)
    else:
        dv(url, path, True)
    # yt.download(path)


# print(pl.video_urls)
