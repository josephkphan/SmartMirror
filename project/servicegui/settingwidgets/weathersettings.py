from Tkinter import *
from PIL import Image, ImageTk
from resources import var
from uimanagers.settingwidgets import checkbox

class WeatherSettings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        # Weather Settings
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)

        self.weather_page_title_label = Label(self.container, text='Weather Page:', font=(font_style,  font_sizes['text']),
                                              fg=selected_off, bg=background_color)
        self.weather_page_title_label.pack(side=TOP, anchor=W)

        self.weather_page_humidity = checkbox.CheckBox(self.container, 'Show Humidity', 'weather_page_humidity')
        self.weather_page_humidity.pack(side=TOP, anchor=W, padx=50)

        self.weather_page_humidity = checkbox.CheckBox(self.container, 'Show Sunrise', 'weather_page_humidity')
        self.weather_page_humidity.pack(side=TOP, anchor=W, padx=50)

        self.weather_page_humidity = checkbox.CheckBox(self.container, 'Show Sunset', 'weather_page_humidity')
        self.weather_page_humidity.pack(side=TOP, anchor=W, padx=50)

