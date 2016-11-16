import var
import json
import time


# ----------------------- Saved Web Data ----------------------- #
# todo Make this work!!!!
def write_saved_data_json_to_file():
    # Open a file for writing

    out_file = open("data.json", "w")
    # Save the data into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(var.saved_data, out_file, indent=4)
    out_file.close()


# Reading data back
def get_saved_data():
    try:
        with open('data.json', 'r') as f:
            var.saved_data = json.load(f)
    except IOError as e:
        print "Unable to open file"  # Does not exist OR no read permissions


def update_data(weather_data, location_data, news_data):
    # Converting to Json
    get_saved_data()
    if weather_data is not None:
        var.saved_data['weather'] = weather_data

    if location_data is not None:
        var.saved_data['location'] = location_data

    if news_data is not None:
        headlines = {}
        links = {}
        for i in range(0, 5):
            headlines[str(i)] = news_data.entries[i].title
            links[str(i)] = news_data.entries[i].links
            var.saved_data['news_headlines'] = headlines
            var.saved_data['news_links'] = links
        var.saved_data['last_updated'] = time.time()
        write_saved_data_json_to_file()


# ----------------------- Preferences ----------------------- #

def update_preferences():
    out_file = open("preferences.json", "w")
    # Save the data into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(var.preferences, out_file, indent=4)
    out_file.close()


def get_preferences():
    try:
        with open('preferences.json') as file:
            var.preferences = json.load(file)
    except IOError as e:
        print "Unable to open file"  # Does not exist OR no read permissions
        # Preferences Default
        var.preferences['main_page_stocks'] = True
        var.preferences['main_page_news'] = True
        var.preferences['main_page_sunset'] = True
        var.preferences['main_page_sunrise'] = True
        var.preferences['main_page_weather_humidity'] = True
