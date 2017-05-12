from project.resources import var
from webinfo import *
from cursorhandler import *
from selectionhandler import *
from mainpagewidgets.news import *
from mainpagewidgets.clock import *
from mainpagewidgets.weather import *
from generalwidgets.returnbutton import *
from generalwidgets.settingsbutton import *
from weatherpagewidgets.dailyweather import *
from weatherpagewidgets.hourlyweather import *
from weatherpagewidgets.currentweather import *
from settingwidgets.colorsettings import *
from settingwidgets.fontsettings import *
from settingwidgets.updatenow import *
from plannerwidgets.todolist import *
from plannerwidgets.eventlist import *
from transitionwidgets.startuptext import *
from transitionwidgets.powerofftext import *
from newswidgets.stock import *
from uisetup.keyboardsetup import *
from uisetup.widgetswitcher import *
from uisetup.widgetcoloring import *


# File Name: UI Handler:
# Purpose: Handles all TKinter widgets and displays them appropriately based on the given inputs from the hardware
class UIManager:
    def __init__(self, controller):
        # initializing Keys
        self.key_up, self.key_down, self.key_left, self.key_right = 0, 1, 2, 3  # todo move to var constant file
        # Handlers
        self.cursor_handler = CursorHandler()
        self.web_info = WebInfo()
        self.selection_handler = SelectionHandler()

        self.controller = controller

        # TK
        self.tk = Tk()

        # camera select mode
        self.camera_select_mode = False

        # Configuring the UI window, Creating Frames
        self.tk.configure(background='black')
        self.camera_selection_mode = False

        self.keyboard = KeyboardSetUp(self)

        # Initialize Widget Switcher #TODO move this shit
        self.widget_switcher = WidgetSwitcher(self)

        self.widget_coloring = WidgetColoring(self)

        # Creating Frames
        self.top_frame = Frame(self.tk, background='black')
        self.top_frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottom_frame = Frame(self.tk, background='black')
        self.bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=YES)

        self.left_top = Frame(self.top_frame, bg=background_color)
        self.left_top.pack(side=LEFT, anchor=N)
        self.right_top = Frame(self.top_frame, bg=background_color)
        self.right_top.pack(side=RIGHT, anchor=N)

        self.left_bottom = Frame(self.bottom_frame, bg=background_color)
        self.left_bottom.pack(side=LEFT, anchor=N)
        self.right_bottom = Frame(self.bottom_frame, bg=background_color)
        self.right_bottom.pack(side=RIGHT, anchor=N)

        self.container = Frame(self.right_top, bg=background_color)

        self.camera_selection_mode = not self.camera_selection_mode  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.camera_selection_mode)

        self.update_tk()

        # Initializing Start up and update Page - Needs to be here
        self.start_up = StartUpText(self.top_frame)
        self.power_off = PowerOffText(self.top_frame)

        self.current_zone = zone.StartUpPage.none
        self.current_page = Page.startup
        self.widget_switcher.open_startup_page()

        self.update_tk()

        # ---------------------------------- Initializing Widgets ----------------------------------- #

        # FIRST TIME OPENING MIRROR
        if not var.weather_data or not var.news_data or not var.last_updated:
            self.web_info.update()  # todo if this fails, exit program sicne you dont have any data

        # General Widgets
        self.return_button = ReturnButton(self.left_top)

        # Main Page Widgets
        self.main_weather = Weather(self.left_top)
        self.main_clock = Clock(self.right_top)
        self.main_news = News(self.bottom_frame, 3)
        self.main_settings = SettingsButton(self.bottom_frame)

        # Weather Page Widgets
        self.weather_current = CurrentWeather(self.right_top)
        self.weather_hourly = {}
        self.weather_daily = {}
        for i in range(0, 24):
            self.weather_hourly[i] = HourlyWeather(self.left_top, i)
        for i in range(0, 7):
            self.weather_daily[i] = DailyWeather(self.container, i)

        # News Page Widgets
        self.news_headlines = News(self.bottom_frame, var.news_data['number_of_headlines'])
        self.stocks = {}
        for i in range(0,len(var.stocks_list)):
            self.stocks[i] = Stock(self.right_top, var.stocks_list[i])

        # Settings Page Widgets
        self.settings_font = FontSettings(self.left_top)
        self.settings_color_scheme = ColorSettings(self.left_top)
        self.settings_update_now = UpdateNow(self.left_top, self.web_info_update, self.update_all_widgets_content)

        # To Do List Page Widgets
        self.planner_todolist = ToDoList(self.right_top)
        self.planner_event_list = EventList(self.bottom_frame)

        # Creating the Cursor window
        self.canvas = Canvas(self.left_top, width=camera_width + tk_cursor_diameter,
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
        self.on_startup()

    # ---------------------------------- UIManager Updating Functions ----------------------------------- #
    def on_startup(self):
        # Setting initial zone and page data
        last_update_time = (time.time() - var.last_updated) / 60
        # print last_update_time
        if not(last_update_time >= var.update_time and self.current_page == Page.main):
            time.sleep(3)
        else:
            self.web_info_update()
            self.update_all_widgets_content()

        self.widget_switcher.close_startup_page()
        self.current_zone = zone.MainPage.none  # Starts off on main page
        self.current_page = Page.main
        self.widget_switcher.open_main_page()

    def update_all(self, cursor):
        self.update_web_info()
        self.get_current_zone_from_cursor(cursor)
        self.update_zone()
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        self.canvas.move(self.cursor, diff_x, diff_y)
        self.circle_coord = cursor
        self.update_page(self.selection_handler.update(self.current_zone, self.camera_select_mode))
        self.update_tk()

    def update_all_manually(self):
        self.update_web_info()
        self.update_zone()
        self.update_tk()

    def update_all_joystick(self, joystick_state):
        if joystick_state == 'up':
            self.keyboard.directional_click(self.key_up)
        elif joystick_state == 'down':
            self.keyboard.directional_click(self.key_down)
        elif joystick_state == 'left':
            self.keyboard.directional_click(self.key_left)
        elif joystick_state == 'right':
            self.keyboard.directional_click(self.key_right)
        elif joystick_state == 'pressed':
            self.keyboard.enter_click()
        elif joystick_state == 'toggled':
            self.keyboard.toggle_power()

    # ---------------------------------- Web Info Updating Functions ----------------------------------- #
    def update_web_info(self):
        last_update_time = (time.time() - var.last_updated) / 60
        # print last_update_time
        if last_update_time >= var.update_time and self.current_page == Page.main:  # todo only update on main page??
            # Means its been 10 minutes since it last updated
            print "UPDATING WEB INFO. REQUESTING FROM WEB"
            self.main_clock.change_update_label_to_updating()
            self.web_info_update()
            self.update_all_widgets_content()

    def web_info_update(self):
        self.web_info.update()

    def update_all_widgets_content(self, event=None):  # todo IMPLEMENT THIS IN
        # Main Page
        self.main_news.update_now()
        self.main_weather.update_now()
        self.settings_update_now.update_now()
        self.return_button.update_now()

        # Weather Page
        for i in range(0, 7):
            self.weather_daily[i].update_now(i)  # NOTE THIS ONLY UPDATES IMAGE COLORS AND TEXT CONTENT
        for i in range(0, 24):
            self.weather_hourly[i].update_now(i)
        self.weather_current.update_now()

        # News Page
        self.news_headlines.update_now()
        for i in range(0,len(var.stocks_list)):
            self.stocks[i].update_now()

        # To Do List Page
        self.planner_todolist.update_now()
        self.planner_event_list.update_now()

    def update_all_widgets_everything(self, event=None):  # updates font, content, and image colors
        self.update_all_widgets_content()
        self.main_settings.update_now()
        self.main_clock.update_font_size()

    # ---------------------------------- TKinter Updating Functions ----------------------------------- #
    def update_tk(self):
        self.tk.update_idletasks()
        self.tk.update()

    # ---------------------------------- UI Zones Updating Functions ----------------------------------- #
    def get_current_zone_from_cursor(self, cursor):
        self.current_zone = self.cursor_handler.update_cursor(cursor, self.current_page)

    # Updates specific page's zones based on current location
    def update_zone(self):
        if self.current_page == Page.main:
            self.widget_coloring.update_zone_main_page()
        # Updating zones for Weather Page
        elif self.current_page == Page.weather:
            self.widget_coloring.update_zone_weather_page()
        # Updating Zones for Settings Page
        elif self.current_page == Page.settings:
            self.widget_coloring.update_zone_settings_page()
        elif self.current_page == Page.news:
            self.widget_coloring.update_zone_news_page()
        elif self.current_page == Page.planner:
            self.widget_coloring.update_zone_planner_page()

    # -------------------------------- Updating Current Pages ------------------------------------#
    def update_page(self, cur_zone):
        if cur_zone is not None:  # need this or it'll change page like crazy
            self.change_page(self.find_page_to_change_to())

    # ---------------------------------- HELPER ----------------------------------- #
    def find_page_to_change_to(self):
        # --- Going from Main Page to Another Page --- #

        if self.current_page == Page.main:
            # Change from Main Page to Weather Page
            if self.current_zone == zone.MainPage.weather:
                return Page.weather
            # Change from Main Page to Settings
            elif self.current_zone == zone.MainPage.settings:
                return Page.settings
            # Change from Main Page to News
            elif self.current_zone == zone.MainPage.news:
                return Page.news
            elif self.current_zone == zone.MainPage.clock:
                return Page.planner

        # --- Going back to Main Page--- #

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

        # Currently on News Page
        elif self.current_page == Page.news:
            # Change from Settings Page to Main Page
            if self.current_zone == zone.NewsPage.returnButton:
                return Page.main

        # Currently on Planner Page
        elif self.current_page == Page.planner:
            # Change from Planner Page to Main Page
            if self.current_zone == zone.PlannerPage.returnButton:
                return Page.main
        return None

    def change_page(self, new_page):
        if new_page is not None:  # safety check for manual mode
            if new_page == Page.startup:
                self.update_tk()
                self.current_page = Page.startup
                self.widget_switcher.open_startup_page()
                self.current_zone = zone.StartUpPage.none
                self.update_tk()
                self.on_startup()

            # Switching to Main Page
            if new_page == Page.main:
                # Switching from Weather
                if self.current_page == Page.weather:
                    self.widget_switcher.close_weather_page()  # todo remove previous page if weather, news, etc
                # Switching from Settings
                elif self.current_page == Page.settings:
                    self.widget_switcher.close_settings_page()
                elif self.current_page == Page.news:
                    self.widget_switcher.close_news_page()
                elif self.current_page == Page.planner:
                    self.widget_switcher.close_planner_page()
                self.current_page = Page.main
                self.widget_switcher.open_main_page()
                self.current_zone = zone.MainPage.none

            # ----------Switching from Main Page --------- #

            # Switching to Weather
            elif new_page == Page.weather:  # BLANK PAGE
                self.widget_switcher.close_main_page()
                self.current_page = Page.weather
                self.widget_switcher.open_weather_page()
                self.current_zone = zone.WeatherPage.none
            # Switching to Settings
            elif new_page == Page.settings:
                self.widget_switcher.close_main_page()
                self.current_page = Page.settings
                self.widget_switcher.open_settings_page()
                self.current_zone = zone.SettingsPage.none
            # Switching to News
            elif new_page == Page.news:
                self.widget_switcher.close_main_page()
                self.current_page = Page.news
                self.widget_switcher.open_news_page()
                self.current_zone = zone.NewsPage.none
            elif new_page == Page.planner:
                self.widget_switcher.close_main_page()
                self.current_page = Page.planner
                self.widget_switcher.open_planner_page()
                self.current_zone = zone.PlannerPage.none

            elif new_page == Page.blank:
                if self.current_page == Page.main:
                    self.widget_switcher.close_main_page()
                elif self.current_page == Page.weather:
                    self.widget_switcher.close_weather_page()
                elif self.current_page == Page.settings:
                    self.widget_switcher.close_settings_page()
                elif self.current_page == Page.planner:
                    self.widget_switcher.close_planner_page()
                elif self.current_page == Page.news:
                    self.widget_switcher.close_news_page()
                self.current_page = Page.blank
                self.right_top.pack_forget()
                self.left_top.pack_forget()
                self.right_bottom.pack_forget()
                self.left_bottom.pack_forget()
                self.widget_switcher.open_power_off_page()
                self.update_tk()
                time.sleep(3)
                self.widget_switcher.close_power_off_page()
                self.controller.is_mirror_on = False

