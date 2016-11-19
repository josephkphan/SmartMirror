from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, zone, varLoader
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

        # ------------------------- Color ------------------------------ #

        self.color_stocks = selected_off
        self.color_news = selected_off
        self.color_sunset = selected_off
        self.color_sunrise = selected_off
        self.color_hilo = selected_off

        # ------------------------- Keys ----------------------------- #

        self.mp_humidity = var.pref_keys['mp_humidity']  # todo NOT USED
        self.mp_sunrise = var.pref_keys['mp_sunrise']
        self.mp_sunset = var.pref_keys['mp_sunset']
        self.mp_stocks = var.pref_keys['mp_stocks']
        self.mp_news = var.pref_keys['mp_news']
        self.mp_hilo = var.pref_keys['mp_hilo']

        # --------------------------- Main Page ------------------------------ #

        self.weather_page_title_label = Label(self.container, text='Main Page:', font=(font_style, 18),
                                              fg=selected_off, bg=background_color)
        self.weather_page_title_label.pack(side=TOP, anchor=W)

        self.stocks = checkbox.CheckBox(self.container, 'Show Stocks', self.mp_stocks)
        self.stocks.pack(side=TOP, anchor=W, padx=50)

        self.news = checkbox.CheckBox(self.container, 'Show News', self.mp_news)
        self.news.pack(side=TOP, anchor=W, padx=50)

        self.sunrise = checkbox.CheckBox(self.container, 'Show Sunrise time', self.mp_sunrise)
        self.sunrise.pack(side=TOP, anchor=W, padx=50)

        self.sunset = checkbox.CheckBox(self.container, 'Show Sunset time', self.mp_sunset)
        self.sunset.pack(side=TOP, anchor=W, padx=50)

        self.hilo = checkbox.CheckBox(self.container, 'Show High Low for Day', self.mp_hilo)
        self.hilo.pack(side=TOP, anchor=W, padx=50)

    def change_color_sunset(self, mode):
        if self.color_sunset != mode:
            self.color_sunset = mode
            self.sunset.change_color_all(mode)

    def change_color_sunrise(self, mode):
        if self.color_sunrise != mode:
            self.color_sunrise = mode
            self.sunrise.change_color_all(mode)

    def change_color_hilo(self, mode):
        if self.color_hilo != mode:
            self.color_hilo = mode
            self.hilo.change_color_all(mode)

    def change_color_news(self, mode):
        if self.color_news != mode:
            self.color_news = mode
            self.news.change_color_all(mode)

    def change_color_stocks(self, mode):
        if self.color_stocks != mode:
            self.color_stocks = mode
            self.stocks.change_color_all(mode)

    def change_a_setting(self, zone_to_change):
        print "~~~~~~~ INSIDE CHANGE A SETTING"
        print zone_to_change
        if zone_to_change == zone.SettingsPage.main_page_stocks:
            varLoader.toggle_preferences(self.mp_stocks)
            self.stocks.update_check_box_image()


        # elif zone_to_change == zone.SettingsPage.main_page_high_low:
        #     varLoader.toggle_preferences(self.mp_humidity)
        #     self.humidity.update_check_box_image()

        elif zone_to_change == zone.SettingsPage.main_page_news:
            varLoader.toggle_preferences(self.mp_news)
            self.news.update_check_box_image()

        elif zone_to_change == zone.SettingsPage.main_page_sunrise:
            varLoader.toggle_preferences(self.mp_sunrise)
            self.sunrise.update_check_box_image()

        elif zone_to_change == zone.SettingsPage.main_page_sunset:
            varLoader.toggle_preferences(self.mp_sunset)
            self.sunset.update_check_box_image()

        elif zone_to_change == zone.SettingsPage.main_page_high_low:
            varLoader.toggle_preferences(self.mp_hilo)
            self.hilo.update_check_box_image()
