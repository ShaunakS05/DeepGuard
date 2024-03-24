from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List

app = FastAPI()

@app.post("/uploadvideo/")
async def create_upload_video(video: UploadFile = File(...)):
    # Check the file type
    if not video.filename.endswith('.mp4'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an MP4 video.")
    
    # You can now save the video to a file or process it
    # For example, save to disk
    with open(f"./dl.mp4", "wb") as buffer:
        buffer.write(await video.read())

    return {"filename": video.filename}