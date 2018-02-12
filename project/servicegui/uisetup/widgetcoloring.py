from Tkinter import *
from resources import var, zone
class WidgetColoring:
     # ---------------------------------- Main Page Zone Helper Functions ----------------------------------- #
    # Updates all 4 zones on the main page
    def __init__(self, ui_handler):
        self.ui_handler = ui_handler

    def update_zone_main_page(self):
        self.main_page_all_off()
        # Weather Zone Selected
        if self.ui_handler.current_zone == zone.MainPage.weather:
            self.ui_handler.main_weather.change_color_all(var.selected_on)
        # News Zone Selected
        elif self.ui_handler.current_zone == zone.MainPage.news:
            self.ui_handler.main_news.change_color_all(var.selected_on)
        # Clock Zone Selected
        elif self.ui_handler.current_zone == zone.MainPage.clock:
            self.ui_handler.main_clock.change_color_all(var.selected_on)
        # Settings Zone Selected
        elif self.ui_handler.current_zone == zone.MainPage.settings:
            self.ui_handler.main_settings.change_color_setting(var.selected_on)

    # De-selects all 4 zones on the main page
    def main_page_all_off(self):
        self.ui_handler.main_weather.change_color_all(var.selected_off)
        self.ui_handler.main_news.change_color_all(var.selected_off)
        self.ui_handler.main_clock.change_color_all(var.selected_off)
        self.ui_handler.main_settings.change_color_setting(var.selected_off)

    # ---------------------------------- Weather Page Zone Helper Functions ----------------------------------- #
    # Updates all 4 zones on the weather page
    def update_zone_weather_page(self):
        self.weather_page_all_off()
        # Return Button Selected
        if self.ui_handler.current_zone == zone.WeatherPage.returnButton:
            self.ui_handler.return_button.change_color_all(var.selected_on)
        elif self.ui_handler.current_zone == zone.WeatherPage.hourly_weather:
            for i in range(0, 24):
                self.ui_handler.weather_hourly[i].change_color_all(var.selected_on)
        elif self.ui_handler.current_zone == zone.WeatherPage.current_weather:
            self.ui_handler.weather_current.change_color_all(var.selected_on)
        elif self.ui_handler.current_zone == zone.WeatherPage.daily_weather:
            for i in range(0, 7):
                self.ui_handler.weather_daily[i].change_color_all(var.selected_on)

    # De-selects all 4 zones on the weather page
    def weather_page_all_off(self):
        self.ui_handler.return_button.change_color_all(var.selected_off)
        for i in range(0, 7):
            self.ui_handler.weather_daily[i].change_color_all(var.selected_off)
        self.ui_handler.weather_current.change_color_all(var.selected_off)
        for i in range(0, 24):
            self.ui_handler.weather_hourly[i].change_color_all(var.selected_off)

    # ---------------------------------- News Page Zone Helper Functions ----------------------------------- #
    # Updates all zones on the news page
    def update_zone_news_page(self):
        self.news_page_all_off()
        # Return Button Selected
        if self.ui_handler.current_zone == zone.NewsPage.returnButton:
            self.ui_handler.return_button.change_color_all(var.selected_on)
        elif self.ui_handler.current_zone == zone.NewsPage.headlines:
            self.ui_handler.news_headlines.change_color_all(var.selected_on)
        elif self.ui_handler.current_zone == zone.NewsPage.stocks_bottom or self.ui_handler.current_zone == zone.NewsPage.stocks_top:
            for i in range(0, len(var.stocks_list)):
                self.ui_handler.stocks[i].change_color_all(var.selected_on)

    def news_page_all_off(self):
        self.ui_handler.return_button.change_color_all(var.selected_off)
        self.ui_handler.news_headlines.change_color_all(var.selected_off)
        for i in range(0, len(var.stocks_list)):
                self.ui_handler.stocks[i].change_color_all(var.selected_off)

    # ---------------------------------- Planner Page Zone Helper Functions ----------------------------------- #
    def update_zone_planner_page(self):
        self.planner_page_all_off()
        # Return Button Selected
        if self.ui_handler.current_zone == zone.PlannerPage.returnButton:
            self.ui_handler.return_button.change_color_all(var.selected_on)
        elif self.ui_handler.current_zone == zone.PlannerPage.todolist:
            self.ui_handler.planner_todolist.change_color_all(var.selected_on)
        #     self.ui_handler.planner_todolist.change_color_todolist(var.selected_on, self.ui_handler.current_zone) # TODO FIX THIS PIECE OF SHIT
        # elif self.ui_handler.current_zone == zone.PlannerPage.todo0:
        #     self.ui_handler.planner_todolist.change_color_todolist(var.selected_on, zone.PlannerPage.todo0)
        # elif self.ui_handler.current_zone == zone.PlannerPage.todo1:
        #     self.ui_handler.planner_todolist.change_color_todolist(var.selected_on, zone.PlannerPage.todo1)
        # elif self.ui_handler.current_zone == zone.PlannerPage.todo2:
        #     self.ui_handler.planner_todolist.change_color_todolist(var.selected_on, zone.PlannerPage.todo2)
        # elif self.ui_handler.current_zone == zone.PlannerPage.todo3:
        #     self.ui_handler.planner_todolist.change_color_todolist(var.selected_on, zone.PlannerPage.todo3)
        # elif self.ui_handler.current_zone == zone.PlannerPage.todo4:
        #     self.ui_handler.planner_todolist.change_color_todolist(var.selected_on, zone.PlannerPage.todo4)

        elif self.ui_handler.current_zone == zone.PlannerPage.eventlist_left or self.ui_handler.current_zone == zone.PlannerPage.eventlist_right:
            self.ui_handler.planner_event_list.change_color_all(var.selected_on)


    def planner_page_all_off(self):
        self.ui_handler.return_button.change_color_all(var.selected_off)
        self.ui_handler.planner_todolist.change_color_all(var.selected_off)
        self.ui_handler.planner_event_list.change_color_all(var.selected_off)

    # ---------------------------------- Settings Page Zone Helper Functions ----------------------------------- #
    # Updates all zones on the weather page
    def update_zone_settings_page(self):
        # Return Button Selected
        self.settings_page_all_off()
        if self.ui_handler.current_zone == zone.SettingsPage.returnButton:
            self.ui_handler.return_button.change_color_all(var.selected_on)
        # Update now Setting
        elif self.ui_handler.current_zone == zone.SettingsPage.update_now:
            self.ui_handler.settings_update_now.change_color_update_now(var.selected_on)
        # Color Scheme Settings
        elif self.ui_handler.current_zone == zone.SettingsPage.blue:
            self.ui_handler.settings_color_scheme.change_color_blue(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.green:
            self.ui_handler.settings_color_scheme.change_color_green(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.orange:
            self.ui_handler.settings_color_scheme.change_color_orange(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.pink:
            self.ui_handler.settings_color_scheme.change_color_pink(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.purple:
            self.ui_handler.settings_color_scheme.change_color_purple(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.red:
            self.ui_handler.settings_color_scheme.change_color_red(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.yellow:
            self.ui_handler.settings_color_scheme.change_color_yellow(var.selected_on)

        # Font Settings
        elif self.ui_handler.current_zone == zone.SettingsPage.small:
            self.ui_handler.settings_font.change_color_small(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.medium:
            self.ui_handler.settings_font.change_color_medium(var.selected_on)
        elif self.ui_handler.current_zone == zone.SettingsPage.large:
            self.ui_handler.settings_font.change_color_large(var.selected_on)

    # De-selects all zones on the settings page
    def settings_page_all_off(self):
        self.ui_handler.return_button.change_color_all(var.selected_off)
        # self.main_page_settings.change_all_label_colors(var.selected_off)
        self.ui_handler.settings_color_scheme.change_all_label_colors(var.selected_off)
        self.ui_handler.settings_font.change_all_label_colors(var.selected_off)
        self.ui_handler.settings_update_now.change_color_update_now(var.selected_off)