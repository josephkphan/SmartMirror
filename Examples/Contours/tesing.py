import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #hit q to quit video capture
        break

cap.release()       #releases camera - sort of like fclose
cv2.destroyAllWindows()