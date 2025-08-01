import cv2

# |--------- Path to footage folder goes here -------------|
cap = cv2.VideoCapture("Footage/output.mp4")

ret, frame = cap.read(0)
if not ret:
    print("Error loading video")
    cap.release()
    exit()

# |--------- Draw bounding box with mouse -------------|
bbox = cv2.selectROI("Select Frisbee", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Frisbee")

tracker = cv2.TrackerKCF_create()
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
        cv2.putText(frame, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    else:
        cv2.putText(frame, "Lost", (50,80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

# |--------- Monitor rescaling -------------|
    target_width = 1440
    target_height = 960

    h, w = frame.shape[:2]
    scaling_factor = min(target_width / w, target_height / h)
    frame_resized = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor)

    cv2.imshow("Multi-Object CSRT Tracker", frame_resized)

# |--------- q to quit -------------|
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()