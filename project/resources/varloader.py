import var
import json
import time


# ----------------------- Saved Web Data ----------------------- #

def update_last_updated_variable():
    var.last_updated = time.time()
    out_file = open("last_updated.json", "w")
    json.dump(var.last_updated, out_file, indent=4)
    out_file.close()


def update_location(location_data):
    # Same as above, this makes sure an "empty' location doesnt get saved
    if location_data is not None:
        var.location_data = location_data
        out_file = open("location.json", "w")
        json.dump(var.location_data, out_file, indent=4)
        out_file.close()


def update_weather(weather_data):
    if weather_data is not None:
        var.weather_data = weather_data
        out_file = open("weather.json", "w")
        json.dump(var.weather_data, out_file, indent=4)
        out_file.close()


def update_news_headlines(news_data):
    # Same as above, but News came as parsed string. Have to convert it into Json
    if news_data is not None:
        headlines = {}  # Taking out only the headlines and links to those headlines
        links = {}
        # Converting data to Json
        print news_data.entries[0].keys()
        counter = 0
        for entry in news_data.entries:
            headlines[str(counter)] = entry.title
            links[str(counter)] = entry.links
            counter += 1
        var.news_data['headlines'] = headlines
        var.news_data['links'] = links
        var.news_data['number_of_headlines'] = counter

        out_file = open("news.json", "w")
        json.dump(var.news_data, out_file, indent=4)
        out_file.close()


# ----------------------- Preferences ----------------------- #

# Writes Preferences to file
def update_preferences():
    out_file = open("preferences.json", "w")
    json.dump(var.preferences, out_file, indent=4)
    out_file.close()


def update_api_tokens(weather_key, distance_matrix_key, geocode_key):
    if weather_key is not None:
        var.api_tokens['dark_sky_weather'] = weather_key
    if distance_matrix_key is not None:
        var.api_tokens['google_distance_matrix'] = distance_matrix_key
    if geocode_key is not None:
        var.api_tokens['google_geocode'] = geocode_key
    out_file = open("key.json", "w")
    json.dump(var.api_tokens, out_file, indent=4)
    out_file.close()


def update_gmap():
    out_file = open("gmap.json", "w")
    json.dump(var.gmap, out_file, indent=4)
    out_file.close()


def update_stocks():
    out_file = open("stocks.json", "w")
    json.dump(var.stocks, out_file, indent=4)
    out_file.close()


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


def change_other_data(key, val):
    var.other_data[key] = val
    update_other()


def get_data_from_json_file(file_name):
    try:
        with open(file_name) as f:
            return json.load(f)
    except IOError as e:
        print 'could not read ' + file_name
        if file_name == 'other.json':
            var.other_data['manual_mode'] = True
            update_other()
        elif file_name == 'preferences.json':
            reset_preferences_to_default()


def reset_preferences_to_default():
    var.preferences['color'] = 'yellow'
    var.preferences['blue'] = False
    var.preferences['green'] = False
    var.preferences['orange'] = False
    var.preferences['pink'] = False
    var.preferences['purple'] = False
    var.preferences['red'] = False
    var.preferences['yellow'] = True
    # Font Size Preferences
    # Only one of these choices can be true at a time
    var.preferences['font_size_current'] = 'medium'
    var.preferences['small'] = False
    var.preferences['medium'] = True
    var.preferences['large'] = False

    update_preferences()  # Saves to file
