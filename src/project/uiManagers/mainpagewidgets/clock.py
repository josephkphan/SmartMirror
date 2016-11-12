from Tkinter import *
from src.project.resources.var import *
import time
import math

# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page


# Will show the basic information such as current time, day of week, date, and last updated
class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')

        # initialize label colors
        self.time_color = selected_off
        self.day_color = selected_off
        self.date_color = selected_off
        self.last_update = selected_off

        # initialize time label
        self.time1 = ''
        self.time_label = Label(self, font=(font_style, 48), fg=selected_off, bg=background_color)
        self.time_label.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.day_label = Label(self, text=self.day_of_week1, font=(font_style, 18), fg=selected_off,
                               bg=background_color)
        self.day_label.pack(side=TOP, anchor=E)
        # initialize date label
        self.date1 = ''
        self.date_label = Label(self, text=self.date1, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.date_label.pack(side=TOP, anchor=E)
        # initialize last updated label
        self.last_update = ''
        self.last_update = Label(self, text=self.last_update, font=(font_style, 12), fg=selected_off,
                                 bg=background_color)
        self.last_update.pack(side=TOP, anchor=E)

        self.tick()

    # Will update the clock and last updated
    def tick(self):
        time2 = time.strftime('%I:%M')
        day_of_week2 = time.strftime('%A')
        date2 = time.strftime("%b %d, %Y")
        # if time string has changed, update it
        if time2 != self.time1:
            self.time1 = time2
            self.time_label.config(text=time2)
        #if the day of week changed, update it
        if day_of_week2 != self.day_of_week1:
            self.day_of_week1 = day_of_week2
            self.day_label.config(text=day_of_week2)

        if date2 != self.date1:
            self.date1 = date2
            self.date_label.config(text=date2)

        # if last update time changed, update it
        last_update_time = math.floor(time.time() - saved_data['last_updated'])/60
        if int(last_update_time) == 0:
            last_update = 'Just Updated'
            if self.last_update != last_update:
                self.last_update.config(text=last_update)
                self.last_update = last_update
        else:
            last_update = ("Updated " + str(int(last_update_time)) + " min ago")
            if self.last_update != last_update:
                self.last_update.config(text=last_update)

        # calls itself every 200 milliseconds to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.update()
        self.time_label.after(200, self.tick)

    def change_color_to_yellow(self):
        self.date_label.config(foreground="yellow")
        self.time_label.config(foreground="yellow")
        self.day_label.config(foreground="yellow")

    def change_color_to_white(self):
        self.date_label.config(foreground="white")
        self.time_label.config(foreground="white")
        self.day_label.config(foreground="white")

    def change_last_update_color_to_yellow(self):
        self.last_update.config(foreground="yellow")

    def change_last_update_color_to_white(self):
        self.last_update.config(foreground="white")

    def change_update_label_to_updating(self):
        self.last_update.config(text="Updating...")
