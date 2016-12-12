import sys

sys.path.append("../..")
# from project.hardwareManagers.camera import *
# from project.hardwareManagers.powerswitch import *
from project.hardwareManagers.ultrasoundhandler import *
# from project.uiManagers.uihandler import *
# from project.resources import var

ultra_sound_handler = UltraSoundHandler()

while True:
    ultra_sound_handler.wait_to_start_up()