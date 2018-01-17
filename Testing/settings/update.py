import requests
import json

# NOTE: To run this program, the shell must currently be in the 'project' directory


# Python only searches current directory, the entry-point script is running from, and sys.path which includes
# locations such as the package installation directory
import sys
sys.path.insert(0, '/Users/thomasnguyen/Library/Mobile Documents/com~apple~CloudDocs/Santa Clara University/Smart Mirror/SmartMirror')
from project.resources import var, varloader


# -------------------- File Paths of Preferences To Be Updated -------------------- #
file_paths = {
    'location': '../project/data/info/location.json',
    'weather': '../project/data/info/weather.json',
    'gmap': '../project/data/info/gmap.json',
    'travel_data': '../project/data/info/travel_data.json',
    'last_updated': '../project/data/info/last_updated.json',
    'news': '../project/data/info/news.json',
    'other': '../project/data/info/other.json',
    'preferences': '../project/data/info/preferences.json',
    'stocks': '../project/data/info/stocks.json',
    'stock_data': '../project/data/info/stock_data.json',
    'key': '../project/data/key/key.json',
    'gcalendar_key': '../project/data/key/client_secret.json',
    'calendar_data': '../project/data/info/calendar_data.json',
    'to_do_list': '../project/data/info/to_do_list.json',
    'profile': '../project/data/info/profile.json'
}


# -------------------- Get Updates From the Web Server -------------------- #
payload = {'username': 'test', 'mirrorID': 'test'} # TODO: mirrorID & gpg key
r = requests.get('http://localhost:3000/api/get_user_settings', params=payload)
web_server_response = r.json()


# TODO: IF web account does not yet exist ... return

# -------------------- Mirror Settings -------------------- #
mirror_preferences = varloader.get_data_from_json_file(file_paths['preferences'])
if mirror_preferences['color'] != web_server_response['color']:
    varloader.change_color_scheme(web_server_response['color'])
if mirror_preferences['font_size_current'] != web_server_response['fontSize']:
    varloader.change_font_size(web_server_response['fontSize'])


# -------------------- Stocks -------------------- #
# Parse response from web server and make it into a JSON
stocks_string = web_server_response['stocks'].split("////")
web_server_stocks = []
for item in stocks_string:
    web_server_stocks += item

# Check to see if they differ, if so, save to JSON
mirror_stocks = varloader.get_data_from_json_file(file_paths['stocks'])
if mirror_stocks != web_server_stocks:
    varloader.update_stocks(web_server_stocks)


# -------------------- To Do List -------------------- #
# Parse response from web server and make it into a JSON
to_do_list_string = web_server_response['to_do_list'].split("////")
web_server_to_do_list = []
for item in to_do_list_string:
    web_server_to_do_list += item

# Check to see if they differ, if so, save to JSON
mirror_to_do_list = varloader.get_data_from_json_file(file_paths['to_do_list'])
if mirror_to_do_list != web_server_to_do_list:
    varloader.update_to_do_list(web_server_to_do_list)


# -------------------- Maps Settings -------------------- #
# Parse response from web server and make it into a JSON
web_server_maps = {
    "origin": {
        "city_address": web_server_response['maps_origin_city_address'],
        "street_address": web_server_response['maps_origin_street_address'],
        "state_address": web_server_response['maps_origin_state_address']
    },
    "destination": {
        "city_address": web_server_response['maps_destination_city_address'],
        "street_address": web_server_response['maps_destination_street_address'],
        "state_address": web_server_response['maps_destination_state_address']
    },
    "settings": {
        "avoid_tolls": web_server_response['maps_settings_avoid_tolls'],
        "mode": web_server_response['maps_settings_mode'],
        "transit_mode": web_server_response['maps_settings_transit_mode']
    }
}

web_server_maps_string = json.dumps(web_server_maps)
web_server_maps_json = json.loads(web_server_maps_string)

# Check to see if they differ, if so, save to JSON
mirror_map = varloader.get_data_from_json_file(file_paths['gmap'])
if mirror_map != web_server_maps_json:
    varloader.update_maps(web_server_maps_json)


# -------------------- API Keys -------------------- #
# Parse response from web server and make it into a JSON
web_server_keys = {
    "google_distance_matrix": web_server_response['google_distance_matrix_key'],
    "google_geocode": web_server_response['google_geocode_key'],
    "dark_sky_weather": web_server_response['dark_sky_weather_key'],
}

web_server_keys_string = json.dumps(web_server_keys)
web_server_keys_json = json.loads(web_server_keys_string)

# Check to see if they differ, if so, save to JSON
mirror_keys = varloader.get_data_from_json_file(file_paths['key'])
if mirror_keys != web_server_keys_json:
    varloader.update_keys(web_server_keys_json)


# -------------------- User Profile -------------------- #
# Parse response from web server and make it into a JSON
web_server_profile = {
    "username": web_server_response['username'],
    "name": web_server_response['name'],
    "mirrorID": web_server_response['mirrorID']
}

web_server_profile_string = json.dumps(web_server_profile)
web_server_profile_json = json.loads(web_server_profile_string)

# Check to see if they differ, if so, save to JSON
mirror_profile = varloader.get_data_from_json_file(file_paths['profile'])
if mirror_profile != web_server_profile_json:
    varloader.update_profile(web_server_profile_json)
