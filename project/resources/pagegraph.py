from project.resources.zone import *

# Format    'Current Node' : [ UP, DOWN LEFT RIGHT]
Main = {
    MainPage.clock: [MainPage.clock, MainPage.settings, MainPage.weather, MainPage.clock],
    MainPage.settings: [MainPage.clock, MainPage.settings, MainPage.news, MainPage.settings],
    MainPage.weather: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock],
    MainPage.news: [MainPage.weather, MainPage.news, MainPage.news, MainPage.settings],
    MainPage.none: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock]
}

Weather = {
    WeatherPage.none: [WeatherPage.returnButton, WeatherPage.returnButton, WeatherPage.returnButton,
                       WeatherPage.returnButton],
    WeatherPage.returnButton: [WeatherPage.none, WeatherPage.none, WeatherPage.none, WeatherPage.none]
}

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
