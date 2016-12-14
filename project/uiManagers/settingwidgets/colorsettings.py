from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, zone, varLoader
from project.uiManagers.settingwidgets import checkbox


class ColorSettings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        # Main Page Settings
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)

        # ------------------------- Color ------------------------------ #

        self.color_yellow = selected_off
        self.color_blue = selected_off
        self.color_pink = selected_off
        self.color_green = selected_off
        self.color_red = selected_off

        # ------------------------- Keys ----------------------------- #

        self.bool_yellow, self.bool_blue, self.bool_pink, self.bool_green, self.bool_red = False, False, False, False, False
        selected_hex_code = var.preferences['color']
        if selected_hex_code == var.color_hex_codes['yellow']:
            self.bool_yellow = True
        elif selected_hex_code == var.color_hex_codes['blue']:
            self.bool_blue = True
        elif selected_hex_code == var.color_hex_codes['pink']:
            self.bool_pink = True
        elif selected_hex_code == var.color_hex_codes['green']:
            self.bool_green = True
        elif selected_hex_code == var.color_hex_codes['red']:
            self.bool_red = True
        self.mp_stocks = var.pref_keys['mp_stocks']
        self.mp_news = var.pref_keys['mp_news']
        self.mp_sunrise = var.pref_keys['mp_sunrise']
        self.mp_sunset = var.pref_keys['mp_sunset']
        self.mp_hilo = var.pref_keys['mp_hilo']

        # --------------------------- Main Page ------------------------------ #

        self.weather_page_title_label = Label(self.container, text='Color Scheme:', font=(font_style, 18),
                                              fg=selected_off, bg=background_color)
        self.weather_page_title_label.pack(side=TOP, anchor=W)

        self.stocks = checkbox.CheckBox(self.container, 'Yellow', self.mp_stocks)
        self.stocks.pack(side=TOP, anchor=W, padx=50)

        self.news = checkbox.CheckBox(self.container, 'Blue', self.mp_news)
        self.news.pack(side=TOP, anchor=W, padx=50)

        self.sunrise = checkbox.CheckBox(self.container, 'Pink', self.mp_sunrise)
        self.sunrise.pack(side=TOP, anchor=W, padx=50)

        self.sunset = checkbox.CheckBox(self.container, 'Green', self.mp_sunset)
        self.sunset.pack(side=TOP, anchor=W, padx=50)

        self.hilo = checkbox.CheckBox(self.container, 'Red', self.mp_hilo)
        self.hilo.pack(side=TOP, anchor=W, padx=50)

    def change_color_green(self, mode):
        if self.color_green != mode:
            self.color_green = mode
            self.sunset.change_color_all(mode)

    def change_color_pink(self, mode):
        if self.color_pink != mode:
            self.color_pink = mode
            self.sunrise.change_color_all(mode)

    def change_color_red(self, mode):
        if self.color_red != mode:
            self.color_red = mode
            self.hilo.change_color_all(mode)

    def change_color_blue(self, mode):
        if self.color_blue != mode:
            self.color_blue = mode
            self.news.change_color_all(mode)

    def change_color_yellow(self, mode):
        if self.color_yellow != mode:
            self.color_yellow = mode
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
