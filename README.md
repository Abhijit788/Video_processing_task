
# Video Feature Vector API (FastAPI + Qdrant)

---

## Problem Statement

- Upload a video (MP4)
- Extract frames every second
- Compute simple feature vectors (Color Histogram)
- Store vectors into a vector database (Qdrant)
- Allow retrieval of similar frames via API

---

## Tech Stack

- FastAPI
- OpenCV
- Qdrant (in-memory)
- Python
- NumPy

---

# 🔧 Setup Instructions

---

## ✅1️⃣ Running Locally

### Step 1 — Clone the repository

```bash
git clone https://github.com/Abhijit788/Video_processing_task.git
```

### Step 2 — Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run FastAPI server

```bash
uvicorn main:app --reload
```

### Step 5 — Test API locally

- Open Swagger UI in your browser:  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can upload videos, extract frames, search for similar frames, and download frames directly from this Swagger UI interface.

---

## ✅ 2️⃣ Running on GitHub Codespaces

### Step 1 — Open Codespaces and clone the repository

Use Codespaces on GitHub and open the repo directly.

### Step 2 — Install dependencies (inside Codespaces terminal)

```bash
pip install -r requirements.txt
```

### Step 3 — Run FastAPI server (important to expose port)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

> ✅ The `--host 0.0.0.0` ensures Codespaces can forward port 8000 to the public preview URL.

### Step 4 — Access Swagger UI in browser

Once running, Codespaces will give you a forwarded URL like:

```
https://<your-codespace-id>-8000.githubpreview.dev/docs
```

- Open this URL in your browser to access the interactive Swagger UI.
- You can fully test all API endpoints directly here.

---

# 🚀 API Endpoints Summary

| Endpoint | Method | Description |
| -------- | ------ | ----------- |
| `/upload_video` | POST | Upload a video file and extract frames |
| `/search_similar` | POST | Upload an image to find similar frames |
| `/get_frame/{frame_filename}` | GET | Download specific frame by filename |

---

# 🧪 How to Use Swagger UI for Testing

### 1️⃣ Upload Video

- Select `/upload_video` endpoint
- Click **"Try it out"**
- Upload your video file (MP4)
- Click **Execute**

### 2️⃣ Search Similar Frames

- Select `/search_similar` endpoint
- Click **"Try it out"**
- Upload an image file to search
- Click **Execute**

### 3️⃣ Download Frame

- Select `/get_frame/{frame_filename}` endpoint
- Enter a frame filename (from search result)
- Click **Execute**

---

# 📂 Project Directory Structure

- `uploaded_videos/` → Uploaded videos are stored here.
- `extracted_frames/` → Extracted frames from video.

---

# 📊 Sample Search Response

```json
[
  {
    "score": 0.002,
    "frame_path": "extracted_frames/frame_0.jpg"
  },
  {
    "score": 0.015,
    "frame_path": "extracted_frames/frame_1.jpg"
  }
]
```

---
✅ Both **local testing** and **Codespaces testing** are fully supported.
---

# ✅ Done!
