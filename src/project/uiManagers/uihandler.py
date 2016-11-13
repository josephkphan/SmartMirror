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

        # Handlers
        self.cursor_handler = CursorHandler()
        self.web_info = WebInfo()
        self.selection_handler = SelectionHandler()

        # TK
        self.tk = Tk()
        self.tk2 = Tk()

        # Page selection variables
        self.current_page = None
        self.zone = None

        # Main Page Widgets
        self.main_weather, self.main_clock, self.main_news = None, None, None

        # Weather Page Widgets
        self.weather_current, self.weather_hourly, self.weather_week = None, None, None
        self.weather_day = {}
        self.weather_hour = {}

        # General Widgets
        self.returnButton, self.last_updated = None, None

        # Frames for other pages
        self.left_top = None
        self.right_top = None
        self.weather_container = None

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

        # Configuring the UI window, Creating Frames
        self.tk.configure(background='black')
        self.top_frame = Frame(self.tk, background='black')
        self.top_frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottom_frame = Frame(self.tk, background='black')
        self.bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # self.tk.bind("<W>", self.update_page(Page.weather))
        # self.tk.bind("<M>", self.update_page(Page.main))  # todo : Doesn't work. please fix

        # Display data onto UI Window
        # self.current_page = Page.main
        # self.open_main_page()

        self.current_page = Page.weather
        self.open_weather_page()


        # calender - removing for now
        # self.calender = Calendar(self.bottom_frame)
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

    # ---------------------------------- Main Page ----------------------------------- #

    def open_main_page(self):
        # Weather
        self.main_weather = Weather(self.top_frame)
        self.main_weather.pack(side=LEFT, anchor=N, padx=50, pady=50)

        # Clock
        self.main_clock = Clock(self.top_frame)
        self.main_clock.pack(side=RIGHT, anchor=N, padx=50, pady=50)

        # News
        self.main_news = News(self.bottom_frame)
        self.main_news.pack(side=LEFT, anchor=S, padx=50, pady=50)

    def close_main_page(self):
        # Weather
        self.main_weather.destroy()
        self.main_weather = None

        # Clock
        self.main_clock.destroy()
        self.main_clock = None

        # News
        self.main_news.destroy()
        self.main_news = None

    # ---------------------------------- Weather Page ----------------------------------- #

    def open_weather_page(self):
        self.left_top = Frame(self.top_frame, bg=background_color)
        self.left_top.pack(side=LEFT, anchor=W)

        self.right_top = Frame(self.top_frame, bg=background_color)
        self.right_top.pack(side=RIGHT, anchor=N)

        # Return Button
        self.returnButton = ReturnButton(self.left_top)
        self.returnButton.pack(side=TOP, anchor=N, padx=15, pady=15)

        # Hourly Weather
        for i in range(0,24):
            self.weather_hour[i] = HourlyWeather(self.left_top, i)
            self.weather_hour[i].pack(side=TOP, anchor=N, padx=5, pady=5)

        # Current weather
        self.weather_current = CurrentWeather(self.right_top)
        self.weather_current.pack(side=TOP, anchor=N, padx=50, pady=50)

        # Daily Weather Container
        self.weather_container = Frame(self.right_top, bg=background_color)
        self.weather_container.pack(side=TOP, anchor=W)

        # Daily weather
        for i in range(0, 7):
            self.weather_day[i] = WeeklyWeather(self.weather_container, i)
            self.weather_day[i].pack(side=LEFT, anchor=N, padx=0, pady=0)

    def close_weather_page(self):
        # Return Button
        self.returnButton.destroy()
        self.returnButton = None

        # Current Weather
        self.weather_current.destroy()
        self.weather_current = None

        # Daily Weather
        for i in range(0, 7):
            self.weather_day[i].destroy()
            self.weather_day[i] = None

        # Hourly Weather
        for i in range(0, 24):
            self.weather_hour[i].destroy()
            self.weather_hour[i] = None

        self.left_top.destroy()
        self.right_top.destroy()
        self.weather_container.destroy()
        self.left_top, self.right_top, self.weather_container = None, None, None

    # ---------------------------------- UPDATING UIMANAGER ----------------------------------- #

    def update_all(self, cursor):
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

        self.update_zone(cursor)
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        self.canvas.move(self.cursor, diff_x, diff_y)
        self.circle_coord = cursor

        self.update_page(self.selection_handler.update(self.zone))

        # Update tk
        self.tk.update_idletasks()
        self.tk.update()
        self.tk2.update_idletasks()
        self.tk2.update()

    def update_zone(self, cursor):
        self.zone = self.cursor_handler.update_cursor(cursor, self.current_page)
        # Updating Zone based on Main Page
        if self.current_page == Page.main:
            if self.zone == MainPageZone.weather:
                self.main_weather.change_color_all(selected_on)
                self.main_news.change_color_news_title(selected_off)
                self.main_clock.change_color_all(selected_off)
            elif self.zone == MainPageZone.news:
                self.main_weather.change_color_all(selected_off)
                self.main_news.change_color_news_title(selected_on)
                self.main_clock.change_color_all(selected_off)
            elif self.zone == MainPageZone.clock:
                self.main_weather.change_color_all(selected_off)
                self.main_news.change_color_news_title(selected_off)
                self.main_clock.change_color_all(selected_on)
            else:
                self.main_weather.change_color_all(selected_off)
                self.main_news.change_color_news_title(selected_off)
                self.main_clock.change_color_all(selected_off)
        elif self.current_page == Page.weather:
            if self.zone == WeatherZone.returnButton:
                self.returnButton.change_color_all(selected_on)
            else:
                self.returnButton.change_color_all(selected_off)

    def update_page(self, new_page):
        if new_page is not None:
            if self.current_page == Page.main:
                if self.zone == MainPageZone.weather:
                    print "CHANGING PAGES"
                    self.change_page(Page.weather)
            elif self.current_page == Page.weather:
                if self.zone == WeatherZone.returnButton:
                    print "CHANGING PAGES"
                    self.change_page(Page.main)

    # ---------------------------------- HELPER ----------------------------------- #

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
