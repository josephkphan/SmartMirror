from Tkinter import *


# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page

class ReturnButton(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.returnButton = Label(self, text="Return", font=('Helvetica', 28), fg="white", bg="black")
        self.returnButton.pack(side=LEFT, anchor=N, padx=25, pady=25)  # todo padding isnt working, fix it

    def change_color_to_yellow(self):
        self.returnButton.config(foreground="yellow")

    def change_color_to_white(self):
        self.returnButton.config(foreground="white")