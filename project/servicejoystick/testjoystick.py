import sys
import time
from servicejoystick.joystick.joystickhandler import *

# sys.path.append("../")
# from project.uimanagers.uihandler import *

#ui_manager = UIManager()
joystick_manager = JoystickHandler()

joystick_state = 'home'

while True:
    time.sleep(.5)
    # Get the direction
    joystick_state = joystick_manager.get_direction()

    start = time.time()

    # Hold down enter on Joystick to turn off
    while joystick_state == 'pressed':

        # Did not hold for 5 seconds
        if joystick_state != 'pressed':
            joystick_state = 'pressed'
            break

        # Update the direction of the joystick
        joystick_state = joystick_manager.get_direction()
        print joystick_state
        end = time.time()

        # Wait for 5 seconds to toggle the mirror
        if (end-start) >= 5:
            joystick_state = 'toggled'
            break


    # Manual Mode
    # ui_manager.update_all_joystick(joystick_state)
    # ui_manager.update_all_manually()
