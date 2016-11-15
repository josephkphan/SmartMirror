from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var


class CheckBox(Frame):
    def __init__(self, parent, label="", key=""):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style

        Frame.__init__(self, bg=background_color)
        self.settings_selected = selected_off

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

        self.icon_label = Label(self, bg=background_color, image=self.filled_check_box_off) #todo change
        self.icon_label.image = self.filled_check_box_off
        self.icon_label.pack(side=LEFT, anchor=N, padx=20)


class Settings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        self.main_page_title_label = Label(self, text='Main Page:', font=(font_style, 18),
                                           fg=selected_off, bg=background_color)
        self.main_page_title_label.pack(side=TOP, anchor=W)

        self.weather_page_title_label = Label(self, text='Weather Page:', font=(font_style, 18),
                                              fg=selected_off, bg=background_color)
        self.weather_page_title_label.pack(side=TOP, anchor=W)

        self.weather_page_humidity = CheckBox(parent, 'Show Humidity', 'weather_page_humidity')
        self.weather_page_humidity.pack(side=TOP, anchor=W, padx=50)

        self.weather_page_humidity = CheckBox(parent, 'Show Sunrise', 'weather_page_humidity')
        self.weather_page_humidity.pack(side=TOP, anchor=W, padx=50)

        self.weather_page_humidity = CheckBox(parent, 'Show Sunset', 'weather_page_humidity') #todo change
        self.weather_page_humidity.pack(side=TOP, anchor=W, padx=50)
