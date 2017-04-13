from project.resources.page import *


class KeyboardSetUp:
    def __init__(self, uiHandler):
        self.uiHandler = uiHandler
        self.uiHandler.tk.bind("<Tab>", self.toggle_fullscreen)
        self.uiHandler.tk.bind("<Escape>", self.end_fullscreen)
        self.uiHandler.tk.bind("<Control_R>", self.toggle_power)

        # ---------------------------------- Key Binding Functions ----------------------------------- #

    def toggle_fullscreen(self, event=None):
        self.uiHandler.camera_selection_mode = not self.uiHandler.camera_selection_mode  # Just toggling the boolean
        self.uiHandler.tk.attributes("-fullscreen", self.uiHandler.camera_selection_mode)
        return "break"

    def end_fullscreen(self, event=None):
        self.uiHandler.camera_selection_mode = False
        self.uiHandler.tk.attributes("-fullscreen", False)
        return "break"

    def toggle_power(self, event=None):
        if self.uiHandler.current_page != Page.blank:
            self.uiHandler.change_page(Page.blank)
        else:
            self.uiHandler.change_page(Page.main)
