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
        print "Unable to open data.json file"  # Does not exist OR no read permissions
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
        print news_data.entries[0].keys()
        counter =0
        for entry in news_data.entries:
            headlines[str(counter)] = entry.title
            links[str(counter)] = entry.links
            counter += 1
        var.saved_data['news_headlines'] = headlines
        var.saved_data['news_links'] = links
        var.saved_data['news_number_of_headlines'] = counter

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
            update_font_size()
    except IOError as e:
        print "Unable to open Preferences file"  # Does not exist OR no read permissions
        # Preferences Default
        # If preferences were never created, create the preference file

        # Main page Preferences

        # todo Main Page settings isn't implemented.
        # # ONLY one of these choices can be true at a time
        # var.preferences['weather'] = True
        # var.preferences['time'] = False
        # # If weather is true, that means weather on the left and time on the right
        # # If time is true, that means time is on the left and weather is on the right
        # # weather and time cannot both be true at the same time
        #
        # # ONLY one of these choices can be true at a time
        # var.preferences['news'] = True
        # var.preferences['stocks'] = False
        # var.preferences['sports'] = False
        # var.preferences['show_this_on_bottom_of_main_page'] = 'news'

        # Color Preferences
        # ONLY one of these choices can be true at a time
        var.preferences['color'] = 'yellow'
        var.preferences['blue'] = False
        var.preferences['green'] = False
        var.preferences['orange'] = False
        var.preferences['pink'] = False
        var.preferences['purple'] = False
        var.preferences['red'] = False
        var.preferences['yellow'] = True

        # Font Size Preferences
        # OBLY one of these choices can be true at a time
        var.preferences['font_size_current'] = 'medium'
        var.preferences['small'] = False
        var.preferences['medium'] = True
        var.preferences['large'] = False

        update_preferences()  # Saves to file


def change_main_page_top(new_widget):
    if not var.preferences[new_widget]:
        var.preferences['weather'], var.preferences['time'] = var.preferences['time'], var.preferences['weather']
    update_preferences()


def change_main_page_bottom(new_widget):
    print 'HEREEEEEEE'
    print new_widget
    var.preferences[var.preferences['show_this_on_bottom_of_main_page']] = False  # turns old color off
    var.preferences[new_widget] = True  # Turns new color on
    var.preferences['show_this_on_bottom_of_main_page'] = new_widget  # updates new color
    update_preferences()


def change_color_scheme(new_color):
    var.preferences[var.preferences['color']] = False  # turns old color off
    var.preferences[new_color] = True  # Turns new color on
    var.preferences['color'] = new_color  # updates new color
    var.selected_on = var.color_hex_codes[new_color]  # PROBLEM
    update_preferences()


def change_font_size(new_size):
    var.preferences[var.preferences['font_size_current']] = False  # turns old color off
    var.preferences[new_size] = True  # Turns new color on
    var.preferences['font_size_current'] = new_size  # updates new color
    update_font_size()
    update_preferences()


def update_font_size():
    if var.preferences['font_size_current'] == 'small':
        var.font_sizes = var.font_size_small
    elif var.preferences['font_size_current'] == 'medium':
        var.font_sizes = var.font_size_medium
    else:
        var.font_sizes = var.font_size_large

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
