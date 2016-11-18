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
        with open('preferences.json') as f:
            var.preferences = json.load(f)
    except IOError as e:
        print "Unable to open file"  # Does not exist OR no read permissions
        # Preferences Default
        print var.pref_keys['mp_stocks']
        var.preferences[var.pref_keys['mp_stocks']] = True
        var.preferences[var.pref_keys['mp_news']] = True
        var.preferences[var.pref_keys['mp_sunset']] = True
        var.preferences[var.pref_keys['mp_sunrise']] = True
        var.preferences[var.pref_keys['mp_humidity']] = True
        var.preferences[var.pref_keys['mp_hilo']] = True
        update_preferences()


def toggle_preferences(key):
    var.preferences[key] = not var.preferences[key]
    update_preferences()



# ------------------------ Other Data -------------------------- #


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


def change_other_data(key,val):
    var.other_data[key] = val
    update_other()