from camera import *
from powerswitch import *
from ultrasoundhandler import *
import cv2
import numpy as np
import math

bool_light = True
ultra_sound_handler = UltraSoundHandler()
power_switch = PowerSwitch()
camera = Camera(bool_light)

while True:
    camera.update_values()
    k = cv2.waitKey(10)
    if k == 27: # Esc key breaks out of program
        break # break out of program