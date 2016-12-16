import var
import json
import time


# ----------------------- Saved Web Data ----------------------- #

# Writes saved_data to data.json
def write_saved_data_json_to_file():
    # Open a file for writing
    out_file = open("data.json", "w")
    # Save the data into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(var.saved_data, out_file, indent=4)
    out_file.close()


# Reading from data.json file and saving into saved_data
def get_saved_data():
    try:
        with open('data.json', 'r') as f:
            var.saved_data = json.load(f)
    except IOError as e:
        print "Unable to open file"  # Does not exist OR no read permissions
        # todo end the program is there isnt an internet


# Updated the current gathered data from web, and saves it (by writing to file)
def update_data(weather_data, location_data, news_data):
    # if gathering weather data failed, this will keep the last successful saved instance
    # rather than writing over it
    get_saved_data()

    if weather_data is not None:
        var.saved_data['weather'] = weather_data

    # Same as above, this makes sure an "empty' location doesnt get saved
    if location_data is not None:
        var.saved_data['location'] = location_data

    # Same as above, but News came as parsed string. Have to convert it into Json
    if news_data is not None:
        headlines = {}  # Taking out only the headlines and links to those headlines
        links = {}
        # Converting data to Json
        for i in range(0, 5):
            headlines[str(i)] = news_data.entries[i].title
            links[str(i)] = news_data.entries[i].links
            var.saved_data['news_headlines'] = headlines
            var.saved_data['news_links'] = links

    # Saves the time which data was last updated
    var.saved_data['last_updated'] = time.time()

    # Writes data to file
    write_saved_data_json_to_file()


# ----------------------- Preferences ----------------------- #

# Writes Preferences to file
def update_preferences():
    out_file = open("preferences.json", "w")
    json.dump(var.preferences, out_file, indent=4)
    out_file.close()


# Gets Preferences from file
def get_preferences():
    try:
        with open('preferences.json') as f:
            var.preferences = json.load(f)
    except IOError as e:
        print "Unable to open file"  # Does not exist OR no read permissions
        # Preferences Default
        # If preferences were never created, create the preference file

        # Main page Preferences
        var.preferences['main_page_stocks'] = True
        var.preferences['main_page_news'] = True
        var.preferences['main_page_sunset'] = True
        var.preferences['main_page_sunrise'] = True
        var.preferences['main_page_high_low'] = True

        # Color Preferences
        var.preferences['color'] = 'yellow'
        var.preferences['blue'] = False
        var.preferences['green'] = False
        var.preferences['orange'] = False
        var.preferences['pink'] = False
        var.preferences['purple'] = False
        var.preferences['red'] = False
        var.preferences['yellow'] = True

        update_preferences()  # Saves to file


# User wanted to change a preference, change it and update file
def toggle_preferences(key):
    var.preferences[key] = not var.preferences[key]
    update_preferences()


def change_color_scheme(new_color):
    var.preferences[var.preferences['color']] = False  # turns old color off
    var.preferences[new_color] = True  # Turns new color on
    var.preferences['color'] = new_color  # updates new color   #TODO PROBLEM IS HERE NEW COLOR IS STILL HEX NEED TEXT
    var.selected_on = var.color_hex_codes[new_color]  # PROBLEM
    update_preferences()


# ------------------------ Other Data -------------------------- #

# todo DO WE NEED THIS OTHER FILE??? Curently only holding Camera mode... which isnt even implemented yet
def update_other():
    out_file = open("other.json", "w")
    # Save the data into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(var.other_data, out_file, indent=4)
    out_file.close()


def get_other():
    try:
        with open('other.json') as file:
            var.other_data = json.load(file)
    except IOError as e:
        print "Unable to open file"  # Does not exist OR no read permissions
        # Preferences Default
        var.other_data['manual_mode'] = True
        update_other()


def change_other_data(key, val):
    var.other_data[key] = val
    update_other()
