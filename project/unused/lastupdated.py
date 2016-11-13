from Tkinter import *
from project.resources.var import *
import time
# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page


class LastUpdatedLabel(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.last_update = Label(self, text="", font=('Helvetica', 12), fg="white", bg="black")
        self.last_update.pack(side=TOP, anchor=N, padx=25, pady=25)  # todo padding isnt working, fix it
        self.update()

    def change_color_to_yellow(self):
        self.last_update.config(foreground="yellow")

    def change_color_to_white(self):
        self.last_update.config(foreground="white")

    def update(self):
        last_update_time = time.time() - saved_data['last_updated']
        print last_update_time
        self.last_update.config(text=str(last_update_time))
        #self.last_update.after(100000, self.update())  # todo find out how long this is