# import sys
#
# sys.path.append("../..")
# from project.hardwaremanagers.camera import *
# from project.hardwaremanagers.powerswitch import *
from hardwaremanagers.ultrasoundhandler import *
# from project.uimanagers.uihandler import *
# from project.resources import var

ultra_sound_handler = UltraSoundHandler()

while True:
    ultra_sound_handler.wait_to_start_up()

# Thomas's Test Comment