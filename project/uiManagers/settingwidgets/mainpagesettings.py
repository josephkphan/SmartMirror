from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var
from project.uiManagers.settingwidgets import checkbox


class MainPageSettings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        # Main Page Settings
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)

        self.weather_page_title_label = Label(self.container, text='Main Page:', font=(font_style, 18),
                                              fg=selected_off, bg=background_color)
        self.weather_page_title_label.pack(side=TOP, anchor=W)

        self.stocks = checkbox.CheckBox(self.container, 'Show Stocks', 'main_page_stocks')
        self.stocks.pack(side=TOP, anchor=W, padx=50)

        self.news = checkbox.CheckBox(self.container, 'Show News', 'main_page_news')
        self.news.pack(side=TOP, anchor=W, padx=50)

        self.sunset = checkbox.CheckBox(self.container, 'Show Sunset', 'main_page_sunset')
        self.sunset.pack(side=TOP, anchor=W, padx=50)

        self.sunset = checkbox.CheckBox(self.container, 'Show SunRise', 'main_page_sunrise')
        self.sunset.pack(side=TOP, anchor=W, padx=50)

