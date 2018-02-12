from Tkinter import *
from PIL import Image, ImageTk
from resources import var, zone, varloader
from uimanagers.settingwidgets import checkbox


class MainPageSettings(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        # Main Page Settings
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)

        # ------------------------- Color ------------------------------ #

        self.color_weather = selected_off
        self.color_time = selected_off
        self.color_news = selected_off
        self.color_sports = selected_off
        self.color_stocks = selected_off

        # ---------------- Key from varLoader Preferences -------------- #
        self.key_weather='weather'
        self.key_time='time'
        self.key_news ='news'
        self.key_sports ='sports'
        self.key_stocks ='stocks'

        # --------------------------- Main Page ------------------------------ #

        self.main_page_title_label = Label(self.container, text='Main Page:', font=(font_style,  font_sizes['text']),
                                              fg=selected_off, bg=background_color)
        self.main_page_title_label.pack(side=TOP, anchor=W)

        self.top_half_title_label = Label(self.container, text='Top Half:', font=(font_style,  font_sizes['text']),
                                              fg=selected_off, bg=background_color,padx=50)
        self.top_half_title_label.pack(side=TOP, anchor=W)

        self.weather_label = checkbox.CheckBox(self.container, 'Weather on Left Side',  self.key_weather)
        self.weather_label.pack(side=TOP, anchor=W, padx=100)

        self.time_label = checkbox.CheckBox(self.container, 'Time on Left Side',  self.key_time)
        self.time_label.pack(side=TOP, anchor=W, padx=100)

        self.bottom_half_title_label = Label(self.container, text='Bottom Half:', font=(font_style,  font_sizes['text']),
                                              fg=selected_off, bg=background_color,padx=50 )
        self.bottom_half_title_label.pack(side=TOP, anchor=W)

        self.news_label = checkbox.CheckBox(self.container, 'Show News',  self.key_news)
        self.news_label.pack(side=TOP, anchor=W, padx=100)

        self.sports_label = checkbox.CheckBox(self.container, 'Show Sports', self.key_sports)
        self.sports_label.pack(side=TOP, anchor=W, padx=100)

        self.stocks_label = checkbox.CheckBox(self.container, 'Show Stocks', self.key_stocks)
        self.stocks_label.pack(side=TOP, anchor=W, padx=100)

    def change_all_label_colors(self, mode):
        self.change_color_weather(mode)
        self.change_color_time(mode)
        self.change_color_news(mode)
        self.change_color_sports(mode)
        self.change_color_stocks(mode)

    def change_color_weather(self, mode):
        if self.color_weather != mode:
            self.color_weather = mode
            self.weather_label.change_color_all(mode)

    def change_color_time(self, mode):
        if self.color_time != mode:
            self.color_time = mode
            self.time_label.change_color_all(mode)

    def change_color_news(self, mode):
        if self.color_news != mode:
            self.color_news = mode
            self.news_label.change_color_all(mode)

    def change_color_sports(self, mode):
        if self.color_sports != mode:
            self.color_sports = mode
            self.sports_label.change_color_all(mode)

    def change_color_stocks(self, mode):
        if self.color_stocks != mode:
            self.color_stocks = mode
            self.stocks_label.change_color_all(mode)

    def change_a_setting(self, zone_to_change):
        if zone_to_change == zone.SettingsPage.main_page_weather:
            varloader.change_main_page_top(self.key_weather)
            self.update_top_label_check_boxes()

        elif zone_to_change == zone.SettingsPage.main_page_time:
            varloader.change_main_page_top(self.key_time)
            self.update_top_label_check_boxes()

        elif zone_to_change == zone.SettingsPage.main_page_news:
            varloader.change_main_page_bottom(self.key_news)
            self.update_bottom_label_check_boxes()

        elif zone_to_change == zone.SettingsPage.main_page_sports:
            varloader.change_main_page_bottom(self.key_sports)
            self.update_bottom_label_check_boxes()

        elif zone_to_change == zone.SettingsPage.main_page_stocks:
            varloader.change_main_page_bottom(self.key_stocks)
            self.update_bottom_label_check_boxes()

    def update_top_label_check_boxes(self):
        self.weather_label.update_check_box_image()
        self.time_label.update_check_box_image()

    def update_bottom_label_check_boxes(self):
        self.news_label.update_check_box_image()
        self.sports_label.update_check_box_image()
        self.stocks_label.update_check_box_image()

    # Used by Color Settings Widget Class when color changes
    def update_all_label_check_boxes(self):
        self.weather_label.update_colored_boxes()
        self.time_label.update_colored_boxes()
        self.sports_label.update_colored_boxes()
        self.news_label.update_colored_boxes()
        self.stocks_label.update_colored_boxes()
