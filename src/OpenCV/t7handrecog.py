import numpy as np
import cv2

fist_cascade = cv2.CascadeClassifier('fist2.xml')
hand_cascade = cv2.CascadeClassifier('Hand2.xml')
hand_cascade1 = cv2.CascadeClassifier('haarCascade1.xml')
hand_cascade2 = cv2.CascadeClassifier('haarCascade2.xml')
hand_cascade3 = cv2.CascadeClassifier('haarCascade3.xml')
hand_cascade4 = cv2.CascadeClassifier('haarCascade4.xml')
hand_cascade5 = cv2.CascadeClassifier('haarCascade5.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fists = fist_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in fists:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    hands1 = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    hands2 = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    hands3 = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    hands4 = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    hands5 = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()