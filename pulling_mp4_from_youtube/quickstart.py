from pytube import YouTube

yt = YouTube("https://www.youtube.com/shorts/jcNzoONhrmE")

# How do you pull the mp4 file?
# yt.streams.first().download() -> this did not pull sound with the video

# ChatGPT-4 Recommendation -> WORKS
stream = yt.streams.filter(progressive=True).first()
stream.download()