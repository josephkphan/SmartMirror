from Tkinter import *


# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page

class ReturnButton(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        # initialize the return label
        self.return_button = Label(self, text="Return", font=('Helvetica', 28), fg="white", bg="black")
        self.return_button.pack(side=LEFT, anchor=N)

    def change_color_to_yellow(self):
        self.return_button.config(foreground="yellow")

    def change_color_to_white(self):
        self.return_button.config(foreground="white")