from Tkinter import *
# from src.project.uiManagers.generalwidgets.lastupdated import *
import time
from Tkinter import *
from src.project.resources.var import *
import time
import math
# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page


class LastUpdatedLabel(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        self.update()


class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        # initialize time label
        self.time1 = ''
        self.timeLbl = Label(self, font=('Helvetica', 48), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=('Helvetica', 18), fg="white", bg="black")
        self.dayOWLbl.pack(side=TOP, anchor=E)
        # initialize date label
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=('Helvetica', 18), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E)
        self.last_update = Label(self, text="", font=('Helvetica', 12), fg="white", bg="black")
        self.last_update.pack(side=TOP, anchor=E)

        self.tick()

    def tick(self):
        time2 = time.strftime('%I:%M')
        day_of_week2 = time.strftime('%A')
        date2 = time.strftime("%b %d, %Y")
        # if time string has changed, update it
        if time2 != self.time1:
            self.time1 = time2
            self.timeLbl.config(text=time2)
        if day_of_week2 != self.day_of_week1:
            self.day_of_week1 = day_of_week2
            self.dayOWLbl.config(text=day_of_week2)
        if date2 != self.date1:
            self.date1 = date2
            self.dateLbl.config(text=date2)

        last_update_time = math.floor(time.time() - saved_data['last_updated'])/60
        if int(last_update_time) == 0:
            self.last_update.config(text="Just Updated")
        else:
            self.last_update.config(text="Updated " + str(int(last_update_time)) + " min ago")
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.update()
        self.timeLbl.after(200, self.tick)

    def change_color_to_yellow(self):
        self.dateLbl.config(foreground="yellow")
        self.timeLbl.config(foreground="yellow")
        self.dayOWLbl.config(foreground="yellow")

    def change_color_to_white(self):
        self.dateLbl.config(foreground="white")
        self.timeLbl.config(foreground="white")
        self.dayOWLbl.config(foreground="white")

    def change_last_update_color_to_yellow(self):
        self.last_update.config(foreground="yellow")

    def change_last_update_color_to_white(self):
        self.last_update.config(foreground="white")

    def change_update_label_to_updating(self):
        self.last_update.config(text="Updating...")
