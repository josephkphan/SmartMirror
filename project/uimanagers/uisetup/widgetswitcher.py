from Tkinter import *
from project.resources import var


class WidgetSwitcher:
    def __init__(self, ui_handler):
        self.ui_handler = ui_handler

    def open_startup_page(self):
        self.ui_handler.start_up.pack(side=BOTTOM, anchor=S, padx=0, pady=0)

    def close_startup_page(self):
        self.ui_handler.start_up.pack_forget()

    def open_power_off_page(self):
        self.ui_handler.power_off.pack(side=BOTTOM, anchor=S, padx=200, pady=150)

    def close_power_off_page(self):
        self.ui_handler.power_off.pack_forget()

    # ---------------------------------- UI Functions ----------------------------------- #
    def open_main_page(self):
        self.ui_handler.main_weather.pack(side=TOP, anchor=W, padx=50, pady=50)
        self.ui_handler.main_clock.pack(side=RIGHT, anchor=N, padx=50, pady=25)
        self.ui_handler.main_news.pack(side=LEFT, anchor=S, padx=50, pady=50)
        self.ui_handler.main_settings.pack(side=RIGHT, anchor=S, padx=50, pady=50)
        # self.ui_handler.canvas.pack(side=TOP, anchor=W, padx=50)

    def close_main_page(self):
        self.ui_handler.main_weather.pack_forget()
        self.ui_handler.main_clock.pack_forget()
        self.ui_handler.main_news.pack_forget()
        self.ui_handler.main_settings.pack_forget()
        # self.ui_handler.canvas.pack_forget()

    # ---------------------------------- News Page Functions ----------------------------------- #
    def open_news_page(self):
        self.ui_handler.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)
        self.ui_handler.news_headlines.pack(side=BOTTOM, anchor=W, padx=50, pady=100)
        for i in range(0, len(var.stocks_list)):
            self.ui_handler.stocks[i].pack(side=TOP, anchor=E, padx=25, pady=15)

    def close_news_page(self):
        self.ui_handler.news_headlines.pack_forget()
        self.ui_handler.return_button.pack_forget()
        for i in range(0, len(var.stocks_list)):
            self.ui_handler.stocks[i].pack_forget()

    # ---------------------------------- Weather Page Functions----------------------------------- #
    def open_weather_page(self):
        self.ui_handler.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)
        for i in range(0, 24):
            self.ui_handler.weather_hourly[i].pack(side=TOP, anchor=W, padx=5, pady=5)
        self.ui_handler.weather_current.pack(side=TOP, anchor=N, padx=50, pady=50)

        self.ui_handler.container.pack(side=TOP, anchor=N)
        for i in range(0, 7):
            self.ui_handler.weather_daily[i].pack(side=LEFT, anchor=N, padx=0, pady=0)

    def close_weather_page(self):
        self.ui_handler.return_button.pack_forget()
        self.ui_handler.weather_current.pack_forget()
        for i in range(0, 7):
            self.ui_handler.weather_daily[i].pack_forget()

        for i in range(0, 24):
            self.ui_handler.weather_hourly[i].pack_forget()
        self.ui_handler.container.pack_forget()

    # ---------------------------------- Settings Page Functions ----------------------------------- #
    def open_settings_page(self):
        self.ui_handler.return_button.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.ui_handler.settings_update_now.pack(side=TOP, anchor=W, padx=50, pady=15)
        self.ui_handler.settings_color_scheme.pack(side=TOP, anchor=W, padx=50, pady=15)
        self.ui_handler.settings_font.pack(side=TOP, anchor=W, padx=50, pady=15)

    def close_settings_page(self):
        self.ui_handler.return_button.pack_forget()
        self.ui_handler.settings_color_scheme.pack_forget()
        self.ui_handler.settings_font.pack_forget()
        self.ui_handler.settings_update_now.pack_forget()

    # ---------------------------------- Planner Page Functions ----------------------------------- #
    def open_planner_page(self):
        self.ui_handler.return_button.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.ui_handler.planner_todolist.pack(side=TOP, anchor=W, padx=50, pady=50)
        self.ui_handler.planner_event_list.pack(side=BOTTOM, anchor=W, padx=15, pady=50)

    def close_planner_page(self):
        self.ui_handler.return_button.pack_forget()
        self.ui_handler.planner_todolist.pack_forget()
        self.ui_handler.planner_event_list.pack_forget()
