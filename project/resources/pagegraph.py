from project.resources.zone import *

# This file contains Graphs used for the manual mode to know which zone to switch to given a
# up down left right Command
# NOTE the key is the zone and the result is an array of the corresponding zone in this format
# Current Node' : [ UP, DOWN LEFT RIGHT]

# Main Page Graph
Main = {
    MainPage.clock: [MainPage.clock, MainPage.settings, MainPage.weather, MainPage.clock],
    MainPage.settings: [MainPage.clock, MainPage.settings, MainPage.news, MainPage.settings],
    MainPage.weather: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock],
    MainPage.news: [MainPage.weather, MainPage.news, MainPage.news, MainPage.settings],
    MainPage.none: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock]
}

# Weather Page Graph
Weather = {
    WeatherPage.none: [WeatherPage.returnButton, WeatherPage.returnButton, WeatherPage.returnButton,
                       WeatherPage.returnButton],
    WeatherPage.returnButton: [WeatherPage.none, WeatherPage.none, WeatherPage.none, WeatherPage.none]
}

# Settings Page Graph
Settings = {
    SettingsPage.none: [SettingsPage.returnButton, SettingsPage.returnButton, SettingsPage.returnButton,
                        SettingsPage.returnButton],
    SettingsPage.returnButton: [SettingsPage.returnButton, SettingsPage.main_page_stocks, SettingsPage.main_page_news,
                                SettingsPage.none],
    SettingsPage.main_page_stocks: [SettingsPage.returnButton, SettingsPage.main_page_news, SettingsPage.none,
                                    SettingsPage.none],
    SettingsPage.main_page_news: [SettingsPage.main_page_stocks, SettingsPage.main_page_sunrise, SettingsPage.none,
                                  SettingsPage.none],
    SettingsPage.main_page_sunrise: [SettingsPage.main_page_news, SettingsPage.main_page_sunset, SettingsPage.none,
                                     SettingsPage.none],
    SettingsPage.main_page_sunset: [SettingsPage.main_page_sunrise, SettingsPage.main_page_high_low, SettingsPage.none,
                                    SettingsPage.none],
    SettingsPage.main_page_high_low: [SettingsPage.main_page_sunset, SettingsPage.none, SettingsPage.none,
                                      SettingsPage.none]

}
