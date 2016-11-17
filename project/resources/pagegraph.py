from project.resources.zone import *

# Format    'Current Node' : [ UP, DOWN LEFT RIGHT]
Main = {
    MainPage.clock: [MainPage.clock, MainPage.settings, MainPage.weather, MainPage.clock],
    MainPage.settings: [MainPage.clock, MainPage.settings, MainPage.news, MainPage.settings],
    MainPage.weather: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock],
    MainPage.news: [MainPage.weather, MainPage.news, MainPage.news, MainPage.settings],
    MainPage.none: [MainPage.weather,MainPage.news, MainPage.news, MainPage.clock]
}

# Weather = {
#
#
# }