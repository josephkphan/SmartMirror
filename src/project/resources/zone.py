from enum import Enum


class MainPageZone(Enum):
    weather = 1
    clock = 2
    news = 3
    none = -1


class WeatherZone(Enum):
    returnButton = 4
    none = -1
