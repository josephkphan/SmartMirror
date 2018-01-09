import requests

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
}


# -------------------- Get Updates From the Web Server -------------------- #
payload = {'username': 'test', 'mirrorID': 'test'} # TODO: mirrorID & gpg key
r = requests.get('http://localhost:3000/api/get_user_settings', params=payload)
print r.text
web_server_response = r.json()


# -------------------- Mirror Settings -------------------- #
mirror_preferences = varloader.get_data_from_json_file(file_paths['preferences'])
if mirror_preferences['color'] != web_server_response['color']:
    varloader.change_color_scheme(web_server_response['color'])
    print 'Changed color scheme to ' + web_server_response['color']
if mirror_preferences['font_size_current'] != web_server_response['fontSize']:
    varloader.change_font_size(web_server_response['fontSize'])
    print 'Changed font size to ' + web_server_response['fontSize']


# -------------------- Stocks -------------------- #
mirror_stocks = varloader.get_data_from_json_file(file_paths['to_do_list'])


# -------------------- To Do List -------------------- #
mirror_to_do_list = varloader.get_data_from_json_file(file_paths['stocks'])


# -------------------- Maps Settings -------------------- #
mirror_map = varloader.get_data_from_json_file(file_paths['gmap'])


# -------------------- API Keys -------------------- #
mirror_map = varloader.get_data_from_json_file(file_paths['key'])



# // General Information
# username: String,
# password: String,
# email: String,
# name: String, -->
# mirrorID: String, -->
# about_me: String,
#
# // Api Keys
# google_distance_matrix_key: String, --> api_tokens[]
# google_geocode_key: String, --> api_tokens[]
# dark_sky_weather_key: String, --> api_tokens[]
#
# // Facebook and Google Authentication
# facebook: {
#     id: String,
#     token: String,
#     name: String
# },
# google: {
#     id: String,
#     token: String,
#     name: String
# },
#
# // Mirror Widget Information
# to_do_list: String, --> to_do_list[]
# stocks: String, --> stocks_list[]
#
# maps_origin_street_address: String, --> gmap[]
# maps_origin_city_address: String, --> gmap[]
# maps_origin_state_address: String, --> gmap[]
# maps_origin_country_address: String, --> gmap[]
#
# maps_destination_street_address: String, --> gmap[]
# maps_destination_city_address: String, --> gmap[]
# maps_destination_state_address: String, --> gmap[]
#
# maps_settings_avoid_tolls: Boolean, --> gmap[]
# maps_settings_mode: String, --> gmap[]
# maps_settings_transit_mode: String, --> gmap[]
#
# // Mirror Settings
# color: String, --> preferences[]
# fontSize: String --> preferences[]
