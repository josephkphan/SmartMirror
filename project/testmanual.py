import sys, time
sys.path.append("../")
from project.uimanagers.uihandler import *

class Controller():
    def __init__(self):
        self.ui_manager = UIManager(self)
        self.is_mirror_on = True
        while True:
            try:
                while self.is_mirror_on:
                    # Manual Mode
                    self.ui_manager.update_all_manually()
            except:
                print 'Powered off'
            self.ui_manager.tk.destroy()
            self.ui_manager = UIManager(self)
            self.is_mirror_on = True


controller = Controller()
