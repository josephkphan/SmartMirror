# Libraries
import RPi.GPIO as GPIO
import time
import os


class UltraSoundHandler:
    def __init__(self):
        self.distance = 0
        # todo get code

        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # set GPIO Pins
        self.GPIO_TRIGGER = 18
        self.GPIO_ECHO = 24

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

        # initialize time
        self.stopTime, self.startTime, self.timeElapsed = None, None, None

        self.consecutiveHits = 0

    def get_distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        self.startTime = time.time()
        self.stopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            self.startTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            self.stopTime = time.time()

        # time difference between start and arrival
        self.timeElapsed = self.stopTime - self.startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (self.timeElapsed * 34300) / 2

        return distance

    def wait_to_start_up(self):

        while True:
            dist = self.get_distance()
            print ("Measured Distance = %.1f cm" % dist)
            if dist > 150:
                self.consecutiveHits = 0
            elif dist <= 150:
                self.consecutiveHits += 1
                if self.consecutiveHits >= 3:
                     print ("HELLO")
                     self.consecutiveHits = 0
                #     os.system("python test_image.py")
            time.sleep(.1)

    def get_last_distance(self):
        return self.distance
