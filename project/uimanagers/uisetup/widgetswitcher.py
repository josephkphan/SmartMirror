from Tkinter import *

class WidgetSwitcher:
    def __init__(self, uiHandler):
        self.uiHandler = uiHandler

    # ---------------------------------- UI Functions ----------------------------------- #
    def open_main_page(self):
        self.uiHandler.main_weather.pack(side=TOP, anchor=W, padx=50, pady=50)
        self.uiHandler.main_clock.pack(side=RIGHT, anchor=N, padx=50, pady=50)
        self.uiHandler.main_news.pack(side=LEFT, anchor=S, padx=50, pady=50)
        self.uiHandler.main_settings.pack(side=RIGHT, anchor=S, padx=50, pady=50)
        # self.uiHandler.canvas.pack(side=TOP, anchor=W, padx=50)

    def close_main_page(self):
        self.uiHandler.main_weather.pack_forget()
        self.uiHandler.main_clock.pack_forget()
        self.uiHandler.main_news.pack_forget()
        self.uiHandler.main_settings.pack_forget()
        # self.uiHandler.canvas.pack_forget()

    # ---------------------------------- News Page Functions ----------------------------------- #
    def open_news_page(self):
        self.uiHandler.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)
        self.uiHandler.news_headlines.pack(side=BOTTOM, anchor=S, padx=50, pady=50)

    def close_news_page(self):
        self.uiHandler.news_headlines.pack_forget()
        self.uiHandler.return_button.pack_forget()

    # ---------------------------------- Planner Page Functions----------------------------------- #
    def open_planner_page(self):
        self.uiHandler.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)

    def close_planner_page(self):
        self.uiHandler.return_button.pack_forget()

    # ---------------------------------- Weather Page Functions----------------------------------- #
    def open_weather_page(self):
        self.uiHandler.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)
        for i in range(0, 24):
            self.uiHandler.weather_hourly[i].pack(side=TOP, anchor=W, padx=5, pady=5)
        self.uiHandler.weather_current.pack(side=TOP, anchor=N, padx=50, pady=50)

        self.uiHandler.container.pack(side=TOP, anchor=N)
        for i in range(0, 7):
            self.uiHandler.weather_daily[i].pack(side=LEFT, anchor=N, padx=0, pady=0)

    def close_weather_page(self):
        self.uiHandler.return_button.pack_forget()
        self.uiHandler.weather_current.pack_forget()
        for i in range(0, 7):
            self.uiHandler.weather_daily[i].pack_forget()

        for i in range(0, 24):
            self.uiHandler.weather_hourly[i].pack_forget()
        self.uiHandler.container.pack_forget()

    # ---------------------------------- Settings Page Functions ----------------------------------- #
    def open_settings_page(self):
        self.uiHandler.return_button.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.uiHandler.settings_update_now.pack(side=TOP, anchor=W, padx=50, pady=15)
        self.uiHandler.settings_color_scheme.pack(side=TOP, anchor=W, padx=50, pady=15)
        self.uiHandler.settings_font.pack(side=TOP, anchor=W, padx=50, pady=15)

    def close_settings_page(self):
        self.uiHandler.return_button.pack_forget()
        self.uiHandler.settings_color_scheme.pack_forget()
        self.uiHandler.settings_font.pack_forget()
        self.uiHandler.settings_update_now.pack_forget()

    # ---------------------------------- Planner Page Functions ----------------------------------- #
    def open_planner_page(self):
        self.uiHandler.return_button.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.uiHandler.planner_todolist.pack(side=TOP, anchor=W, padx=50, pady=50)

    def close_planner_page(self):
        self.uiHandler.return_button.pack_forget()
        self.uiHandler.planner_todolist.pack_forget()