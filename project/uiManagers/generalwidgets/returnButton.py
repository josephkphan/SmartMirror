from Tkinter import *
from project.resources import var


# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page

class ReturnButton(Frame):
    def __init__(self, parent):
        # Gets constant variables from var file
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)

        # initialize color for the label
        self.color_return = selected_off

        # initialize the return label
        self.return_button = Label(self, text="Return", font=(font_style,  font_sizes['title']), fg=selected_off, bg=background_color)
        self.return_button.pack(side=LEFT, anchor=N)

    # Changes color based on specified mode
    def change_color_all(self, mode):
        if self.color_return != mode:  # will only act if the requested change is different
            self.color_return = mode
            self.return_button.config(foreground=self.color_return)

    def update_font_size(self):
        self.return_button.config(font=(var.font_style,  var.font_sizes['title']))
