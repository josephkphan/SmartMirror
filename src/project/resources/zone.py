from enum import Enum


# Includes the possible zones that could be selected on the main page
class MainPageZone(Enum):
    weather = 1
    clock = 2
    news = 3
    none = -1


# Includes the possible zones that could be selected on the weather page
class WeatherZone(Enum):
    returnButton = 4
    none = -1
