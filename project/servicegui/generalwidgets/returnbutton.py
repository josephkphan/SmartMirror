from Tkinter import *
from project.resources import var, imagecolor
from PIL import Image, ImageTk

# File Name: returnButton
# Purpose: created a text label "return" to go back to the main page

class ReturnButton(Frame):
    def __init__(self, parent):
        # Gets constant variables from var file
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)

        # initialize color for the label
        self.color_return = selected_off

        self.image = Image.open("assets/previous2.png")
        self.icon_photo, self.icon_photo_selected = None, None

        # Packs in the icon
        self.icon_label = Label(self, bg=background_color)
        self.create_photo()
        self.icon_label.pack(side=LEFT, anchor=E)

        # initialize the return label
        self.return_button = Label(self, text="Back", font=(font_style,  font_sizes['title']), fg=selected_off, bg=background_color)
        self.return_button.pack(side=LEFT, anchor=N)

    def create_photo(self):
        self.image = self.image.resize(var.font_sizes['small_medium_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        self.icon_photo = ImageTk.PhotoImage(self.image)
        self.icon_photo_selected = ImageTk.PhotoImage(imagecolor.tint(self.image, var.selected_on))
        self.icon_label.config(image=self.icon_photo)

    def update_now(self):
        if self.icon_photo is not None:
            self.create_photo()
        self.update_font_size()

    # Changes color based on specified mode
    def change_color_all(self, mode):
        if self.color_return != mode:
            self.color_return = mode  # update color boolean
            # Updating the image
            if self.color_return == var.selected_on:
                # changing image to on
                self.icon_label.config(image=self.icon_photo_selected)
            else:
                self.icon_label.config(image=self.icon_photo)
            # updates the text label
            self.return_button.config(foreground=self.color_return)

    def update_font_size(self):
        self.return_button.config(font=(var.font_style,  var.font_sizes['title']))
