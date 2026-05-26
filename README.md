# Face Recognition Demo with DeepFace

This is a simple demo script for face recognition using the DeepFace library.

## Features

- Face verification: Check if two faces belong to the same person
- Face detection: Detect faces in an image

## Requirements

- Python 3.7+
- DeepFace library
- OpenCV

Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the script:
```
python face.py
```

Choose the demo option:
1. Face Verification
2. Face Detection

## Troubleshooting

- If you get import errors, ensure DeepFace is installed: `pip install deepface`
- For face verification, the script uses sample images from URLs. Replace with your own image paths if needed.
- DeepFace requires internet connection for downloading models on first run.
- If camera is not working (in original code), ensure OpenCV can access your webcam.

## Notes

- Face verification uses a threshold to determine if faces match.
- The demo uses public domain images for demonstration purposes.