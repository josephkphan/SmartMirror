from project.resources.zone import *
from enum import Enum


class Key(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    ENTER = 4


# Format    'Current Node' : [ UP, DOWN LEFT RIGHT]
MainPageGraph = {
    MainPage.clock: [MainPage.clock, MainPage.settings, MainPage.weather, MainPage.clock],
    MainPage.setting: [MainPage.clock, MainPage.settings, MainPage.news, MainPage.settings],
    MainPage.weather: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock],
    MainPage.news: [MainPage.weather, MainPage.news, MainPage.news, MainPage.settings]
}
