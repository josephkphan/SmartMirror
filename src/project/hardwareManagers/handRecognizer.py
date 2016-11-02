import cv2
import numpy as np
import math


cap = cv2.VideoCapture(0) # access camera feed
box_selected = 0;
box_hit_count = 0;

#fgbg = cv2.createBackgroundSubtractorMOG2() #for background reduction

while (cap.isOpened()): # main loop
    ret, img = cap.read() #gets frame of camera feed
    img = cv2.flip (img,1)
    img = img[0:500, 600:1300]
    #fgmask = fgbg.apply(img)
    #cv2.imshow('fgmask', fgmask)
    x_start = 300
    y_start = 100
    cv2.rectangle(img, (x_start+300, y_start+300), (x_start, y_start), (0, 255, 0), 0) # draw the full rectangle to show detection box
    cv2.rectangle(img, (x_start+100, y_start), (x_start+200, y_start+100), (0, 255, 0), 0) # draw the grid in the rectangle
    cv2.rectangle(img, (x_start, y_start+100), (x_start+100, y_start+200), (0, 255, 0), 0) # draw the grid in the rectangle
    cv2.rectangle(img, (x_start+200, y_start+100), (x_start+300, y_start+200), (0, 255, 0), 0) # draw the grid in the rectangle
    cv2.rectangle(img, (x_start+100, y_start+200), (x_start+200, y_start+300), (0, 255, 0), 0) # draw the grid in the rectangle
    crop_img = img[y_start:y_start+300, x_start:x_start+300] # crop frame range
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) # turns image into greyscale
    value = (35, 35) # value for blur
    blurred = cv2.GaussianBlur(grey, value, 6)  # removes noise from image

    #USED FOR LIGHT BACKGROUND
    _, thresh1 = cv2.threshold(blurred, 180, 255, # turns into black and white
                               cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # USED FOR DARK BACKGROUND
    #_,thresh1 = cv2.threshold(blurred, 180, 255,  # turns into black and white
    #                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    cv2.imshow('Thresholded', thresh1) # display black and white threshold to screen

    (version, _, _) = cv2.__version__.split('.') # parse to get opencv version

    if version is '3':
        image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
                                                      cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # detect contours
    elif version is '2':
        contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, \
                                               cv2.CHAIN_APPROX_NONE) #detect contours

    cnt = max(contours, key=lambda x: cv2.contourArea(x)) #count contours

    x, y, w, h = cv2.boundingRect(cnt) # coordinates of detected object
    cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0, 0, 255), 0) # draw rectangle around detected object
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape, np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0) # draws contours
    cv2.drawContours(drawing, [hull], 0, (241, 202, 161), 0) #draws contours
    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)


    cv2.circle(img, (x+100 + w/2, 100 + y ), 5, (0, 255, 0), -1) # draw circle for cursor

    cursor = (1000, 1000)

    for i in range(defects.shape[0]): # do the math to find number of fingers
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
        if angle <= 110:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0, 255, 0], -1)
        # dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_img, start, end, [255,0,0], 2)
        #cv2.circle(img, end, 5, (0, 255, 0), -1)
        #cv2.circle(img, start, 5, (0, 255, 0), -1)
        cv2.circle(img, (end[0] + x_start, end[1] + y_start), 5, (0, 255, 0), -1)
        #cv2.circle(img, (start[0] + 100, start[1] + 100), 5, (0, 255, 0), -1)
        # cv2.circle(crop_img,far,5,[0,0,255],-1)
        if cursor[1] > start[1]:
            cursor = start;
        if cursor[1] > end[1]:
            cursor = end;
    cv2.circle(img, (cursor[0] + x_start, cursor[1] + y_start), 5, (255, 0, 0), -1)
    cv2.putText(img, "x: " + str(cursor[0]) + " y: " + str(cursor[1]), (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 1 finger action

    # detect which box the cursor is in
    if cursor[0] > 2 and cursor[0] < 100 and cursor[1] > 2 and cursor[1] < 100: # box 1
        if box_selected == 1:
            box_hit_count += 1;
            cv2.putText(img, "hit count: " + str(box_hit_count), (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            if box_hit_count > 50:
                print "Selected 1"
                box_hit_count = 0
        cv2.putText(img, "Cursor in box 1", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        box_selected = 1
    elif cursor[0] > 100 and cursor[0] < 200 and cursor[1] > 2 and cursor[1] < 100:
        cv2.putText(img, "Cursor in box 2", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(img, "Outside", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    if count_defects == 1:
        cv2.putText(img, "2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2) # 1 finger action
    elif count_defects == 2:
        cv2.putText(img, "3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2) # 2 finger action
    elif count_defects == 3:
        cv2.putText(img, "4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2) # 3 finger action
    elif count_defects == 4:
        cv2.putText(img, "5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2) # 4 finger action
    else:
        cv2.putText(img, "1", (50, 50), \
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2) # 5 finger action
    # cv2.imshow('drawing', drawing)
    # cv2.imshow('end', crop_img)
    cv2.imshow('Gesture', img) # full frame with excess camera feed
    all_img = np.hstack((drawing, crop_img))
    cv2.circle(all_img, (x + 0 + w / 2, y), 5, (0, 255,0), -1)
    cv2.imshow('Contours', all_img) # contours and frame feed - side by side

    k = cv2.waitKey(10)
    if k == 27: # Esc key breaks out of program
        break # break out of program

def hit_counter(box_no):
    if box_selected == box_no:
        box_hit_count += 1;
        cv2.putText(img, "hit count: " + str(box_hit_count), (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        if box_hit_count > 50:
            print "Selected " + str(box_no)
            box_hit_count = 0
    cv2.putText(img, "Cursor in box 1", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    box_selected = 1