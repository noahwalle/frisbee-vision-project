import cv2
import numpy as np

# |--------- Other Video Options in Footage Folder -------------|
cap = cv2.VideoCapture("Footage/forehand_3.mp4")
ret, frame = cap.read(0)

if not ret:
    print("Error loading video")
    cap.release()
    exit()

# |--------- Prompts the user for a bounding box to track -------------|
bbox = cv2.selectROI("Select Frisbee", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Frisbee")

tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

# |--------- Tracking done on processed image -------------|
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), cv2.BORDER_DEFAULT)
    threshold, thresh = cv2.threshold(blur, 190, 230, cv2.THRESH_BINARY)

    success, bbox = tracker.update(thresh)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    else:
        cv2.putText(frame, "Lost", (50,80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

# |--------- Scaled input image to monitor -------------|
# |--------- Put your own monitor resolution or lower in here -------------|
    target_width = 1440
    target_height = 960

    h, w = frame.shape[:2]
    scaling_factor = min(target_width / w, target_height / h)
    frame_resized = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor)

    cv2.imshow("Multi-Object CSRT Tracker", frame_resized)

    key = cv2.waitKey(0) & 0xFF

# |--------- Won't continue without user input -------------|
    if key == ord("n"):
        continue

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()