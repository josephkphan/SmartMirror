import cv2
import numpy as np
import math

# Class Description:


class Camera:
    # ------------------------------------------------ INIT ------------------------------------------------#

    # Description:
    def __init__(self, bool_light):
        self.cap = cv2.VideoCapture(0)  # access camera feed
        self.bool_light = bool_light
        self.cursor = (1000, 1000)
        self.ret, self.img = self.cap.read()  # gets frame of camera feed
        self.img = cv2.flip(self.img, 1)
        cv2.rectangle(self.img, (300, 300), (100, 100), (0, 255, 0), 0)  # draw the rectangle to show detection
        self.crop_img = self.img[100:300, 100:300]  # crop frame range
        self.grey = cv2.cvtColor(self.crop_img, cv2.COLOR_BGR2GRAY)  # turns image into greyscale
        self.value = (35, 35)  # value for blur
        self.blurred = cv2.GaussianBlur(self.grey, self.value, 6)  # removes noise from image
        if self.bool_light:  # Means background is white
            _, self.thresh1 = cv2.threshold(self.blurred, 180, 255,  # Inverse Threshold
                                            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        else:
            _, self.thresh1 = cv2.threshold(self.blurred, 180, 255,  # Regular Threshold
                                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        (version, _, _) = cv2.__version__.split('.')  # parse to get opencv version

        cv2.imshow('Threshold', self.thresh1)  # display black and white threshold to screen

        if version is '3':
            self.image, self.contours, self.hierarchy = cv2.findContours(self.thresh1.copy(),
                                                                         cv2.RETR_TREE,
                                                                         cv2.CHAIN_APPROX_NONE)  # detect contours
        elif version is '2':
            self.contours, self.hierarchy = cv2.findContours(self.thresh1.copy(), cv2.RETR_TREE,
                                                             cv2.CHAIN_APPROX_NONE)  # count contours

        self.cnt = max(self.contours, key=lambda x: cv2.contourArea(x))

        self.x, self.y, self.w, self.h = cv2.boundingRect(self.cnt)  # coordinates of detected object

        # draw rectangle around detected object
        cv2.rectangle(self.crop_img, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 0, 255), 0)
        self.hull = cv2.convexHull(self.cnt)
        self.drawing = np.zeros(self.crop_img.shape, np.uint8)
        cv2.drawContours(self.drawing, [self.cnt], 0, (0, 255, 0), 0)  # draws contours
        cv2.drawContours(self.drawing, [self.hull], 0, (241, 202, 161), 0)  # draws contours
        self.hull = cv2.convexHull(self.cnt, returnPoints=False)
        self.defects = cv2.convexityDefects(self.cnt, self.hull)
        self.count_defects = 0
        cv2.drawContours(self.thresh1, self.contours, -1, (0, 255, 0), 3)

        #cv2.circle(self.img, (self.x + 100 + self.w / 2, 100 + self.y), 5, (0, 255, 0), -1)  # draw circle for cursor

        for i in range(self.defects.shape[0]):  # do the math to find number of fingers
            s, e, f, d = self.defects[i, 0]
            self.start = tuple(self.cnt[s][0])
            self.end = tuple(self.cnt[e][0])
            self.far = tuple(self.cnt[f][0])
            a = math.sqrt((self.end[0] - self.start[0]) ** 2 + (self.end[1] - self.start[1]) ** 2)
            b = math.sqrt((self.far[0] - self.start[0]) ** 2 + (self.far[1] - self.start[1]) ** 2)
            c = math.sqrt((self.end[0] - self.far[0]) ** 2 + (self.end[1] - self.far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
            if angle <= 110:
                self.count_defects += 1
                cv2.circle(self.crop_img, self.far, 1, [0, 255, 0], -1)
            cv2.line(self.crop_img, self.start, self.end, [255, 0, 0], 2)
            cv2.circle(self.img, (self.end[0] + 100, self.end[1] + 100), 5, (0, 255, 0), -1)

            if self.cursor[1] > self.start[1]:
                self.cursor = self.start
            if self.cursor[1] > self.end[1]:
                self.cursor = self.end

        cv2.circle(self.img, (self.cursor[0] + 100, self.cursor[1] + 100), 5, (255, 0, 0), -1)
        if self.count_defects == 1:
            cv2.putText(self.img, "1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 1 finger action
        elif self.count_defects == 2:
            str = "2"
            cv2.putText(self.img, str, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)  # 2 finger action
        elif self.count_defects == 3:
            cv2.putText(self.img, "3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 3 finger action
        elif self.count_defects == 4:
            cv2.putText(self.img, "4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 4 finger action
        else:
            cv2.putText(self.img, "5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 5 finger action)
        cv2.imshow('Gesture', self.img)  # full frame with excess camera feed
        self.all_img = np.hstack((self.drawing, self.crop_img))
        #cv2.circle(self.all_img, (self.x + 0 + self.w / 2, self.y), 5, (0, 255, 0), -1)
        cv2.imshow('Contours', self.all_img)  # contours and frame feed - side by side

    # ------------------------------------------------ UPDATE ------------------------------------------------#

    # Description:
    def update_values(self):
        self.cursor = (1000, 1000)
        self.ret, self.img = self.cap.read()                            # gets frame of camera feed
        self.img = cv2.flip(self.img, 1)
        cv2.rectangle(self.img, (300, 300), (100, 100), (0, 255, 0), 0)  # draw the rectangle to show detection
        self.crop_img = self.img[100:300, 100:300]                      # crop frame range
        self.grey = cv2.cvtColor(self.crop_img, cv2.COLOR_BGR2GRAY)     # turns image into greyscale
        self.value = (35, 35)                                           # value for blur
        self.blurred = cv2.GaussianBlur(self.grey, self.value, 6)       # removes noise from image
        if self.bool_light:                                                   # Means background is white
            _, self.thresh1 = cv2.threshold(self.blurred, 180, 255,     # Inverse Threshold
                                       cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        else:
            _, self.thresh1 = cv2.threshold(self.blurred, 180, 255,     # Regular Threshold
                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        (version, _, _) = cv2.__version__.split('.')                    # parse to get opencv version

        cv2.imshow('Threshold', self.thresh1)  # display black and white threshold to screen

        if version is '3':
            self.image, self.contours, self.hierarchy = cv2.findContours(self.thresh1.copy(),
                cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)                   # detect contours
        elif version is '2':
            self.contours, self.hierarchy = cv2.findContours(self.thresh1.copy(), cv2.RETR_TREE,
                cv2.CHAIN_APPROX_NONE)                                  # count contours

        self.cnt = max(self.contours, key=lambda x: cv2.contourArea(x))

        self.x, self.y, self.w, self.h = cv2.boundingRect(self.cnt)     # coordinates of detected object

        # draw rectangle around detected object
        cv2.rectangle(self.crop_img, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 0, 255), 0)
        self.hull = cv2.convexHull(self.cnt)
        self.drawing = np.zeros(self.crop_img.shape, np.uint8)
        cv2.drawContours(self.drawing, [self.cnt], 0, (0, 255, 0), 0)   # draws contours
        cv2.drawContours(self.drawing, [self.hull], 0, (241, 202, 161), 0)  # draws contours
        self.hull = cv2.convexHull(self.cnt, returnPoints=False)
        self.defects = cv2.convexityDefects(self.cnt, self.hull)
        self.count_defects = 0
        cv2.drawContours(self.thresh1, self.contours, -1, (0, 255, 0), 3)

        #cv2.circle(self.img, (self.x + 100 + self.w / 2, 100 + self.y), 5, (0, 255, 0), -1)  # draw circle for cursor

        for i in range(self.defects.shape[0]):  # do the math to find number of fingers
            s, e, f, d = self.defects[i, 0]
            self.start = tuple(self.cnt[s][0])
            self.end = tuple(self.cnt[e][0])
            self.far = tuple(self.cnt[f][0])
            a = math.sqrt((self.end[0] - self.start[0]) ** 2 + (self.end[1] - self.start[1]) ** 2)
            b = math.sqrt((self.far[0] - self.start[0]) ** 2 + (self.far[1] - self.start[1]) ** 2)
            c = math.sqrt((self.end[0] - self.far[0]) ** 2 + (self.end[1] - self.far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
            if angle <= 110:
                self.count_defects += 1
                cv2.circle(self.crop_img, self.far, 1, [0, 255, 0], -1)
            cv2.line(self.crop_img, self.start, self.end, [255, 0, 0], 2)
            cv2.circle(self.img, (self.end[0] + 100, self.end[1] + 100), 5, (0, 255, 0), -1)
            if self.cursor[1] > self.start[1]:
                self.cursor = self.start
            if self.cursor[1] > self.end[1]:
                self.cursor = self.end

        cv2.circle(self.img, (self.cursor[0] + 100, self.cursor[1] + 100), 5, (255, 0, 0), -1)
        if self.count_defects == 1:
            cv2.putText(self.img, "1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 1 finger action
        elif self.count_defects == 2:
            str = "2"
            cv2.putText(self.img, str, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)  # 2 finger action
        elif self.count_defects == 3:
            cv2.putText(self.img, "3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 3 finger action
        elif self.count_defects == 4:
            cv2.putText(self.img, "4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 4 finger action
        else:
            cv2.putText(self.img, "5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)  # 5 finger action)
        cv2.imshow('Gesture', self.img)                                 # full frame with excess camera feed
        self.all_img = np.hstack((self.drawing, self.crop_img))
        #cv2.circle(self.all_img, (self.x + 0 + self.w / 2, self.y), 5, (0, 255, 0), -1)
        cv2.circle(self.all_img, (self.cursor[0] , self.cursor[1]), 5, (0, 255, 0), -1)
        cv2.imshow('Contours', self.all_img)                            # contours and frame feed - side by side

    # ------------------------------------------------ DISPLAY ------------------------------------------------#

    # Description:
    def update_display(self):
        cv2.drawContours(self.drawing, [self.cnt], 0, (0, 255, 0), 0)  # draws contours
        cv2.drawContours(self.drawing, [self.hull], 0, (241, 202, 161), 0)  # draws contours
        cv2.rectangle(self.img, (300, 300), (100, 100), (0, 255, 0), 0)  # draw the rectangle to show detection
        cv2.imshow('Threshold', self.thresh1)  # display black and white threshold to screen
        cv2.imshow('Gesture', self.img)
        cv2.imshow('Contours', self.all_img)
        for i in range(self.defects.shape[0]):  # do the math to find number of fingers
            cv2.line(self.crop_img, self.start, self.end, [255, 0, 0], 2)
            cv2.circle(self.img, (self.end[0] + 100, self.end[1] + 100), 5, (0, 255, 0), -1)
        cv2.circle(self.img, (self.cursor[0] + 100, self.cursor[1] + 100), 5, (255, 0, 0), -1)

    # ------------------------------------------------ GETTERS ------------------------------------------------#

    # Description:
    def get_number_defects(self):
        return self.count_defects

    # Description:
    def get_cursor(self):
        return self.cursor

    # ------------------------------------------------ TURN ON / OFF ------------------------------------------------#

    # Description:
    def turn_off(self):
        if self.cap.isOpened():
            self.cap.release

    # Description:
    def turn_on(self):
        if self.cap.isOpened()!= True:
            self.cap = cv2.VideoCapture(0)
