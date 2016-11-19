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

    if var.other_data['manual_mode']:
        # Manual Mode
        ui_manager.update_all_manually()

    else:
        camera.turn_on()                         #todo IF THIS IS PASS BY REFERENCE. ADD CAMErA INTO
                                                 #todo UI MANAger, and only call camera.turn_on when its toggled
        # Camera Mode - relies on Camera
        camera.update_values()
        cursor_location = camera.get_cursor()
        ui_manager.update_all(cursor_location)

    k = cv2.waitKey(10)
    if k == 27:  # Esc key breaks out of program
        break  # break out of program
