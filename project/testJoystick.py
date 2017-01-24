import sys
from hardwareManagers.joystick.joystickhandler import *

sys.path.append("../")
from project.uiManagers.uihandler import *

ui_manager = UIManager()
joystick_manager = JoystickHandler()

joystick_state = 'home'

while True:

    # Get the direction
    joystick_state = joystick_manager.get_direction()

    counter = 0

    # Hold down enter on Joystick to turn off
    while joystick_state == 'pressed':
        counter += 1
        if counter == 50:
            joystick_state = 'toggled'


    # Manual Mode
    ui_manager.update_all_joystick(joystick_state)
    ui_manager.update_all_manually()
