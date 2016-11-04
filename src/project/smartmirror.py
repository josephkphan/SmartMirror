from hardwareManagers.camera import *
from hardwareManagers.powerswitch import *
from hardwareManagers.ultrasoundhandler import *
from uiManagers.uihandler import *

bool_light = False
ultra_sound_handler = UltraSoundHandler()
power_switch = PowerSwitch()
camera = Camera(bool_light)
ui_manager = UIManager()

counter = 0
while True:
    counter += 1
    camera.update_values()
    cursor_location = camera.get_cursor()
    ui_manager.update(cursor_location)
    # print str(counter)
    # if counter >100:
    #     ui_manager.end_news()
    #     counter = -500

    k = cv2.waitKey(10)
    if k == 27:  # Esc key breaks out of program
        break  # break out of program
