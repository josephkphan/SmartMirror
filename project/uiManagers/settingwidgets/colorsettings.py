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
        self.current_color = var.preferences['color']

        # ------------------------- Color ------------------------------ #

        self.color_yellow = selected_off
        self.color_blue = selected_off
        self.color_pink = selected_off
        self.color_green = selected_off
        self.color_red = selected_off

        # ------------------------- Keys ----------------------------- #

        self.key_yellow = 'color_page_yellow'
        self.key_red = 'color_page_red'
        self.key_green='color_page_green'
        self.key_pink='color_page_pink'
        self.key_blue='color_page_blue'

        # --------------------------- Main Page ------------------------------ #

        self.title_label = Label(self.container, text='Color Scheme:', font=(font_style, 18),
                                              fg=selected_off, bg=background_color)
        self.title_label.pack(side=TOP, anchor=W)

        self.blue_label = checkbox.CheckBox(self.container, 'Blue', self.key_blue)
        self.blue_label.pack(side=TOP, anchor=W, padx=50)

        self.green_label = checkbox.CheckBox(self.container, 'Green', self.key_green )
        self.green_label.pack(side=TOP, anchor=W, padx=50)

        self.pink_label = checkbox.CheckBox(self.container, 'Pink', self.key_pink)
        self.pink_label.pack(side=TOP, anchor=W, padx=50)

        self.red_label = checkbox.CheckBox(self.container, 'Red', self.key_red)
        self.red_label.pack(side=TOP, anchor=W, padx=50)

        self.yellow_label = checkbox.CheckBox(self.container, 'Yellow', self.key_yellow)
        self.yellow_label.pack(side=TOP, anchor=W, padx=50)

    def change_color_green(self, mode):
        if self.color_green != mode:
            self.color_green = mode
            self.green_label.change_color_all(mode)

    def change_color_pink(self, mode):
        if self.color_pink != mode:
            self.color_pink = mode
            self.pink_label.change_color_all(mode)

    def change_color_red(self, mode):
        if self.color_red != mode:
            self.color_red = mode
            self.red_label.change_color_all(mode)

    def change_color_blue(self, mode):
        if self.color_blue != mode:
            self.color_blue = mode
            self.blue_label.change_color_all(mode)

    def change_color_yellow(self, mode):
        if self.color_yellow != mode:
            self.color_yellow = mode
            self.yellow_label.change_color_all(mode)

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
