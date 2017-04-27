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
    hourly_weather = 2
    current_weather = 3
    daily_weather = 4


class NewsPage(Enum):
    none = 0
    returnButton = 1
    headlines = 2


class PlannerPage(Enum):
    none = 0
    returnButton = 1
    todolist = 2
    # todo0 = 3
    # todo1 = 4
    # todo2 = 5
    # todo3 = 6
    # todo4 = 7


# Includes the possible zones that could be selected on the settings page
class SettingsPage(Enum):
    none = 0
    returnButton = 1
    # Main page zones
    main_page_weather = 2
    main_page_time = 3
    main_page_news = 4
    main_page_sports = 5
    main_page_stocks = 6

    # Color Schemes
    blue = 7
    green = 8
    orange = 9
    pink = 10
    purple = 11
    red = 12
    yellow = 13

    # Font Sizes
    small = 14
    medium = 15
    large = 16

    update_now = 17