from enum import Enum

# "ZONE" is a an area that can be "turned yellow" or hovered over via manual or cursor
# none should always be 0 (no reason, just for consistency)


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


# Includes the possible zones that could be selected on the settings page
class SettingsPage(Enum):
    none = 0
    returnButton = 1
    # Main page zones
    main_page_sunset = 2
    main_page_sunrise = 3
    main_page_high_low = 4
    main_page_stocks = 5
    main_page_news = 6

    # Color Schemes
    yellow = 7
    blue = 8
    pink = 9
    red = 10
    green=11