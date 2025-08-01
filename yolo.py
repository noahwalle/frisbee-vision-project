from ultralytics import YOLO
import cv2

# |--------- Model and Footage -------------|
# |--------- Train own model with the dataset provided -------------|
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("Footage/output.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

# |--------- Draw detection boxes -------------|
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

# |--------- Display image, q to quit -------------|
    cv2.imshow("YOLO Frisbee Detection", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
