from project.resources.zone import *

# This file contains Graphs used for the manual mode to know which zone to switch to given a
# up down left right Command
# NOTE the key is the zone and the result is an array of the corresponding zone in this format
# Current Node' : [ UP, DOWN LEFT RIGHT]

# Main Page Graph
Main = {
    MainPage.clock: [MainPage.clock, MainPage.settings, MainPage.weather, MainPage.clock],
    MainPage.settings: [MainPage.clock, MainPage.settings, MainPage.news, MainPage.settings],
    MainPage.weather: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock],
    MainPage.news: [MainPage.weather, MainPage.news, MainPage.news, MainPage.settings],
    MainPage.none: [MainPage.weather, MainPage.news, MainPage.weather, MainPage.clock]
}

# Weather Page Graph
Weather = {
    WeatherPage.none: [WeatherPage.returnButton, WeatherPage.returnButton, WeatherPage.returnButton,
                       WeatherPage.returnButton],
    WeatherPage.returnButton: [WeatherPage.returnButton, WeatherPage.hourly_weather, WeatherPage.returnButton,
                               WeatherPage.current_weather],
    WeatherPage.hourly_weather: [WeatherPage.returnButton, WeatherPage.hourly_weather, WeatherPage.hourly_weather,
                                 WeatherPage.daily_weather],
    WeatherPage.current_weather: [WeatherPage.current_weather, WeatherPage.daily_weather, WeatherPage.returnButton,
                                  WeatherPage.current_weather],
    WeatherPage.daily_weather: [WeatherPage.current_weather, WeatherPage.daily_weather, WeatherPage.hourly_weather,
                                WeatherPage.daily_weather]
}

# News PageGraph
News = {
    NewsPage.none: [NewsPage.headlines, NewsPage.stocks, NewsPage.returnButton, NewsPage.stocks],
    NewsPage.returnButton: [NewsPage.returnButton, NewsPage.stocks, NewsPage.returnButton, NewsPage.stocks],
    NewsPage.headlines:[NewsPage.stocks, NewsPage.headlines, NewsPage.headlines, NewsPage.headlines],
    NewsPage.stocks:[NewsPage.returnButton, NewsPage.headlines, NewsPage.returnButton, NewsPage.stocks]

}

# Time PageGraph
Planner = {
    PlannerPage.none: [PlannerPage.returnButton, PlannerPage.returnButton, PlannerPage.returnButton, PlannerPage.returnButton],
    PlannerPage.returnButton: [PlannerPage.returnButton, PlannerPage.eventlist, PlannerPage.returnButton, PlannerPage.todolist],
    PlannerPage.todolist:[PlannerPage.todolist, PlannerPage.todo0, PlannerPage.returnButton, PlannerPage.todolist],
    PlannerPage.todo0:[PlannerPage.todolist, PlannerPage.todo1, PlannerPage.returnButton, PlannerPage.todo0],
    PlannerPage.todo1:[PlannerPage.todo0, PlannerPage.todo2, PlannerPage.returnButton, PlannerPage.todo1],
    PlannerPage.todo2:[PlannerPage.todo1, PlannerPage.todo3, PlannerPage.returnButton, PlannerPage.todo2],
    PlannerPage.todo3:[PlannerPage.todo2, PlannerPage.todo4, PlannerPage.returnButton, PlannerPage.todo3],
    PlannerPage.todo4:[PlannerPage.todo3, PlannerPage.todo4, PlannerPage.returnButton, PlannerPage.todo4],

    PlannerPage.eventlist:[PlannerPage.returnButton, PlannerPage.event0, PlannerPage.eventlist, PlannerPage.eventlist],
    PlannerPage.event0:[PlannerPage.eventlist, PlannerPage.event1, PlannerPage.event0, PlannerPage.event0],
    PlannerPage.event1:[PlannerPage.event0, PlannerPage.event2, PlannerPage.event1, PlannerPage.event1],
    PlannerPage.event2:[PlannerPage.event1, PlannerPage.event3, PlannerPage.event2, PlannerPage.event2],
    PlannerPage.event3:[PlannerPage.event2, PlannerPage.event4, PlannerPage.event3, PlannerPage.event3],
    PlannerPage.event4:[PlannerPage.event3, PlannerPage.event5, PlannerPage.event4, PlannerPage.event4],
    PlannerPage.event5:[PlannerPage.event4, PlannerPage.event6, PlannerPage.event5, PlannerPage.event5],
    PlannerPage.event6:[PlannerPage.event5, PlannerPage.event7, PlannerPage.event6, PlannerPage.event6],
    PlannerPage.event7:[PlannerPage.event6, PlannerPage.event8, PlannerPage.event7, PlannerPage.event7],
    PlannerPage.event8:[PlannerPage.event7, PlannerPage.event9, PlannerPage.event8, PlannerPage.event8],
    PlannerPage.event9:[PlannerPage.event8, PlannerPage.event9, PlannerPage.event9, PlannerPage.event9],

}

# Settings Page Graph
Settings = {
    # Main Page Portion
    SettingsPage.none: [SettingsPage.returnButton, SettingsPage.returnButton, SettingsPage.returnButton,
                        SettingsPage.returnButton],
    SettingsPage.returnButton: [SettingsPage.returnButton, SettingsPage.update_now, SettingsPage.returnButton,
                                SettingsPage.returnButton],
    # Update now portion
    SettingsPage.update_now: [SettingsPage.returnButton, SettingsPage.blue, SettingsPage.update_now,
                                SettingsPage.update_now],

    # Color Scheme portion
    SettingsPage.blue: [SettingsPage.update_now, SettingsPage.green, SettingsPage.blue, SettingsPage.blue],
    SettingsPage.green: [SettingsPage.blue, SettingsPage.orange, SettingsPage.green, SettingsPage.green],
    SettingsPage.orange: [SettingsPage.green, SettingsPage.pink, SettingsPage.orange, SettingsPage.orange],
    SettingsPage.pink: [SettingsPage.orange, SettingsPage.purple, SettingsPage.pink, SettingsPage.pink],
    SettingsPage.purple: [SettingsPage.pink, SettingsPage.red, SettingsPage.purple, SettingsPage.purple],
    SettingsPage.red: [SettingsPage.purple, SettingsPage.yellow, SettingsPage.red, SettingsPage.red],
    SettingsPage.yellow: [SettingsPage.red, SettingsPage.small, SettingsPage.yellow, SettingsPage.yellow],

    # Font Setting Portion
    SettingsPage.small: [SettingsPage.yellow, SettingsPage.medium, SettingsPage.small, SettingsPage.small],
    SettingsPage.medium: [SettingsPage.small, SettingsPage.large, SettingsPage.medium, SettingsPage.medium],
    SettingsPage.large: [SettingsPage.medium, SettingsPage.large, SettingsPage.large, SettingsPage.large]


}

