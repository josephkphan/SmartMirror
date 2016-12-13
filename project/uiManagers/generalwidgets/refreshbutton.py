from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var

#Not yet tested
class RefreshButton(Frame):
    def __init__(self, parent):
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
        image = Image.open("assets/refresh.png")  # todo DOesnt WOrk! FIX THIS
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.photo_not_selected = ImageTk.PhotoImage(image)

        # Settings - Yellow
        image = Image.open("assets/refresh_on.png")  # todo DOesnt WOrk! FIX THIS
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = image.convert('RGB')
        self.photo_selected = ImageTk.PhotoImage(image)

        # Packs in the icon
        self.icon_label = Label(self, bg=background_color, image=self.photo_not_selected)
        self.icon_label.image = self.photo_not_selected
        self.icon_label.pack(side=LEFT, anchor=N)

        # Adds in label
        self.settings_text = "Refresh Now"
        self.settings_text_label = Label(self, text=self.settings_text, font=(font_style, 24), fg=selected_off,
                                      bg=background_color)
        self.settings_text_label.pack(side=LEFT, anchor=CENTER)

    # Changes color based on passed in mode
    def change_color(self, mode):
        if self.settings_selected != mode:
            self.settings_selected = mode
            if self.settings_selected == var.selected_on:
                self.icon_label.config(image=self.photo_selected)
                self.icon_label.image = self.photo_selected
            else:
                self.icon_label.config(image=self.photo_not_selected)
                self.icon_label.image = self.photo_not_selected
            self.settings_text_label.config(foreground=self.settings_selected)


