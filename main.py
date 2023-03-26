from pytube import Playlist
from pytube.cli import on_progress

playlist_url = input("Playlist URL: ")
resolution = "720p"

yt = Playlist(playlist_url)

for video in yt.videos:
    print("Downloading:", video.title)
    video.register_on_progress_callback(on_progress)
    stream = video.streams.get_by_resolution(resolution)
    stream.download()

