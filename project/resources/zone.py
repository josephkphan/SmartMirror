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
    stocks = 3


class PlannerPage(Enum):
    none = 0
    returnButton = 1
    todolist = 2
    eventlist = 3

    todo0 = 10
    todo1 = 11
    todo2 = 12
    todo3 = 13
    todo4 = 14

    event0 = 20
    event1 = 21
    event2 = 22
    event3 = 23
    event4 = 24
    event5 = 25
    event6 = 26
    event7 = 27
    event8 = 28
    event9 = 29



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