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
    NewsPage.none: [NewsPage.returnButton, NewsPage.none, NewsPage.none, NewsPage.returnButton],
    NewsPage.returnButton: [NewsPage.returnButton, NewsPage.headlines, NewsPage.returnButton, NewsPage.returnButton],
    NewsPage.headlines:[NewsPage.returnButton, NewsPage.headlines, NewsPage.headlines, NewsPage.headlines]
}

# Time PageGraph
Planner = {
    PlannerPage.none: [PlannerPage.returnButton, PlannerPage.returnButton, PlannerPage.returnButton, PlannerPage.returnButton],
    PlannerPage.returnButton: [PlannerPage.returnButton, PlannerPage.returnButton, PlannerPage.returnButton, PlannerPage.todolist],
    PlannerPage.todolist:[PlannerPage.todolist, PlannerPage.todolist, PlannerPage.returnButton, PlannerPage.todolist]
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

