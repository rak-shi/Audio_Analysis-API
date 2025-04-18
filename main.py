from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List
import shutil
import os
from utils.audio_processing import extract_features_and_score

app = FastAPI()

UPLOAD_DIR = "temp_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Welcome to MemoTag Audio Analysis API"}

@app.post("/analyze/")
async def analyze_audio(files: List[UploadFile] = File(...)):
    if not 5 <= len(files) <= 10:
        return JSONResponse(
            content={"error": "Please upload between 5 to 10 audio files."},
            status_code=400
        )

    file_paths = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(file_path)

    result = extract_features_and_score(file_paths)

    # Clean up uploaded files
    for path in file_paths:
        os.remove(path)

    return {"result": result}
