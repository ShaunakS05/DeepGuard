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

@app.get("/thumbnail_and_title/")
def get_thumbnail_and_title(youtube_link: str="https://www.youtube.com/shorts/jcNzoONhrmE"):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)

    # Return streaming response
    return {"Title": yt.title , "Thumbnail_URL":yt.thumbnail_url}

# from fastapi import FastAPI, File, UploadFile, Response
# from pytube import YouTube
# import shutil
# import os

# app = FastAPI()

# @app.get("/download_video")
# async def download_video():
#     # Replace 'your_path' with the path where you want to save the downloaded video
#     save_path = '/'

#     # Create a YouTube object
#     yt = YouTube(f'https://www.youtube.com/shorts/jcNzoONhrmE')

#     # Download the best quality video
#     video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#     if video_stream:
#         filename = video_stream.default_filename
#         video_stream.download(output_path=save_path, filename=filename)
        
#         # Define path to the downloaded video
#         file_path = os.path.join(save_path, filename)

#         # Return the video as a response
#         return Response(content=open(file_path, "rb"), media_type="video/mp4")
#     else:
#         return {"error": "Video could not be downloaded"}
