from fastapi import FastAPI, UploadFile, File
import os
from extract_frames import extract_frames
from qdrant_utils import QdrantHandler
from fastapi.responses import FileResponse

app = FastAPI()
qdrant = QdrantHandler()

UPLOAD_DIR = "uploaded_videos"
FRAME_DIR = "extracted_frames"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(FRAME_DIR, exist_ok=True)

@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    video_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(video_path, "wb") as f:
        f.write(await file.read())

    num_frames = extract_frames(video_path, FRAME_DIR)

    for idx, frame_file in enumerate(os.listdir(FRAME_DIR)):
        frame_path = os.path.join(FRAME_DIR, frame_file)
        qdrant.insert_frame(id=idx, image_path=frame_path)

    return {"message": f"Video processed, {num_frames} frames extracted and stored."}

@app.post("/search_similar")
async def search_similar(file: UploadFile = File(...)):
    query_path = os.path.join("query.jpg")
    with open(query_path, "wb") as f:
        f.write(await file.read())

    results = qdrant.search_similar(query_path)

    response = []
    for result in results:
        response.append({
            "score": result.score,
            "frame_path": result.payload["path"]
        })
    return response

@app.get("/get_frame/{frame_filename}")
async def get_frame(frame_filename: str):
    return FileResponse(os.path.join(FRAME_DIR, frame_filename))
