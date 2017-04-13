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
from project.resources import zone, pagegraph, var, varloader
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

        # initializing Keys
        self.key_up, self.key_down, self.key_left, self.key_right = 0, 1, 2, 3

        # camera select mode
        self.camera_select_mode = False

        # Configuring the UI window, Creating Frames
        self.tk.configure(background='black')
        self.camera_selection_mode = False
        self.tk.bind("<Tab>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk.bind("<Left>", self.left_click)
        self.tk.bind("<Right>", self.right_click)
        self.tk.bind("<Up>", self.up_click)
        self.tk.bind("<Down>", self.down_click)
        self.tk.bind("<BackSpace>", self.enter_click)
        self.tk.bind("<Control_L>", self.toggle_manual_mode)
        self.tk.bind("<Shift_L>", self.toggle_select_mode_for_camera)
        self.tk.bind("<Control_R>", self.toggle_power)

        # FIRST TIME OPENING MIRROR
        if not var.saved_data:
            self.web_info.update()  # todo if this fails, exit program sicne you dont have any data

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



        # ---------------------------------- Initializing Widgets ----------------------------------- #
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
        self.news_headlines = News(self.bottom_frame, var.saved_data['news_number_of_headlines'])

        # Settings Page Widgets
        self.settings_font = FontSettings(self.left_top)
        self.settings_color_scheme = ColorSettings(self.left_top)
        self.settings_update_now = UpdateNow(self.left_top, self.web_info_update, self.update_all_widgets_content)

        # To Do List Page Widgets
        self.planner_todolist = ToDoList(self.right_top)

        # Creating the Cursor window
        self.canvas = Canvas(self.left_top, width=camera_width + tk_cursor_diameter,
                             height=camera_height + tk_cursor_diameter, background='black')
        self.circle_coord = (0, 0)
        self.circle_diameter = tk_cursor_diameter  # todo scale the cursor to match screen size
        self.cursor = self.canvas.create_oval(0, 0, tk_cursor_diameter, tk_cursor_diameter,
                                              fill="blue", outline="#DDD", width=tk_cursor_outline_thickness)

        # todo make a bunch of premade lines and turn them on or off depending on which page it's on
        # @thomas Nguyen

        # Vertical line
        self.line1 = self.canvas.create_line((camera_width / 2 + tk_cursor_diameter / 2, 0),
                                             (camera_width / 2 + tk_cursor_diameter / 2,
                                              camera_height + tk_cursor_diameter), fill="green")
        # Horizontal line
        self.line2 = self.canvas.create_line((0, camera_height / 2 + tk_cursor_diameter / 2),
                                             (camera_width + tk_cursor_diameter,
                                              camera_height / 2 + tk_cursor_diameter / 2), fill="green")

        # Setting initial zone and page data
        self.current_zone = zone.MainPage.none  # Starts off on main page
        self.current_page = Page.main
        self.open_main_page()



    # ---------------------------------- Key Binding Functions ----------------------------------- #
    def toggle_fullscreen(self, event=None):
        self.camera_selection_mode = not self.camera_selection_mode  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.camera_selection_mode)
        return "break"

    def end_fullscreen(self, event=None):
        self.camera_selection_mode = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def toggle_power(self, event=None):
        if self.current_page != Page.blank:
            self.change_page(Page.blank)
        else:
            self.change_page(Page.main)



    # ---------------------------------- Manual Mode Functions ----------------------------------- #
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

    def directional_click(self, key_click):
        if self.current_page == Page.main:
            self.current_zone = pagegraph.Main[self.current_zone][key_click]
        elif self.current_page == Page.weather:
            self.current_zone = pagegraph.Weather[self.current_zone][key_click]
        elif self.current_page == Page.settings:
            self.current_zone = pagegraph.Settings[self.current_zone][key_click]
        elif self.current_page == Page.news:
            self.current_zone = pagegraph.News[self.current_zone][key_click]
        elif self.current_page == Page.planner:
            self.current_zone = pagegraph.Planner[self.current_zone][key_click]
        return "break"

    def enter_click(self, event=None):
        print "Enter CLICK HAPPENED"
        self.change_page(self.find_page_to_change_to())
        if self.current_page == Page.settings:
            # self.main_page_settings.change_a_setting(self.current_zone)
            self.settings_color_scheme.change_a_setting(self.current_zone, self.settings_font)
            self.settings_font.change_a_setting(self.current_zone, self.return_button, self.settings_color_scheme)
            self.settings_update_now.update_smart_mirror(self.current_zone)
            self.update_all_widgets_everything()
        return "break"

    def toggle_manual_mode(self, event=None):
        print "Enter CONTROL HAPPENED"
        varloader.change_other_data('manual_mode', not var.other_data['manual_mode'])
        # todo FINISH THIS

    def toggle_select_mode_for_camera(self, event=None):
        print  "toggling select mode for camera"
        self.camera_select_mode = not self.camera_select_mode



    # ---------------------------------- UI Functions ----------------------------------- #
    def open_main_page(self):
        self.main_weather.pack(side=TOP, anchor=W, padx=50, pady=50)
        self.main_clock.pack(side=RIGHT, anchor=N, padx=50, pady=50)
        self.main_news.pack(side=LEFT, anchor=S, padx=50, pady=50)
        self.main_settings.pack(side=RIGHT, anchor=S, padx=50, pady=50)
        # self.canvas.pack(side=TOP, anchor=W, padx=50)

    def close_main_page(self):
        self.main_weather.pack_forget()
        self.main_clock.pack_forget()
        self.main_news.pack_forget()
        self.main_settings.pack_forget()
        # self.canvas.pack_forget()



    # ---------------------------------- News Page Functions ----------------------------------- #
    def open_news_page(self):
        self.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)
        self.news_headlines.pack(side=BOTTOM, anchor=S, padx=50, pady=50)

    def close_news_page(self):
        self.news_headlines.pack_forget()
        self.return_button.pack_forget()



    # ---------------------------------- Planner Page Functions----------------------------------- #
    def open_planner_page(self):
        self.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)

    def close_planner_page(self):
        self.return_button.pack_forget()



    # ---------------------------------- Weather Page Functions----------------------------------- #
    def open_weather_page(self):
        self.return_button.pack(side=TOP, anchor=NW, padx=15, pady=15)
        for i in range(0, 24):
            self.weather_hourly[i].pack(side=TOP, anchor=W, padx=5, pady=5)
        self.weather_current.pack(side=TOP, anchor=N, padx=50, pady=50)

        self.container.pack(side=TOP, anchor=N)
        for i in range(0, 7):
            self.weather_daily[i].pack(side=LEFT, anchor=N, padx=0, pady=0)

    def close_weather_page(self):
        self.return_button.pack_forget()
        self.weather_current.pack_forget()
        for i in range(0, 7):
            self.weather_daily[i].pack_forget()

        for i in range(0, 24):
            self.weather_hourly[i].pack_forget()
        self.container.pack_forget()



    # ---------------------------------- Settings Page Functions ----------------------------------- #
    def open_settings_page(self):
        self.return_button.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.settings_update_now.pack(side=TOP, anchor=W, padx=50, pady=15)
        self.settings_color_scheme.pack(side=TOP, anchor=W, padx=50, pady=15)
        self.settings_font.pack(side=TOP, anchor=W, padx=50, pady=15)

    def close_settings_page(self):
        self.return_button.pack_forget()
        self.settings_color_scheme.pack_forget()
        self.settings_font.pack_forget()
        self.settings_update_now.pack_forget()



    # ---------------------------------- Planner Page Functions ----------------------------------- #
    def open_planner_page(self):
        self.return_button.pack(side=TOP, anchor=W, padx=15, pady=15)
        self.planner_todolist.pack(side=TOP, anchor=W, padx=50, pady=50)

    def close_planner_page(self):
        self.return_button.pack_forget()
        self.planner_todolist.pack_forget()



    # ---------------------------------- UIManager Updating Functions ----------------------------------- #
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
        if (joystick_state == 'up'):
            self.directional_click(self.key_up)
        elif (joystick_state == 'down'):
            self.directional_click(self.key_down)
        elif (joystick_state == 'left'):
            self.directional_click(self.key_left)
        elif (joystick_state == 'right'):
            self.directional_click(self.key_right)
        elif (joystick_state == 'pressed'):
            self.enter_click()
        elif (joystick_state == 'toggled'):
            self.toggle_power()



    # ---------------------------------- Web Info Updating Functions ----------------------------------- #
    def update_web_info(self):
        last_update_time = (time.time() - var.saved_data['last_updated']) / 60
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

        # To Do List Page
        self.planner_todolist.update_now()

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
            self.update_zone_main_page()
        # Updating zones for Weather Page
        elif self.current_page == Page.weather:
            self.update_zone_weather_page()
        # Updating Zones for Settings Page
        elif self.current_page == Page.settings:
            self.update_zone_settings_page()
        elif self.current_page == Page.news:
            self.update_zone_news_page()
        elif self.current_page == Page.planner:
            self.update_zone_planner_page()



    # ---------------------------------- Main Page Zone Helper Functions ----------------------------------- #
    # Updates all 4 zones on the main page
    def update_zone_main_page(self):
        self.main_page_all_off()
        # Weather Zone Selected
        if self.current_zone == zone.MainPage.weather:
            self.main_weather.change_color_all(var.selected_on)
        # News Zone Selected
        elif self.current_zone == zone.MainPage.news:
            self.main_news.change_color_all(var.selected_on)
        # Clock Zone Selected
        elif self.current_zone == zone.MainPage.clock:
            self.main_clock.change_color_all(var.selected_on)
        # Settings Zone Selected
        elif self.current_zone == zone.MainPage.settings:
            self.main_settings.change_color_setting(var.selected_on)

    # De-selects all 4 zones on the main page
    def main_page_all_off(self):
        self.main_weather.change_color_all(var.selected_off)
        self.main_news.change_color_all(var.selected_off)
        self.main_clock.change_color_all(var.selected_off)
        self.main_settings.change_color_setting(var.selected_off)



    # ---------------------------------- Weather Page Zone Helper Functions ----------------------------------- #
    # Updates all 4 zones on the weather page
    def update_zone_weather_page(self):
        self.weather_page_all_off()
        # Return Button Selected
        if self.current_zone == zone.WeatherPage.returnButton:
            self.return_button.change_color_all(var.selected_on)
        elif self.current_zone == zone.WeatherPage.hourly_weather:
            for i in range(0, 24):
                self.weather_hourly[i].change_color_all(var.selected_on)
        elif self.current_zone == zone.WeatherPage.current_weather:
            self.weather_current.change_color_all(var.selected_on)
        elif self.current_zone == zone.WeatherPage.daily_weather:
            for i in range(0, 7):
                self.weather_daily[i].change_color_all(var.selected_on)

    # De-selects all 4 zones on the weather page
    def weather_page_all_off(self):
        self.return_button.change_color_all(var.selected_off)
        for i in range(0, 7):
            self.weather_daily[i].change_color_all(var.selected_off)
        self.weather_current.change_color_all(var.selected_off)
        for i in range(0, 24):
            self.weather_hourly[i].change_color_all(var.selected_off)



    # ---------------------------------- News Page Zone Helper Functions ----------------------------------- #
    # Updates all zones on the news page
    def update_zone_news_page(self):
        self.news_page_all_off()
        # Return Button Selected
        if self.current_zone == zone.NewsPage.returnButton:
            self.return_button.change_color_all(var.selected_on)
        elif self.current_zone == zone.NewsPage.headlines:
            self.news_headlines.change_color_all(var.selected_on)

    def news_page_all_off(self):
        self.return_button.change_color_all(var.selected_off)
        self.news_headlines.change_color_all(var.selected_off)



    # ---------------------------------- Planner Page Zone Helper Functions ----------------------------------- #
    def update_zone_planner_page(self):
        self.planner_page_all_off()
        # Return Button Selected
        if self.current_zone == zone.PlannerPage.returnButton:
            self.return_button.change_color_all(var.selected_on)

    def planner_page_all_off(self):
        self.return_button.change_color_all(var.selected_off)



    # ---------------------------------- Settings Page Zone Helper Functions ----------------------------------- #
    # Updates all zones on the weather page
    def update_zone_settings_page(self):
        # Return Button Selected
        self.settings_page_all_off()
        if self.current_zone == zone.SettingsPage.returnButton:
            self.return_button.change_color_all(var.selected_on)
        # Update now Setting
        elif self.current_zone == zone.SettingsPage.update_now:
            self.settings_update_now.change_color_update_now(var.selected_on)
        # Color Scheme Settings
        elif self.current_zone == zone.SettingsPage.blue:
            self.settings_color_scheme.change_color_blue(var.selected_on)
        elif self.current_zone == zone.SettingsPage.green:
            self.settings_color_scheme.change_color_green(var.selected_on)
        elif self.current_zone == zone.SettingsPage.orange:
            self.settings_color_scheme.change_color_orange(var.selected_on)
        elif self.current_zone == zone.SettingsPage.pink:
            self.settings_color_scheme.change_color_pink(var.selected_on)
        elif self.current_zone == zone.SettingsPage.purple:
            self.settings_color_scheme.change_color_purple(var.selected_on)
        elif self.current_zone == zone.SettingsPage.red:
            self.settings_color_scheme.change_color_red(var.selected_on)
        elif self.current_zone == zone.SettingsPage.yellow:
            self.settings_color_scheme.change_color_yellow(var.selected_on)

        # Font Settings
        elif self.current_zone == zone.SettingsPage.small:
            self.settings_font.change_color_small(var.selected_on)
        elif self.current_zone == zone.SettingsPage.medium:
            self.settings_font.change_color_medium(var.selected_on)
        elif self.current_zone == zone.SettingsPage.large:
            self.settings_font.change_color_large(var.selected_on)

    # De-selects all zones on the settings page
    def settings_page_all_off(self):
        self.return_button.change_color_all(var.selected_off)
        # self.main_page_settings.change_all_label_colors(var.selected_off)
        self.settings_color_scheme.change_all_label_colors(var.selected_off)
        self.settings_font.change_all_label_colors(var.selected_off)
        self.settings_update_now.change_color_update_now(var.selected_off)



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
            # Switching to Main Page
            if new_page == Page.main:
                # Switching from Weather
                if self.current_page == Page.weather:
                    self.close_weather_page()  # todo remove previous page if weather, news, etc
                # Switching from Settings
                elif self.current_page == Page.settings:
                    self.close_settings_page()
                elif self.current_page == Page.news:
                    self.close_news_page()
                elif self.current_page == Page.planner:
                    self.close_planner_page()
                self.current_page = Page.main
                self.open_main_page()
                self.current_zone = zone.MainPage.none

            # ----------Switching from Main Page --------- #

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
            # Switching to News
            elif new_page == Page.news:
                self.close_main_page()
                self.current_page = Page.news
                self.open_news_page()
                self.current_zone = zone.NewsPage.none
            elif new_page == Page.planner:
                self.close_main_page()
                self.current_page = Page.planner
                self.open_planner_page()
                self.current_zone = zone.PlannerPage.none

            elif new_page == Page.blank:
                if self.current_page == Page.main:
                    self.close_main_page()
                elif self.current_page == Page.weather:
                    self.close_weather_page()
                elif self.current_page == Page.settings:
                    self.close_settings_page()
                elif self.current_page == Page.planner:
                    self.close_planner_page()
                elif self.current_page == Page.news:
                    self.close_news_page()
                self.current_page = Page.blank
