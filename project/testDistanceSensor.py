import sys

sys.path.append("../..")
from project.hardwareManagers.camera import *
from project.hardwareManagers.powerswitch import *
from project.hardwareManagers.ultrasoundhandler import *
from project.uiManagers.uihandler import *
from project.resources import var

ultra_sound_handler = UltraSoundHandler()
power_switch = PowerSwitch()
camera = Camera(var.wall_light_color)
ui_manager = UIManager()
print var.other_data
if var.other_data['manual_mode']:
    camera.turn_off()   # todo add onto this . close windows?
while True:
    ultra_sound_handler.wait_to_start_up()