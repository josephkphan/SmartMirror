from enum import Enum

# File Name page.py
# An Enum of all the possible pages for UI Manager


class Page(Enum):
    main = 1
    clock = 2
    weather = 3
    news = 4


class MainPageZone(Enum):
    weather = 1
    clock = 2
    news = 3


class WeatherZone(Enum):
    returnButton = 4
