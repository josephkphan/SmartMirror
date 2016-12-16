from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, imagecolor
from enum import Enum


# Enum for the different Check Box image modes
class CheckBoxMode(Enum):
    unchecked = 1  # not selected
    unchecked_selected = 2
    checked = 3
    checked_selected = 4


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
            self.check_box_mode = CheckBoxMode.checked
        else:
            self.check_box_mode = CheckBoxMode.unchecked

        # --- Loads the 4 Possible Check Box Images --- #

        # Checked off and white
        image = Image.open("assets/empty_check_box.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.plain_empty_checked_box = image
        self.unchecked_photo = ImageTk.PhotoImage(image)

        # Checked off and yellow
        image = imagecolor.tint(image, var.selected_on)
        self.unchecked_photo_selected = ImageTk.PhotoImage(image)

        # Not Checked off and white
        image = Image.open("assets/check_box.png")
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.plain_checked_box = image
        self.checked_photo = ImageTk.PhotoImage(image)

        # Not Checked off and yellow
        image = imagecolor.tint(image, var.selected_on)
        self.checked_photo_selected = ImageTk.PhotoImage(image)

        # Initializes the Label
        self.text_label = Label(self, text=label, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.text_label.pack(side=LEFT, anchor=N)

        # Chooses the according image to preference file
        if self.check_box_mode == CheckBoxMode.checked:
            self.icon_label = Label(self, bg=background_color, image=self.checked_photo)
        else:
            self.icon_label = Label(self, bg=background_color, image=self.unchecked_photo)
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
            self.text_label.config(foreground=self.color_label)

    # Only changes the check box color
    def change_color_check_box(self, mode):
        if mode == var.selected_on:
            # If its On and the box's aren't selected, then select it
            if self.check_box_mode == CheckBoxMode.unchecked:
                self.check_box_mode = CheckBoxMode.unchecked_selected
                self.icon_label.config(image=self.unchecked_photo_selected)
            elif self.check_box_mode == CheckBoxMode.checked:
                self.check_box_mode = CheckBoxMode.checked_selected
                self.icon_label.config(image=self.checked_photo_selected)
        else:
            # If the mode is off, that means the checkbox should be white
            # only change if its currently on
            if self.check_box_mode == CheckBoxMode.unchecked_selected:
                self.check_box_mode = CheckBoxMode.unchecked
                self.icon_label.config(image=self.unchecked_photo)

            elif self.check_box_mode == CheckBoxMode.checked_selected:
                self.check_box_mode = CheckBoxMode.checked
                self.icon_label.config(image=self.checked_photo)

    # -------------------------- Updating Check Box Image -------------------------- #

    # Will be called when a user wants to change the preference. It will toggle the box image
    def update_check_box_image(self):

        if var.preferences[self.key]:
            # Will end up as a CHECKED box
            if self.check_box_mode == CheckBoxMode.unchecked:
                self.check_box_mode = CheckBoxMode.checked
                self.icon_label.config(image=self.checked_photo)
            if self.check_box_mode == CheckBoxMode.unchecked_selected:
                self.check_box_mode = CheckBoxMode.checked_selected
                self.icon_label.config(image=self.checked_photo_selected)

        else:
            # Will end up as an EMPTY box
            if self.check_box_mode == CheckBoxMode.checked:
                self.check_box_mode = CheckBoxMode.unchecked
                self.icon_label.config(image=self.unchecked_photo)
            if self.check_box_mode == CheckBoxMode.checked_selected:
                self.check_box_mode = CheckBoxMode.unchecked_selected
                self.icon_label.config(image=self.unchecked_photo_selected)

    def update_colored_boxes(self):
        self.unchecked_photo_selected = ImageTk.PhotoImage(
            imagecolor.tint(self.plain_empty_checked_box, var.selected_on))
        self.checked_photo_selected = ImageTk.PhotoImage(imagecolor.tint(self.plain_checked_box, var.selected_on))
