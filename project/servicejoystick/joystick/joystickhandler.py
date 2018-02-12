ls
import PCF8591 as ADC
import time


class JoystickHandler:
    def __init__(self):
        ADC.setup(0x48) # Setup PCF8591
        self.state = None
#        global state

    # Get joystick's result
    def get_direction(self):
        state = ['home', 'up', 'down', 'left', 'right', 'pressed']
        i = 0
        print ADC.read(0)
        if ADC.read(0) <= 5:
            i = 1 # Up
        if ADC.read(0) >= 250:
            i = 2 # Down
        if ADC.read(1) >= 250:
            i = 3 # Left
        if ADC.read(1) <= 5:
            i = 4 # Right
        if ADC.read(2) == 0:
            i = 5 # Button pressed
        if ADC.read(0) - 125 < 15 and ADC.read(0) - 125 > -15 and ADC.read(1) - 125 < 15 and ADC.read(1) - 125 > -15 and ADC.read(2) == 255:
            i = 0
        return state[i]

    # # TODO: Remove infinite loop
    # def loop(self):
    #     status = ''
    #     while True:
    #         tmp = self.get_direction()
    #         if tmp != None and tmp != status:
    #             print tmp
    #             status = tmp

    # def destroy(self):
    #     pass
    #     if __name__ == '__main__': # Program start from here
    #        setup()
    #     try:
    #         loop()
    #     except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    #         destroy()