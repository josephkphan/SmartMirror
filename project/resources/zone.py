from enum import Enum


# Includes the possible zones that could be selected on the main page
class MainPage(Enum):
    weather = 1
    clock = 2
    news = 3
    settings = 4
    none = -1


# Includes the possible zones that could be selected on the weather page
class Weather(Enum):
    returnButton = 4
    none = -1


class Settings(Enum):
    returnButton = 5
    none = -1