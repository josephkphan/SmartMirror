from src.project.resources.page import *

import src.project.resources.var
from cursorhandler import *
from selectionhandler import *
from src.project.resources.zone import *
from src.project.uiManagers.generalwidgets.returnButton import *
from src.project.uiManagers.mainpagewidgets.clock import *
from src.project.uiManagers.mainpagewidgets.news import *
from src.project.uiManagers.mainpagewidgets.weather import *
from src.project.uiManagers.weatherpagewidgets.currentweather import *
from src.project.uiManagers.weatherpagewidgets.dailyweather import *
from src.project.uiManagers.weatherpagewidgets.hourlyweather import *
from webinfo import *


# File Name: UI Handler:
# Purpose: Handles all TKinter widgets and displays them appropriately based on the given inputs from the hardware


class UIManager:
    def __init__(self):
        self.cursor_handler = CursorHandler()
        self.web_info = WebInfo()
        self.selection_handler = SelectionHandler()
        self.tk = Tk()
        self.tk2 = Tk()
        self.current_page = None
        self.zone = None
        self.counter = 0

        # Main Page Widgets
        self.main_weather, self.main_clock, self.main_news = None, None, None
        # Weather Page Widgets
        self.weather_current, self.weather_hourly, self.weather_week = None, None, None
        self.weather_day = {}
        self.weather_hour = {}
        # General Widgets
        self.returnButton, self.last_updated = None, None

        # Creating the Cursor window
        self.canvas = Canvas(self.tk2, width=camera_width + tk_cursor_diameter,
                             height=camera_height + tk_cursor_diameter, background='black')
        self.circle_coord = (0, 0)
        self.circle_diameter = tk_cursor_diameter  # todo scale the cursor to match screen size
        self.cursor = self.canvas.create_oval(0, 0, tk_cursor_diameter, tk_cursor_diameter,
                                              fill="blue", outline="#DDD", width=tk_cursor_outline_thickness)
        # Vertical line
        self.line1 = self.canvas.create_line((camera_width / 2 + tk_cursor_diameter / 2, 0),
                                             (camera_width / 2 + tk_cursor_diameter / 2,
                                              camera_height + tk_cursor_diameter), fill="green")
        # Horizontal line
        self.line2 = self.canvas.create_line((0, camera_height / 2 + tk_cursor_diameter / 2),
                                             (camera_width + tk_cursor_diameter,
                                              camera_height / 2 + tk_cursor_diameter / 2), fill="green")
        self.canvas.pack()

        # Configuring the UI window
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # self.tk.bind("<W>", self.update_page(Page.weather))
        # self.tk.bind("<M>", self.update_page(Page.main))  # todo : Doesn't work. please fix

        # Gather Data from Web
        # self.web_info.update()

        # Display data onto UI Window
        self.current_page = Page.main
        self.open_main_page()   #todo CHANGE BACK TO MAIN

        # self.current_page = Page.weather
        # self.open_weather_page()   #todo CHANGE BACK TO MAIN


        # calender - removing for now
        # self.calender = Calendar(self.bottomFrame)
        # self.calender.pack(side = RIGHT, anchor=S, padx=100, pady=60)

    # ---------------------------------- Key Binding Functions----------------------------------- #

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    # ---------------------------------- Pages ----------------------------------- #

    # ---------------------------------- MAIN PAGE ----------------------------------- #

    def open_main_page(self):
        self.start_clock()
        self.start_weather()
        self.start_news()

    def close_main_page(self):
        self.end_news()
        self.end_weather()
        self.end_clock()

    # ---------------------------------- Weather PAGE ----------------------------------- #

    def open_weather_page(self):
        self.new_return_button()
        self.start_today_weather()
        self.start_daily_weather()
        self.start_hourly_weather()

    def close_weather_page(self):
        self.remove_return_button()
        self.end_today_weather()
        self.end_daily_weather()
        self.end_hourly_weather()


    # ---------------------------------- --------------- ----------------------------------- #
    # ---------------------------------- PAGE COMPONENTS ----------------------------------- #

    # ---------------------------------- MAIN PAGE COMPONENTS ----------------------------------- #
    def start_news(self):
        self.main_news = News(self.bottomFrame)
        self.main_news.pack(side=LEFT, anchor=S, padx=50, pady=50)

    def end_news(self):
        self.main_news.destroy()
        self.main_news = None

    def start_weather(self):
        self.main_weather = Weather(self.topFrame)
        self.main_weather.pack(side=LEFT, anchor=N, padx=50, pady=50)

    def end_weather(self):
        self.main_weather.destroy()
        self.main_weather = None

    def start_clock(self):
        self.main_clock = Clock(self.topFrame)
        self.main_clock.pack(side=RIGHT, anchor=N, padx=50, pady=50)

    def end_clock(self):
        self.main_clock.destroy()
        self.main_clock = None

    # ---------------------------------- WEATHER PAGE COMPONENTS ----------------------------------- #

    def start_today_weather(self):
        self.weather_current = CurrentWeather(self.topFrame)     # todo finish this
        self.weather_current.pack(side=RIGHT, anchor=N, padx=50, pady=50)


    def end_today_weather(self):
        self.weather_current.destroy()
        self.weather_current = None

    def start_daily_weather(self):
        for i in range(0,7):
            self.weather_day[i] = WeeklyWeather(self.topFrame,i)
            self.weather_day[i].pack(side=TOP, anchor=N, padx=5, pady=5)

    def end_daily_weather(self):
        for i in range(0, 7):
            self.weather_day[i].destroy()
            self.weather_day[i] = None

    def start_hourly_weather(self):
        for i in range(0,24):
            self.weather_hour[i] = HourlyWeather(self.topFrame, i)
            self.weather_hour[i].pack(side=TOP, anchor=N, padx=5, pady=5)

    def end_hourly_weather(self):
        for i in range(0, 24):
            self.weather_hour[i].destroy()
            self.weather_hour[i] = None


    # ---------------------------------- OTHER COMPONENTS ----------------------------------- #

    def new_return_button(self):
        self.returnButton = ReturnButton(self.topFrame)
        self.returnButton.pack(side=LEFT, anchor=N, padx=15, pady=15)

    def remove_return_button(self):
        self.returnButton.destroy()
        self.returnButton = None

    # ---------------------------------- UPDATING UIMANAGER ----------------------------------- #

    def update_all(self, cursor):
        #update web data
        last_update_time = (time.time() - src.project.resources.var.saved_data['last_updated']) / 60
        # print last_update_time
        if last_update_time >=src.project.resources.var.update_time and self.current_page == Page.main:
            # Means its been 10 minutes since it last updated
            print "UPDATING WEB INFO. REQUESTING FROM WEB"
            self.main_clock.change_update_label_to_updating()
            self.web_info.update()
            if self.main_weather is not None:
                self.main_weather.update()
            if self.main_news is not None:
                self.main_news.update()             # todo Current only updates main page. need to update everything

        # if self.counter == 100:
        #     self.change_page(Page.weather)
        # elif self.counter == 200:
        #     self.change_page(Page.main)
        # self.counter += 1
        self.update_zone(cursor)
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        self.canvas.move(self.cursor, diff_x, diff_y)
        self.circle_coord = cursor

        self.update_page(self.selection_handler.update(self.zone))

        self.tk.update_idletasks()
        self.tk.update()
        self.tk2.update_idletasks()
        self.tk2.update()

    def update_zone(self, cursor):
        self.zone = self.cursor_handler.update_cursor(cursor, self.current_page)
        # Updating Zone based on Main Page
        if self.current_page == Page.main:
            if self.zone == MainPageZone.weather:
                self.main_weather.change_color_to_yellow()
                self.main_news.change_news_title_to_white()
                self.main_clock.change_color_to_white()
            elif self.zone == MainPageZone.news:
                self.main_weather.change_color_to_white()
                self.main_news.change_news_title_to_yellow()
                self.main_clock.change_color_to_white()
            elif self.zone == MainPageZone.clock:
                self.main_weather.change_color_to_white()
                self.main_news.change_news_title_to_white()
                self.main_clock.change_color_to_yellow()
            else:
                self.main_weather.change_color_to_white()
                self.main_news.change_news_title_to_white()
                self.main_clock.change_color_to_white()
        elif self.current_page == Page.weather:
            if self.zone == WeatherZone.returnButton:
                self.returnButton.change_color_to_yellow()
            else:
                self.returnButton.change_color_to_white()

    def update_page(self, new_page):
        if new_page is not None:
            if self.current_page == Page.main:
                if self.zone == MainPageZone.weather:
                    self.change_page(Page.weather)
            elif self.current_page == Page.weather:
                if self.zone == WeatherZone.returnButton:
                    self.change_page(Page.main)

    def change_page(self, new_page):
        if new_page == Page.main:  # MAIN PAGE
            if self.current_page == Page.weather:
                self.close_weather_page()           # todo remove previous page if weather, news, etc
            self.open_main_page()
            self.current_page = Page.main
        elif new_page == Page.weather:  # BLANK PAGE
            self.close_main_page()
            self.open_weather_page()
            self.current_page = Page.weather
