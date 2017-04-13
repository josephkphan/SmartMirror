import sys

sys.path.append("../")
from project.uimanagers.uihandler import *

ui_manager = UIManager()
while True:

    # Manual Mode
    ui_manager.update_all_manually()
