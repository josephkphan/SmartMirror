from Tkinter import *
from PIL import Image, ImageTk
from resources import var, imagecolor, zone
import time, math


class UpdateNow(Frame):
    def __init__(self,parent, tkinter_update):
        # keep an instance of the constant variables in var file
        # (just so you don't need to continually say var._____)
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self,parent, bg=background_color)
        self.tkinter_update = tkinter_update

        # to keep track of current color
        self.color_update_now = selected_off

        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP, anchor=W)

        self.container2 = Frame(self, bg=background_color)
        self.container2.pack(side=TOP, anchor=W, padx=50)

        self.update_status_text = "Update Status: "
        last_update_time = math.floor(time.time() - var.last_updated) / 60
        self.last_update_text = ("Updated " + str(int(last_update_time)) + " min ago")
        self.update_now_text = "Update Now "

        self.update_status_label = Label(self.container, text=self.update_status_text, font=(font_style, font_sizes['text']),
                                         fg=selected_off, bg=background_color)
        self.update_status_label.pack(side=LEFT, anchor=W)
        self.last_update_label = Label(self.container, text=self.last_update_text, font=(font_style, font_sizes['text']),
                                         fg=selected_off, bg=background_color)
        self.last_update_label.pack(side=LEFT, anchor=W)

        self.image = Image.open("assets/reload.png")
        self.icon_photo, self.icon_photo_selected = None, None

        # Packs in the icon
        self.icon_label = Label(self.container2, bg=background_color)
        self.create_photo()

        self.update_now_label = Label(self.container2, text=self.update_now_text, font=(font_style, font_sizes['text']),
                                         fg=selected_off, bg=background_color)
        self.update_now_label.pack(side=LEFT, anchor=W)
        self.icon_label.pack(side=LEFT, anchor=W)
        self.check_last_update()

    def check_last_update(self):
        # if last update time changed, update it
        last_update_time = math.floor(time.time() - var.last_updated) / 60
        if int(last_update_time) == 0:
            last_update = 'Just Updated'  # todo CHECK after update it doesnt show just updated
            if self.last_update_text != last_update:
                self.last_update_text = last_update
                self.last_update_label.config(text=self.last_update_text)
        else:
            last_update = ("Updated " + str(int(last_update_time)) + " min ago")
            if self.last_update_text != last_update:
                self.last_update_text = last_update
                self.last_update_label.config(text=self.last_update_text)

        # calls itself every 200 milliseconds to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.update()
        self.last_update_label.after(1000, self.check_last_update) #todo is 200 too much???
            #todo THIS IS STILL CALLED EVEN DURING OTHER PAGES!!! -since instiated in begininng

    # Changes color based on passed in mode
    def change_color_update_now(self, mode):
        if self.color_update_now != mode:
            self.color_update_now = mode  # update color boolean
            # Updating the image
            if self.color_update_now == var.selected_on:
                # changing image to on
                self.icon_label.config(image=self.icon_photo_selected)
            else:
                self.icon_label.config(image=self.icon_photo)
            # updates the text label
            self.update_now_label.config(foreground=self.color_update_now)

            #todo create a method that will change text to "just updated"

    def create_photo(self):
        self.image = self.image.resize(var.font_sizes['small_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        self.icon_photo = ImageTk.PhotoImage(self.image)
        self.icon_photo_selected = ImageTk.PhotoImage(imagecolor.tint(self.image, var.selected_on))
        self.icon_label.config(image=self.icon_photo)

    def update_now(self):
        if self.icon_photo is not None:
            self.create_photo()
        self.update_font_size()

    def update_font_size(self):
        self.create_photo()
        self.update_status_label.config(font=(var.font_style, var.font_sizes['text']))
        self.last_update_label.config(font=(var.font_style, var.font_sizes['text']))
        self.update_now_label.config(font=(var.font_style, var.font_sizes['text']))

    def update_smart_mirror(self, current_zone):
        if current_zone == zone.SettingsPage.update_now:
            self.last_update_text = 'Updating...'
            self.last_update_label.config(text=self.last_update_text)       # Todo THIS DOESNT WORK -- FIX IT
            self.tkinter_update()
