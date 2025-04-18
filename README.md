# Audio_Analysis-API

This project is a FastAPI-based backend that analyzes 5–10 audio files to extract speech features and calculate a cognitive risk score. It supports file uploads, processes audio using custom utilities, and returns results via a REST API.

---

## 📜 Project Overview

This API processes uploaded audio files, extracts key speech features (MFCC, ZCR, RMS), and calculates a cognitive risk score. The application is built using FastAPI and deployed on Render.

---

## 🛠 Installation

### Requirements:
- Python 3.7 or higher
- pip (Python package installer)
- system dependencies like `ffmpeg` for audio processing

### Steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Audio_Analysis-API.git
    cd Audio_Analysis-API
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install system dependencies (for audio processing):**
    - If you're using `librosa` for audio processing, you may need `ffmpeg` or `libsndfile`. You can install `ffmpeg` with:
      ```bash
      sudo apt-get install ffmpeg  # For Ubuntu
      brew install ffmpeg          # For MacOS
      ```

---

## ⚙️ Usage

### Running Locally:

To run the FastAPI server locally, use the following command:
```bash
uvicorn app.main:app --reload
