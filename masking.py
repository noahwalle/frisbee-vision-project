import cv2
import numpy as np

# |--------- Path to footage folder goes here -------------|
cap = cv2.VideoCapture('Footage/forehand_2.mp4')

# |--------- Must select a valid frame so change target_frame to low numbers -------------|
target_frame = 20
cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
ret, frame = cap.read()
if not ret:
    print(f"[ERROR] Couldn't read frame {target_frame}")
    cap.release()
    exit()

h, w = frame.shape[:2]
scale = min(1440 / w, 960 / h)
frame_resized = cv2.resize(frame, None, fx=scale/2, fy=scale/2)

# |--------- Processing -------------|
gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 125, 175)
dilated = cv2.dilate(canny, (7,7), iterations=3)
eroded = cv2.erode(dilated, (7,7), iterations=3)

blank = np.zeros(frame.shape[:2], dtype='uint8')
blank_resized = cv2.resize(blank, None, fx=scale/2, fy=scale/2)

# |------ Masking runs into its own problems because sometimes the frisbee ------|
# |------ enters the region that we are masking ------|
mask = cv2.rectangle(blank.copy(), (0,0), (frame.shape[1], 400), 255, -1)
mask = cv2.bitwise_not(mask)
mask_resized = cv2.resize(mask, None, fx=scale/2, fy=scale/2)

masked = cv2.bitwise_and(frame,frame,mask=mask)
masked_resized = cv2.resize(masked, None, fx=scale/2, fy=scale/2)

# |--------- Will produce a lot of popups -------------|
cv2.imshow('Frame', frame_resized)
cv2.imshow('Blank', blank_resized)
cv2.imshow('Mask', mask_resized)
cv2.imshow('Masked', masked_resized)

cv2.imshow('Blur', blur)
cv2.imshow('Canny', canny)
cv2.imshow('Dilated', dilated)
cv2.imshow('Eroded', eroded)

# |--------- Any key to quit -------------|
cv2.waitKey(0)