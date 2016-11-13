from Tkinter import *
from src.project.resources import var
import time
import math
# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page


# Will show the basic information such as current time, day of week, date, and last updated
class Clock(Frame):
    def __init__(self, parent):
        background_color = var.background_color
        selected_off = var.selected_off
        font_style = var.font_style

        Frame.__init__(self, parent, bg=background_color)

        # initialize label colors
        self.color_time = selected_off
        self.color_day = selected_off
        self.color_date = selected_off
        self.color_last_update = selected_off

        # initialize time label
        self.time = ''
        self.time_label = Label(self, text=self.time, font=(font_style, 48), fg=selected_off, bg=background_color)
        self.time_label.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day = ''
        self.day_label = Label(self, text=self.day, font=(font_style, 18), fg=selected_off,
                               bg=background_color)
        self.day_label.pack(side=TOP, anchor=E)
        # initialize date label
        self.date = ''
        self.date_label = Label(self, text=self.date, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.date_label.pack(side=TOP, anchor=E)
        # initialize last updated label
        self.last_update = ''
        self.last_update_label = Label(self, text=self.last_update, font=(font_style, 12), fg=selected_off,
                                       bg=background_color)
        self.last_update_label.pack(side=TOP, anchor=E)

        self.tick()

    # Will update the clock and last updated
    def tick(self):
        cur_time = time.strftime('%I:%M')
        day_of_week = time.strftime('%A')
        date = time.strftime("%b %d, %Y")
        # if time string has changed, update it
        if cur_time != self.time:
            self.time = cur_time
            self.time_label.config(text=cur_time)
        # if the day of week changed, update it
        if day_of_week != self.day:
            self.day = day_of_week
            self.day_label.config(text=day_of_week)

        if date != self.date:
            self.date = date
            self.date_label.config(text=date)

        # if last update time changed, update it
        last_update_time = math.floor(time.time() - var.saved_data['last_updated']) / 60
        if int(last_update_time) == 0:
            last_update = 'Just Updated'  # todo CHECK after update it doesnt show just updated
            if self.last_update != last_update:
                self.last_update = last_update
                self.last_update_label.config(text=self.last_update)
        else:
            last_update = ("Updated " + str(int(last_update_time)) + " min ago")
            if self.last_update != last_update:
                self.last_update = last_update
                self.last_update_label.config(text=self.last_update)

        # calls itself every 200 milliseconds to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.update()
        self.time_label.after(200, self.tick)

    # -------------------- Colorings -------------------------- #

    def change_color_all(self, mode):
        self.change_color_time(mode)
        self.change_color_date(mode)
        self.change_color_day(mode)
        self.change_color_update(mode)

    def change_color_time(self, mode):
        if self.color_time != mode:
            self.color_time = mode
            self.time_label.config(foreground=self.color_time)

    def change_color_date(self, mode):
        if self.color_date != mode:
            self.color_date = mode
            self.date_label.config(foreground=self.color_date)

    def change_color_day(self, mode):
        if self.color_day != mode:
            self.color_day = mode
            self.day_label.config(foreground=self.color_day)

    def change_color_update(self, mode):
        if self.color_last_update != mode:
            self.color_last_update = mode
            self.last_update_label.config(foreground=self.color_last_update)

    # ---------------------- Update Label ---------------------- #
    def change_update_label_to_updating(self):
        self.last_update = "Updating..."
        self.last_update_label.config(text=self.last_update)
