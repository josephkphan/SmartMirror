import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    corners = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(corners, 100, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #hit q to quit video capture
        break

cap.release()       #releases camera - sort of like fclose
cv2.destroyAllWindows()
