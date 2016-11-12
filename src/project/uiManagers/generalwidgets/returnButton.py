from Tkinter import *
from src.project.resources.var import *


# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page

class ReturnButton(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg=background_color)
        self.color_return = selected_off
        # initialize the return label
        self.return_button = Label(self, text="Return", font=(font_style, 28), fg=selected_off, bg=background_color)
        self.return_button.pack(side=LEFT, anchor=N)

    def change_color_all(self,mode):
        if self.color_return != mode:
            self.color_return = mode
            self.return_button.config(foreground=self.color_return)
