from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, imagecolor


class SettingsButton(Frame):
    def __init__(self,parent):
        # keep an instance of the constant variables in var file
        # (just so you don't need to continually say var._____)
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, bg=background_color)

        # to keep track of current color
        self.settings_selected = selected_off

        # initialize the 2 possible images
        # Settings - white
        image = Image.open("assets/settings.png")
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.icon_photo = ImageTk.PhotoImage(image)

        # Settings - Yellow
        image = imagecolor.tint(image, var.selected_on)
        self.icon_photo_selected = ImageTk.PhotoImage(image)

        # Packs in the icon
        self.icon_label = Label(self, bg=background_color, image=self.icon_photo)
        self.icon_label.image = self.icon_photo
        self.icon_label.pack(side=LEFT, anchor=N)

        # Adds in "settings label"
        self.settings_text = "Settings"
        self.settings_text_label = Label(self, text=self.settings_text, font=(font_style, 24), fg=selected_off,
                                         bg=background_color)
        self.settings_text_label.pack(side=LEFT, anchor=CENTER)

    # Changes color based on passed in mode
    def change_color_setting(self, mode):
        if self.settings_selected != mode:
            self.settings_selected = mode  # update color boolean
            # Updating the image
            if self.settings_selected == var.selected_on:
                # changing image to on
                self.icon_label.config(image=self.icon_photo_selected)
            else:
                self.icon_label.config(image=self.icon_photo)
            # updates the text label
            self.settings_text_label.config(foreground=self.settings_selected)
