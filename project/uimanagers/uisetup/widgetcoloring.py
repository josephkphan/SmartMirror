from Tkinter import *
from project.resources import var, zone
class WidgetColoring:
     # ---------------------------------- Main Page Zone Helper Functions ----------------------------------- #
    # Updates all 4 zones on the main page
    def __init__(self, uiHander):
        self.uiHandler = uiHander

    def update_zone_main_page(self):
        self.main_page_all_off()
        # Weather Zone Selected
        if self.uiHandler.current_zone == zone.MainPage.weather:
            self.uiHandler.main_weather.change_color_all(var.selected_on)
        # News Zone Selected
        elif self.uiHandler.current_zone == zone.MainPage.news:
            self.uiHandler.main_news.change_color_all(var.selected_on)
        # Clock Zone Selected
        elif self.uiHandler.current_zone == zone.MainPage.clock:
            self.uiHandler.main_clock.change_color_all(var.selected_on)
        # Settings Zone Selected
        elif self.uiHandler.current_zone == zone.MainPage.settings:
            self.uiHandler.main_settings.change_color_setting(var.selected_on)

    # De-selects all 4 zones on the main page
    def main_page_all_off(self):
        self.uiHandler.main_weather.change_color_all(var.selected_off)
        self.uiHandler.main_news.change_color_all(var.selected_off)
        self.uiHandler.main_clock.change_color_all(var.selected_off)
        self.uiHandler.main_settings.change_color_setting(var.selected_off)

    # ---------------------------------- Weather Page Zone Helper Functions ----------------------------------- #
    # Updates all 4 zones on the weather page
    def update_zone_weather_page(self):
        self.weather_page_all_off()
        # Return Button Selected
        if self.uiHandler.current_zone == zone.WeatherPage.returnButton:
            self.uiHandler.return_button.change_color_all(var.selected_on)
        elif self.uiHandler.current_zone == zone.WeatherPage.hourly_weather:
            for i in range(0, 24):
                self.uiHandler.weather_hourly[i].change_color_all(var.selected_on)
        elif self.uiHandler.current_zone == zone.WeatherPage.current_weather:
            self.uiHandler.weather_current.change_color_all(var.selected_on)
        elif self.uiHandler.current_zone == zone.WeatherPage.daily_weather:
            for i in range(0, 7):
                self.uiHandler.weather_daily[i].change_color_all(var.selected_on)

    # De-selects all 4 zones on the weather page
    def weather_page_all_off(self):
        self.uiHandler.return_button.change_color_all(var.selected_off)
        for i in range(0, 7):
            self.uiHandler.weather_daily[i].change_color_all(var.selected_off)
        self.uiHandler.weather_current.change_color_all(var.selected_off)
        for i in range(0, 24):
            self.uiHandler.weather_hourly[i].change_color_all(var.selected_off)

    # ---------------------------------- News Page Zone Helper Functions ----------------------------------- #
    # Updates all zones on the news page
    def update_zone_news_page(self):
        self.news_page_all_off()
        # Return Button Selected
        if self.uiHandler.current_zone == zone.NewsPage.returnButton:
            self.uiHandler.return_button.change_color_all(var.selected_on)
        elif self.uiHandler.current_zone == zone.NewsPage.headlines:
            self.uiHandler.news_headlines.change_color_all(var.selected_on)

    def news_page_all_off(self):
        self.uiHandler.return_button.change_color_all(var.selected_off)
        self.uiHandler.news_headlines.change_color_all(var.selected_off)

    # ---------------------------------- Planner Page Zone Helper Functions ----------------------------------- #
    def update_zone_planner_page(self):
        self.planner_page_all_off()
        # Return Button Selected
        if self.uiHandler.current_zone == zone.PlannerPage.returnButton:
            self.uiHandler.return_button.change_color_all(var.selected_on)

    def planner_page_all_off(self):
        self.uiHandler.return_button.change_color_all(var.selected_off)

    # ---------------------------------- Settings Page Zone Helper Functions ----------------------------------- #
    # Updates all zones on the weather page
    def update_zone_settings_page(self):
        # Return Button Selected
        self.settings_page_all_off()
        if self.uiHandler.current_zone == zone.SettingsPage.returnButton:
            self.uiHandler.return_button.change_color_all(var.selected_on)
        # Update now Setting
        elif self.uiHandler.current_zone == zone.SettingsPage.update_now:
            self.uiHandler.settings_update_now.change_color_update_now(var.selected_on)
        # Color Scheme Settings
        elif self.uiHandler.current_zone == zone.SettingsPage.blue:
            self.uiHandler.settings_color_scheme.change_color_blue(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.green:
            self.uiHandler.settings_color_scheme.change_color_green(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.orange:
            self.uiHandler.settings_color_scheme.change_color_orange(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.pink:
            self.uiHandler.settings_color_scheme.change_color_pink(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.purple:
            self.uiHandler.settings_color_scheme.change_color_purple(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.red:
            self.uiHandler.settings_color_scheme.change_color_red(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.yellow:
            self.uiHandler.settings_color_scheme.change_color_yellow(var.selected_on)

        # Font Settings
        elif self.uiHandler.current_zone == zone.SettingsPage.small:
            self.uiHandler.settings_font.change_color_small(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.medium:
            self.uiHandler.settings_font.change_color_medium(var.selected_on)
        elif self.uiHandler.current_zone == zone.SettingsPage.large:
            self.uiHandler.settings_font.change_color_large(var.selected_on)

    # De-selects all zones on the settings page
    def settings_page_all_off(self):
        self.uiHandler.return_button.change_color_all(var.selected_off)
        # self.main_page_settings.change_all_label_colors(var.selected_off)
        self.uiHandler.settings_color_scheme.change_all_label_colors(var.selected_off)
        self.uiHandler.settings_font.change_all_label_colors(var.selected_off)
        self.uiHandler.settings_update_now.change_color_update_now(var.selected_off)