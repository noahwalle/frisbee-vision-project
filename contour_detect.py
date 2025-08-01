import cv2
import numpy as np

# |--------- Other Video Options in Footage Folder -------------|
cap = cv2.VideoCapture("Footage/output.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

# |--------- HSV Colormap for better contour detection -------------|
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color = np.array([190, 190, 190])
    upper_color = np.array([230, 230, 230])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 10:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (0, 255, 0), 3)

# |--------- Display frame -------------|
    cv2.imshow("Frisbee Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()