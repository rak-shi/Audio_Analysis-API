<<<<<<< HEAD1
# MemoTag Speech Intelligence API

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
=======
# Audio_Analysis-API
This  project is a FastAPI/flask-based backend that analyzes 5 -10 audio files to extract speech features and calculates a cognitive risk score. It supports file uploads, processes audio using custom utilities, and returns results via a REST API.
# MemoTag Audio Analysis API

This project provides an API to analyze audio files and calculate cognitive risk scores based on speech features such as MFCC (Mel-frequency cepstral coefficients), ZCR (zero-crossing rate), and RMS (root mean square). The API accepts 5-10 audio files and returns detailed analysis with a calculated risk score.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Optional Frontend](#optional-frontend)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Requirements:
- Python 3.7 or higher
- pip (Python package installer)

### Steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/fastapi-audio-analysis.git
    cd fastapi-audio-analysis
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate     # For Windows
    ```

3. **Install the required dependencies:**
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

## Usage

### Running the FastAPI Application Locally:
To start the FastAPI server locally, run:
```bash
uvicorn app:app --reload
>>>>>>> bdde778ec0c9f2b0e4fa5de5d26561b09875fea4
