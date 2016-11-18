
from project.resources import var
from webinfo import *
from cursorhandler import *
from selectionhandler import *
from project.uiManagers.mainpagewidgets.news import *
from project.uiManagers.mainpagewidgets.clock import *
from project.uiManagers.mainpagewidgets.weather import *
from project.uiManagers.generalwidgets.returnButton import *
from project.uiManagers.generalwidgets.settingsbutton import *
from project.uiManagers.weatherpagewidgets.dailyweather import *
from project.uiManagers.weatherpagewidgets.hourlyweather import *
from project.uiManagers.weatherpagewidgets.currentweather import *
from project.uiManagers.settingwidgets.weathersettings import *
from project.uiManagers.settingwidgets.mainpagesettings import *
from project.resources import zone, pagegraph, var
from project.resources.page import *


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

        # initializing Keys
        self.key_up, self.key_down, self.key_left, self.key_right = 0,1,2,3

        # Main Page Widgets
        self.main_weather, self.main_clock, self.main_news, self.main_settings = None, None, None, None

        # Weather Page Widgets
        self.weather_current, self.weather_hourly, self.weather_week = None, None, None
        self.weather_day = {}
        self.weather_hour = {}

        # Setting Widgets
        self.main_page_settings, self.weather_page_settings = None, None

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
        self.tk.bind("<Tab>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk.bind("<Left>", self.left_click)
        self.tk.bind("<Right>", self.right_click)
        self.tk.bind("<Up>", self.up_click)
        self.tk.bind("<Down>", self.down_click)
        self.tk.bind("<Control_R>", self.enter_click)

        # Display data onto UI Window

        self.current_zone = zone.MainPage.none
        self.current_page = Page.main
        self.open_main_page()

        # self.current_page = Page.weather
        # self.open_weather_page()

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

    # ------------------------ Used for Manual Mode ------------------------- #

    def left_click(self, event=None):
        print "LEFT CLICK HAPPENED"
        self.directional_click(self.key_left)
        return "break"

    def right_click(self, event=None):
        print "RIGHT CLICK HAPPENED"
        self.directional_click(self.key_right)
        return "break"

    def up_click(self, event=None):
        print "UP CLICK HAPPENED"
        self.directional_click(self.key_up)
        return "break"

    def down_click(self, event=None):
        print "DOWN CLICK HAPPENED"
        self.directional_click(self.key_down)
        return "break"

    def directional_click(self,key_click):
        if self.current_page == Page.main:
            self.current_zone = pagegraph.Main[self.current_zone][key_click]
        elif self.current_page == Page.weather:
            self.current_zone = pagegraph.Weather[self.current_zone][key_click]
        elif self.current_page == Page.settings:
            self.current_zone = pagegraph.Settings[self.current_zone][key_click]

    def enter_click(self, event=None):
        print "Enter CLICK HAPPENED"
        self.change_page(self.find_page_to_change_to())
        if self.current_page == Page.settings:
            print "HEEREEEEEEEEE"
            self.main_page_settings.change_a_setting(self.current_zone)
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

        # Settings
        self.main_settings = SettingsButton(self.bottom_frame)
        self.main_settings.pack(side=BOTTOM, anchor=SE, padx=50, pady=10)

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

        self.main_settings.destroy()
        self.main_settings = None

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
        for i in range(0, 24):
            self.weather_hour[i] = HourlyWeather(self.left_top, i)
            self.weather_hour[i].pack(side=TOP, anchor=W, padx=5, pady=5)

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

    # ---------------------------------- Settings Page ----------------------------------- #
    def open_settings_page(self):
        self.returnButton = ReturnButton(self.top_frame)
        self.returnButton.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.main_page_settings = MainPageSettings(self.top_frame)
        self.main_page_settings.pack(side=TOP, anchor=W, padx=50, pady=15)
        # self.weather_page_settings = WeatherSettings(self.top_frame)
        # self.weather_page_settings.pack(side=TOP, anchor=W, padx=50, pady=15)

    def close_settings_page(self):
        # Return Button
        self.returnButton.destroy()
        self.returnButton = None
        self.main_page_settings.destroy()
        self.main_page_settings = None
        # self.weather_page_settings.destroy()
        # self.weather_page_settings = None

    # --------    -------------------------- UPDATING UIMANAGER - ----------------------------------  #

    def update_all(self, cursor):
        self.update_web_info()
        self.get_current_zone_from_cursor(cursor)
        self.update_zone()
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        self.canvas.move(self.cursor, diff_x, diff_y)
        self.circle_coord = cursor

        self.update_page(self.selection_handler.update(self.current_zone))

        # Update tk
        self.update_tk()

    def update_all_manually(self):
        self.update_web_info()
        self.update_zone()
        # Update tk
        self.update_tk()

    # --------------------------------- Updating Web Info ------------------------------------- #

    def update_web_info(self):
        last_update_time = (time.time() - var.saved_data['last_updated']) / 60
        # print last_update_time
        if last_update_time >= var.update_time and self.current_page == Page.main:
            # Means its been 10 minutes since it last updated
            print "UPDATING WEB INFO. REQUESTING FROM WEB"
            self.main_clock.change_update_label_to_updating()
            self.web_info.update()
            if self.main_weather is not None:
                self.main_weather.update()
            if self.main_news is not None:
                self.main_news.update()  # todo Current only updates main page. need to update everything

    # --------------------------------- Updating Tk ------------------------------------- #

    def update_tk(self):
        self.tk.update_idletasks()
        self.tk.update()
        self.tk2.update_idletasks()
        self.tk2.update()

    # --------------------------------- Updating Zones ------------------------------------- #
    def get_current_zone_from_cursor(self,cursor):
        self.current_zone = self.cursor_handler.update_cursor(cursor, self.current_page)

    def update_zone(self):
        if self.current_page == Page.main:
            self.update_zone_main_page()
        # Updating zones for Weather Page
        elif self.current_page == Page.weather:
            self.update_zone_weather_page()
        # Updating Zones for Settings Page
        elif self.current_page == Page.settings:
            self.update_zone_settings_page()

    # Helper for Updating Zones
    def update_zone_main_page(self):
        # Weather Zone Selected
        if self.current_zone == zone.MainPage.weather:
            self.main_weather.change_color_all(var.selected_on)
            self.main_news.change_color_news_title(var.selected_off)
            self.main_clock.change_color_all(var.selected_off)
            self.main_settings.change_color_setting(var.selected_off)
        # News Zone Selected
        elif self.current_zone == zone.MainPage.news:
            self.main_weather.change_color_all(var.selected_off)
            self.main_news.change_color_news_title(var.selected_on)
            self.main_clock.change_color_all(var.selected_off)
            self.main_settings.change_color_setting(var.selected_off)
        # Clock Zone Selected
        elif self.current_zone == zone.MainPage.clock:
            self.main_weather.change_color_all(var.selected_off)
            self.main_news.change_color_news_title(var.selected_off)
            self.main_clock.change_color_all(var.selected_on)
            self.main_settings.change_color_setting(var.selected_off)
        # Settings Zone Selected
        elif self.current_zone == zone.MainPage.settings:
            self.main_weather.change_color_all(var.selected_off)
            self.main_news.change_color_news_title(var.selected_off)
            self.main_clock.change_color_all(var.selected_off)
            self.main_settings.change_color_setting(var.selected_on)
        # Nothing Selected
        else:
            self.main_weather.change_color_all(var.selected_off)
            self.main_news.change_color_news_title(var.selected_off)
            self.main_clock.change_color_all(var.selected_off)
            self.main_settings.change_color_setting(var.selected_off)

    def update_zone_weather_page(self):
        # Return Button Selected
        if self.current_zone == zone.WeatherPage.returnButton:
            self.returnButton.chnge_color_all(var.selected_on)
        else:
            self.returnButton.chnge_color_all(var.selected_off)

    def update_zone_settings_page(self):
        # Return Button Selected
        if self.current_zone == zone.SettingsPage.returnButton:
            self.returnButton.change_color_all(var.selected_on)
            self.main_page_settings.change_color_stocks(var.selected_off)
            self.main_page_settings.change_color_news(var.selected_off)
            self.main_page_settings.change_color_sunrise(var.selected_off)
            self.main_page_settings.change_color_sunset(var.selected_off)
            self.main_page_settings.change_color_hilo(var.selected_off)
        elif self.current_zone == zone.SettingsPage.main_page_stocks:
            self.returnButton.change_color_all(var.selected_off)
            self.main_page_settings.change_color_stocks(var.selected_on)
            self.main_page_settings.change_color_news(var.selected_off)
            self.main_page_settings.change_color_sunrise(var.selected_off)
            self.main_page_settings.change_color_sunset(var.selected_off)
            self.main_page_settings.change_color_hilo(var.selected_off)
        elif self.current_zone == zone.SettingsPage.main_page_news:
            self.returnButton.change_color_all(var.selected_off)
            self.main_page_settings.change_color_stocks(var.selected_off)
            self.main_page_settings.change_color_news(var.selected_on)
            self.main_page_settings.change_color_sunrise(var.selected_off)
            self.main_page_settings.change_color_sunset(var.selected_off)
            self.main_page_settings.change_color_hilo(var.selected_off)
        elif self.current_zone == zone.SettingsPage.main_page_sunrise:
            self.returnButton.change_color_all(var.selected_off)
            self.main_page_settings.change_color_stocks(var.selected_off)
            self.main_page_settings.change_color_news(var.selected_off)
            self.main_page_settings.change_color_sunrise(var.selected_on)
            self.main_page_settings.change_color_sunset(var.selected_off)
            self.main_page_settings.change_color_hilo(var.selected_off)
        elif self.current_zone == zone.SettingsPage.main_page_sunset:
            self.returnButton.change_color_all(var.selected_off)
            self.main_page_settings.change_color_stocks(var.selected_off)
            self.main_page_settings.change_color_news(var.selected_off)
            self.main_page_settings.change_color_sunrise(var.selected_off)
            self.main_page_settings.change_color_sunset(var.selected_on)
            self.main_page_settings.change_color_hilo(var.selected_off)
        elif self.current_zone == zone.SettingsPage.main_page_high_low:
            self.returnButton.change_color_all(var.selected_off)
            self.main_page_settings.change_color_stocks(var.selected_off)
            self.main_page_settings.change_color_news(var.selected_off)
            self.main_page_settings.change_color_sunrise(var.selected_off)
            self.main_page_settings.change_color_sunset(var.selected_off)
            self.main_page_settings.change_color_hilo(var.selected_on)
        else:
            self.returnButton.change_color_all(var.selected_off)
            self.main_page_settings.change_color_stocks(var.selected_off)
            self.main_page_settings.change_color_news(var.selected_off)
            self.main_page_settings.change_color_sunrise(var.selected_off)
            self.main_page_settings.change_color_sunset(var.selected_off)
            self.main_page_settings.change_color_hilo(var.selected_off)

    # -------------------------------- Updating Pages ------------------------------------#

    def update_page(self, cur_zone):
        if cur_zone is not None:    # need this or it'll change page like crazy
            self.change_page(self.find_page_to_change_to())

    # ---------------------------------- HELPER ----------------------------------- #
    def find_page_to_change_to(self):
        if self.current_page == Page.main:
            # Change from Main Page to Weather Page
            if self.current_zone == zone.MainPage.weather:
                return Page.weather
            # Change from Main Page to Settings
            if self.current_zone == zone.MainPage.settings:
                return Page.settings

        # Currently on Weather Page
        elif self.current_page == Page.weather:
            # Change from Weather Page to Main Page
            if self.current_zone == zone.WeatherPage.returnButton:
                return Page.main

        # Currently on Settings Page
        elif self.current_page == Page.settings:
            # Change from Settings Page to Main Page
            if self.current_zone == zone.SettingsPage.returnButton:
                return Page.main
        return None

    def change_page(self, new_page):
        if new_page is not None:    # safety check for manual mode
            # Switching to Main Page
            if new_page == Page.main:
                # Switching from Weather
                if self.current_page == Page.weather:
                    self.close_weather_page()  # todo remove previous page if weather, news, etc
                # Switching from Settings
                elif self.current_page == Page.settings:
                    self.close_settings_page()
                self.current_page = Page.main
                self.open_main_page()
                self.current_zone = zone.MainPage.none

            # Switching from Main Page

            # Switching to Weather
            elif new_page == Page.weather:  # BLANK PAGE
                self.close_main_page()
                self.current_page = Page.weather
                self.open_weather_page()
                self.current_zone = zone.WeatherPage.none
            # Switching to Settings
            elif new_page == Page.settings:
                self.close_main_page()
                self.current_page = Page.settings
                self.open_settings_page()
                self.current_zone = zone.SettingsPage.none



