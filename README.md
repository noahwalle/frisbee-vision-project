# COSC428 Frisbee Tracking Project

This repository contains the implementation of a computer vision system for detecting, tracking, and analyzing frisbee trajectories in gameplay footage. Developed as part of the COSC428 Computer Vision course at the University of Canterbury, the project leverages a combination of deep learning, image processing, and object tracking methods.

---

## Project Structure
```
.
├── contour_detect.py
├── csrt_tracker.py
├── extract_frames.py
├── image_processing.py
├── kcf_tracker.py
├── masking.py
├── yolo.py
├── Footage/
├── datasets/
├── runs/
└── README.md
```

---

## Requirements

Install the following dependencies:

- Python
- OpenCV
- NumPy
- tqdm
- Ultralytics YOLO

Install with pip:

```bash
pip install opencv-python numpy tqdm ultralytics
````
- NB: Some scripts may only run with opencv-contrib-python
---

## Frame Extraction

**Script:** `extract_frames.py`

This script randomly selects frames from an input video and saves them to the `Training/` directory.

### Usage

Edit the video path inside the script:

```python
extract_random_frames("/path/to/your/video.mp4", num_frames=750)
```

---

## Image Preprocessing

**Script:** `image_processing.py`

Processes each frame using grayscale conversion, Gaussian blur, and binary thresholding. It displays a grid of different image representations side-by-side for visual inspection.

### Controls

* Press `n` to move to the next frame
* Press `q` to quit

---

## YOLOv8 Object Detection

**Script:** `yolo.py`

Uses a YOLOv8 nano model (`yolov8n.pt`) from Ultralytics to detect objects (e.g., frisbees) in a video.

### Usage

Update the path to your video:

```python
cap = cv2.VideoCapture("Footage/output.mp4")
model = YOLO("yolov8n.pt")
```

### Controls

* Press `q` to exit the detection window

---

## Object Tracking

### KCF Tracker

**Script:** `kcf_tracker.py`

Uses the KCF (Kernelized Correlation Filters) algorithm for real-time object tracking.

### CSRT Tracker

**Script:** `csrt_tracker.py`

Uses the CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability) algorithm, offering higher accuracy at the cost of speed.

### Common Instructions

Both tracker scripts will prompt you to manually select the frisbee using a mouse-driven ROI selection.

### Controls

* Use the mouse to select the region to track
* Press `q` to quit tracking

---

## Recommendations

* Use `extract_frames.py` to collect training images for object detection.
* Train a YOLO model with labeled frisbee and player data using tools like Roboflow.
* Use KCF for real-time applications and CSRT when accuracy is more important.

---

## Sample Applications

* **Frisbee Detection:** Visualize bounding boxes on the flying disc in match footage.
* **Player & Frisbee Tracking:** Follow player/frisbee movements across frames.
* **Preprocessing Analysis:** Compare raw and processed imagery for analysis pipelines.

---

## License

This project is intended for academic and educational purposes only.

---

