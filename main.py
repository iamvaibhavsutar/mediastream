from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

# Define the absolute path for storing videos
UPLOAD_DIR = "/home/vaibhav/programs/mediastream-hub/videos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to MediaStream Hub!"}

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Video uploaded successfully", "filename": file.filename}

@app.get("/videos/{filename}")
async def get_video(filename: str):
    file_path = f"/app/videos/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="video/mp4")
    return {"error": "Video not found"}
