import cv2
import numpy as np

# |--------- From Footage folder or put your own path -------------|
cap = cv2.VideoCapture('Footage/forehand_3.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

# |--------- Processing -------------|
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), cv2.BORDER_DEFAULT)
    threshold, thresh = cv2.threshold(blur, 190, 230, cv2.THRESH_BINARY)

# |--------- Monitor scaling, set to your preferred size -------------|
    target_width = 1440
    target_height = 960

    h, w = frame.shape[:2]
    scaling_factor = min(target_width / w, target_height / h)
    frame_resized = cv2.resize(frame, None, fx=scaling_factor/2, fy=scaling_factor/2)
    gray_resized = cv2.resize(gray, None, fx=scaling_factor/2, fy=scaling_factor/2)
    blur_resized = cv2.resize(blur, None, fx=scaling_factor/2, fy=scaling_factor/2)
    thresh_resized = cv2.resize(thresh, None, fx=scaling_factor/2, fy=scaling_factor/2)

# |--------- Indices may need adjusting for different monitor sizes -------------|
    blank = np.zeros((960,1440,3), dtype='uint8')
    blank[0:405,0:720] = frame_resized
    blank[0:405,720:1440,0] = gray_resized
    blank[0:405,720:1440,1] = gray_resized
    blank[0:405,720:1440,2] = gray_resized
    blank[405:810,0:720,0] = blur_resized
    blank[405:810,0:720,1] = blur_resized
    blank[405:810,0:720,2] = blur_resized
    blank[405:810,720:1440,0] = thresh_resized
    blank[405:810,720:1440,1] = thresh_resized
    blank[405:810,720:1440,2] = thresh_resized
    cv2.imshow('Footage', blank)

    key = cv2.waitKey(0) & 0xFF

# |--------- Hold down n key for continuous play, q to quit -------------|
    if key == ord("n"):
        continue

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()