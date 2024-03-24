from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pytube import YouTube
import io

app = FastAPI()

@app.get("/mp4/")
def get_mp4(youtube_link: str="https://www.youtube.com/shorts/jcNzoONhrmE"):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)
    
    # Select the highest quality progressive stream
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    if not stream:
        raise HTTPException(status_code=404, detail="Suitable video stream not found")

    # Define a generator to buffer video data
    def iter_video():
        with io.BytesIO() as video_buffer:
            # Stream the video content into the buffer
            stream.stream_to_buffer(buffer=video_buffer)
            # Reset buffer's current position to the beginning
            video_buffer.seek(0)
            # Stream content from buffer to response
            while chunk := video_buffer.read(4096):
                yield chunk

    # Return streaming response
    return StreamingResponse(iter_video(), media_type="video/mp4")

# Curl Command to Download video to your local directory:
# curl -o downloaded_video.mp4 "http://127.0.0.1:8000/mp4/?youtube_link=https://www.youtube.com/shorts/jcNzoONhrmE"

@app.get("/thumbnail_and_title/")
def get_thumbnail_and_title(youtube_link: str="https://www.youtube.com/shorts/jcNzoONhrmE"):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)

    # Return streaming response
    return {"Title": yt.title , "Thumbnail_URL":yt.thumbnail_url}

# Curl Command to get thumnail:
# curl http://127.0.0.1:8000/thumbnail_and_title/?youtube_link=https://www.youtube.com/shorts/jcNzoONhrmE
