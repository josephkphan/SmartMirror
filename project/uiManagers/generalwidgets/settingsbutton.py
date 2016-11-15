from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var


class SettingsButton(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, bg=background_color)
        self.settings_selected = selected_off

        image = Image.open("assets/settings.png")  # todo DOesnt WOrk! FIX THIS
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.photo_not_selected = ImageTk.PhotoImage(image)

        image = Image.open("assets/settings_on.png")  # todo DOesnt WOrk! FIX THIS
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.photo_selected = ImageTk.PhotoImage(image)

        self.icon_label = Label(self, bg=background_color, image=self.photo_not_selected)
        self.icon_label.image = self.photo_not_selected
        self.icon_label.pack(side=LEFT, anchor=N)

        self.event_name = "Settings"
        self.event_name_label = Label(self, text=self.event_name, font=(font_style, 24), fg=selected_off,
                                      bg=background_color)
        self.event_name_label.pack(side=LEFT, anchor=CENTER)

    def change_color_setting(self, mode):
        if self.settings_selected != mode:
            self.settings_selected = mode
            if self.settings_selected == var.selected_on:
                self.icon_label.config(image=self.photo_selected)
                self.icon_label.image = self.photo_selected
            else:
                self.icon_label.config(image=self.photo_not_selected)
                self.icon_label.image = self.photo_not_selected
            self.event_name_label.config(foreground=self.settings_selected)


