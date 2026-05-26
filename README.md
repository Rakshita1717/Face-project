# Face Recognition Demo using DeepFace and OpenCV

## Overview

This project is a simple AI-based Face Recognition and Face Detection system developed using Python, DeepFace, OpenCV, and TensorFlow. The project demonstrates how Artificial Intelligence, Deep Learning, and Computer Vision techniques can be used to detect, compare, and verify human faces from images.

The project is designed especially for beginners who want to understand the basics of face recognition technology and how modern AI models work in real-world applications. It provides a simple implementation of face verification and face detection using pre-trained deep learning models.

---

## Features

### 1. Face Verification
- Compares two face images.
- Checks whether both images belong to the same person.
- Returns verification result (`True` or `False`).
- Displays similarity distance and threshold values.

### 2. Face Detection
- Detects human faces from an image.
- Returns facial area coordinates.
- Uses DeepFace and OpenCV for accurate detection.

### 3. Beginner Friendly
- Simple and easy-to-understand Python code.
- Clean project structure.
- Easy setup and installation process.

---

## Technologies Used

- Python
- DeepFace
- OpenCV
- TensorFlow
- tf-keras
- Computer Vision
- Deep Learning

---

## How It Works

The project uses DeepFace, which internally applies deep learning models such as:
- Facenet
- ArcFace
- VGG-Face

The workflow of the project is:

1. Read input image
2. Detect human face
3. Extract facial features (embeddings)
4. Compare facial embeddings
5. Return verification result

Face detection is performed using computer vision techniques, while face verification uses neural network-based deep learning models.

---

## Project Structure

```text
face_project/
│
├── face.py
├── requirements.txt
├── README.md
├── img1.jpg
├── img2.jpg
