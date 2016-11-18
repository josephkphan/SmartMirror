from enum import Enum


# Includes the possible zones that could be selected on the main page
class MainPage(Enum):
    none = 0
    weather = 1
    clock = 2
    news = 3
    settings = 4


# Includes the possible zones that could be selected on the weather page
class WeatherPage(Enum):
    none = 0
    returnButton = 1


class SettingsPage(Enum):
    none = 0
    returnButton = 1
    main_page_sunset = 2
    main_page_sunrise = 3
    main_page_high_low = 4
    main_page_stocks = 5
    main_page_news = 6
