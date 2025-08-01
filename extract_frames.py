import os
import random
import cv2
import numpy as np
from tqdm import tqdm

# |--------- Use any empty directory -------------|
frames_dir = "Training"

def extract_random_frames(video_path, num_frames=750):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_indices = sorted(random.sample(range(total_frames), min(num_frames, total_frames)))

    for idx, frame_no in enumerate(tqdm(frame_indices, desc=f"Extracting frames from {os.path.basename(video_path)}")):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        if ret:
            frame_filename = os.path.join(frames_dir, f"{os.path.basename(video_path)}_frame{idx}.jpg")
            cv2.imwrite(frame_filename, frame)

    cap.release()

# |--------- Sample footage ~10s, use case is for something longer (~1-2hrs) -------------|
# |--------- Or adjust num_frames to what you want -------------|
extract_random_frames("Footage/backhand_1.mp4", num_frames=20)