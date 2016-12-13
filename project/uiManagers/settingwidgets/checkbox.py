from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, imagecolor
from enum import Enum


# Enum for the different Check Box image modes
class CheckBoxMode(Enum):
    not_checked_off = 1  # not selected
    not_checked_on = 2
    checked_off = 3
    checked_on = 4


# Contains a label given and adds on a check box
class CheckBox(Frame):
    def __init__(self, parent, label="", key=""):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style

        Frame.__init__(self, parent, bg=background_color)
        self.color_label = selected_off
        self.key = key

        # Gets Saved Preferences from preferences file
        if var.preferences[key]:
            self.check_box_mode = CheckBoxMode.checked_off
        else:
            self.check_box_mode = CheckBoxMode.not_checked_off

        # --- Loads the 4 Possible Check Box Images --- #

        # Checked off and white
        image = Image.open("assets/empty_check_box.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.empty_check_box_off = ImageTk.PhotoImage(image)

        # Checked off and yellow
        image = imagecolor.tint(image,var.color_hex_codes[var.selected_on])
        self.empty_check_box_on = ImageTk.PhotoImage(image)

        # Not Checked off and white
        image = Image.open("assets/check_box.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.filled_check_box_off = ImageTk.PhotoImage(image)

        # Not Checked off and yellow
        image = imagecolor.tint(image, var.color_hex_codes[var.selected_on])
        self.filled_check_box_on = ImageTk.PhotoImage(image)

        # Initializes the Label
        self.label = Label(self, text=label, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.label.pack(side=LEFT, anchor=N)

        # Chooses the according image to preference file
        if self.check_box_mode == CheckBoxMode.checked_off:
            self.icon_label = Label(self, bg=background_color, image=self.filled_check_box_off)
            self.icon_label.image = self.filled_check_box_off
        else:
            self.icon_label = Label(self, bg=background_color, image=self.empty_check_box_off)
            self.icon_label.image = self.empty_check_box_off
        self.icon_label.pack(side=LEFT, anchor=N, padx=20)

    # ----------------------- Coloring ------------------------ #

    # Changes the color of both the label and the image to the specified mode
    def change_color_all(self, mode):
        self.change_color_label(mode)
        self.change_color_check_box(mode)

    # Only changes the label color
    def change_color_label(self, mode):
        if self.color_label != mode:
            self.color_label = mode
            self.label.config(foreground=self.color_label)

    # Only changes the check box color
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

    # -------------------------- Updating Check Box Image -------------------------- #

    # Will be called when a user wants to change the preference. It will toggle the box image
    def update_check_box_image(self):
        if var.preferences[self.key]:
            if (self.check_box_mode != CheckBoxMode.checked_off) or (self.check_box_mode != CheckBoxMode.checked_on):
                self.check_box_mode = CheckBoxMode.checked_on
                self.icon_label.config(image=self.filled_check_box_on)
                self.icon_label.image = self.filled_check_box_on
                # Should only be used when the current area is selected, so the color will be yellow
        else:
            if (self.check_box_mode != CheckBoxMode.not_checked_off) or (
                        self.check_box_mode != CheckBoxMode.not_checked_on):
                self.check_box_mode = CheckBoxMode.not_checked_on
                self.icon_label.config(image=self.empty_check_box_on)
                self.icon_label.image = self.empty_check_box_on
