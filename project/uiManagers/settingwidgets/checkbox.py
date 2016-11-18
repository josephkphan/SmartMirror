from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var
from enum import Enum


class CheckBoxMode(Enum):
    not_checked_off = 1  # not selected
    not_checked_on = 2
    checked_off = 3
    checked_on = 4


class CheckBox(Frame):
    def __init__(self, parent, label="", key=""):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style

        Frame.__init__(self, parent, bg=background_color)
        self.color_label = selected_off
        self.key = key
        # todo ADD AN IF TO INIT TO AN OFF BASED ON SAVED PREFERENCES
        if var.preferences[key]:
            self.check_box_mode = CheckBoxMode.checked_off
        else:
            self.check_box_mode = CheckBoxMode.not_checked_off

        image = Image.open("assets/empty_check_box.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.empty_check_box_off = ImageTk.PhotoImage(image)

        image = Image.open("assets/empty_check_box_on.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.empty_check_box_on = ImageTk.PhotoImage(image)

        image = Image.open("assets/check_box.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.filled_check_box_off = ImageTk.PhotoImage(image)

        image = Image.open("assets/check_box_on.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.filled_check_box_on = ImageTk.PhotoImage(image)

        self.label = Label(self, text=label, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.label.pack(side=LEFT, anchor=N)

        if self.check_box_mode == CheckBoxMode.checked_off:
            self.icon_label = Label(self, bg=background_color, image=self.filled_check_box_off)
            self.icon_label.image = self.filled_check_box_off
        else:
            self.icon_label = Label(self, bg=background_color, image=self.empty_check_box_off)
            self.icon_label.image = self.empty_check_box_off
        self.icon_label.pack(side=LEFT, anchor=N, padx=20)

    def change_color_all(self, mode):
        self.change_color_label(mode)
        self.change_color_check_box(mode)

    def change_color_label(self, mode):
        if self.color_label != mode:
            self.color_label = mode
            self.label.config(foreground=self.color_label)

    def change_color_check_box(self, mode):
        if mode == var.selected_on:
            # If its On and the box's aren't selected, then select it
            if self.check_box_mode == CheckBoxMode.not_checked_off:
                self.check_box_mode = CheckBoxMode.not_checked_on
                self.icon_label.config(image=self.empty_check_box_on)
                self.icon_label.image = self.empty_check_box_on
            elif self.check_box_mode == CheckBoxMode.checked_off:
                self.check_box_mode = CheckBoxMode.checked_on
                self.icon_label.config(image=self.filled_check_box_on)
                self.icon_label.image = self.filled_check_box_on
        else:
            # If the mode is off, that means the checkbox should be white
            # only change if its currently on
            if self.check_box_mode == CheckBoxMode.not_checked_on:
                self.check_box_mode = CheckBoxMode.not_checked_off
                self.icon_label.config(image=self.empty_check_box_off)
                self.icon_label.image = self.empty_check_box_off

            elif self.check_box_mode == CheckBoxMode.checked_on:
                self.check_box_mode = CheckBoxMode.checked_off
                self.icon_label.config(image=self.filled_check_box_off)
                self.icon_label.image = self.filled_check_box_off

    # Should only be used when the current area is selected, so the color should be yellow
    def update_check_box_image(self):
        if var.preferences[self.key]:
            if (self.check_box_mode != CheckBoxMode.checked_off) or (self.check_box_mode != CheckBoxMode.checked_on):
                self.check_box_mode = CheckBoxMode.checked_off
                self.icon_label.config(image=self.filled_check_box_on)
                self.icon_label.image = self.filled_check_box_on
        else:
            if (self.check_box_mode != CheckBoxMode.not_checked_off) or (self.check_box_mode != CheckBoxMode.not_checked_on):
                self.check_box_mode = CheckBoxMode.not_checked_off
                self.icon_label.config(image=self.empty_check_box_on)
                self.icon_label.image = self.empty_check_box_on
