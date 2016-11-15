from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var

class SettingsButton(Frame):
    def __init__(self):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, bg=background_color)
        image = Image.open("assets/newspaper.png")  # todo DOesnt WOrk! FIX THIS
        image = image.resize((25, 25), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.icon_label = Label(self, bg=background_color, image=photo)
        self.icon_label.image = photo

