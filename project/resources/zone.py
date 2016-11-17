from enum import Enum


# Includes the possible zones that could be selected on the main page
class MainPage(Enum):
    none = 0
    weather = 1
    clock = 2
    news = 3
    settings = 4


# Includes the possible zones that could be selected on the weather page
class Weather(Enum):
    none = 0
    returnButton = 4


class Settings(Enum):
    none = 0
    returnButton = 5
