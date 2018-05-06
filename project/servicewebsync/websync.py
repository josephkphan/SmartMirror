import requests
import json
import collections
from resources import var, varloader


# These file paths point to the location of the json files in our websync container
file_paths = {
    'location': '/usr/src/app/data/info/location.json',
    'weather': '/usr/src/app/data/info/weather.json',
    'gmap': '/usr/src/app/data/info/gmap.json',
    'travel_data': '/usr/src/app/data/info/travel_data.json',
    'last_updated': '/usr/src/app/data/info/last_updated.json',
    'news': '/usr/src/app/data/info/news.json',
    'other': '/usr/src/app/data/info/other.json',
    'preferences': '/usr/src/app/data/info/preferences.json',
    'stocks': '/usr/src/app/data/info/stocks.json',
    'stock_data': '/usr/src/app/data/info/stock_data.json',
    'key': '/usr/src/app/data/key/key.json',
    'gcalendar_key': '/usr/src/app/data/key/client_secret.json',
    'calendar_data': '/usr/src/app/data/info/calendar_data.json',
    'to_do_list': '/usr/src/app/data/info/to_do_list.json',
    'profile': '/usr/src/app/data/info/profile.json'
}

def convert(data):
    """
    This takes a unicode dictionary as a parameter i.e. {u'key': u'value'},
    This functional will encode it back to a normal looking dictionary (utf-8) and return the dictionary
    """
    if isinstance(data, basestring):
        return str(data.encode('utf-8'))
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

class WebSync:
    def __init__(self):
        self.web_server_response = {}
        self.update_all()

    def update_all(self):
        self.get_updates()
        self.update_settings()
        self.update_stocks()
        self.update_todo_list()
        # self.update_maps()
        # self.update_keys()
        # self.update_profile()
        print "Updated all preferences!"

    def send_updates(self):
        '''
        This function sends a POST request to the web server to update the
        web server about the mirror's current preferences.
        '''
        mirror_preferences = varloader.get_data_from_json_file(file_paths['preferences'])
        payload = {'username': 'admin', 'mirrorID': 'admin'}
        data = {
            "color": mirror_preferences['color'],
            "fontSize": mirror_preferences['font_size_current']
        }
        r = requests.post('http://mysmartmirror.herokuapp.com/api/update_user_settings', params=payload, data=data)

    def get_updates(self):
        '''
        This function sends a GET request to the web server and receives a JSON
        with all of the mirror's preferences

        Note: This function must always be called before any other update
                functions can be called
        '''
        payload = {'username': 'admin', 'mirrorID': 'admin'}  # TODO: mirrorID & gpg key
        r = requests.get('http://mysmartmirror.herokuapp.com/api/get_user_settings', params=payload)
        self.web_server_response = convert(r.json())
        print "---------- Web Server Preferences ----------"
        print self.web_server_response
        # TODO: If web account does not yet exist, return an error
        # TODO: Throw an error for the request instead of letting the program terminate

    def update_settings(self):
        '''
        Adjust mirror preferences if they differ from those on the web server
        '''
        mirror_preferences = varloader.get_data_from_json_file(file_paths['preferences'])
        if mirror_preferences['color'] != self.web_server_response['color']:
            varloader.change_color_scheme(self.web_server_response['color'])
        if mirror_preferences['font_size_current'] != self.web_server_response['fontSize']:
            varloader.change_font_size(self.web_server_response['fontSize'])

    def update_stocks(self):
        '''
        Adjust stock preferences if they differ from those on the web server
        '''
        # Parse response from web server and add it to a list of stocks
        stocks_string = self.web_server_response['stocks'].split("////")
        stocks_string.replace('\'', '"')

        # Check to see if they differ, if so, save to JSON
        mirror_stocks = varloader.get_data_from_json_file(file_paths['stocks'])
        if mirror_stocks != stocks_string:
            varloader.update_stocks(stocks_string)

    def update_todo_list(self):
        '''
        Adjust To Do List if it differs from the one on the web server
        '''
        # Parse response from web server and add it to a list of items
        to_do_list_string = self.web_server_response['to_do_list'].split("////")
        to_do_list_string.replace('\'', '"')

        # Check to see if they differ, if so, save to JSON
        mirror_to_do_list = varloader.get_data_from_json_file(file_paths['to_do_list'])
        if mirror_to_do_list != to_do_list_string:
            varloader.update_to_do_list(to_do_list_string)

    def update_maps(self):
        '''
        Adjust Maps preferences if it differs from the one on the web server
        '''
        # Parse response from web server and make it into a JSON
        web_server_maps = {
            "origin": {
                "city_address": self.web_server_response['maps_origin_city_address'],
                "street_address": self.web_server_response['maps_origin_street_address'],
                "state_address": self.web_server_response['maps_origin_state_address']
            },
            "destination": {
                "city_address": self.web_server_response['maps_destination_city_address'],
                "street_address": self.web_server_response['maps_destination_street_address'],
                "state_address": self.web_server_response['maps_destination_state_address']
            },
            "settings": {
                "avoid_tolls": self.web_server_response['maps_settings_avoid_tolls'],
                "mode": self.web_server_response['maps_settings_mode'],
                "transit_mode": self.web_server_response['maps_settings_transit_mode']
            }
        }
        web_server_maps_string = json.dumps(web_server_maps)
        web_server_maps_json = json.loads(web_server_maps_string)

        # Check to see if they differ, if so, save to JSON
        mirror_map = varloader.get_data_from_json_file(file_paths['gmap'])
        if mirror_map != web_server_maps_json:
            varloader.update_maps(web_server_maps_json)

    def update_keys(self):
        '''
        Adjust API Keys preferences if it differs from the one on the web server
        '''
        # Parse response from web server and make it into a JSON
        web_server_keys = {
            "google_distance_matrix": self.web_server_response['google_distance_matrix_key'],
            "google_geocode": self.web_server_response['google_geocode_key'],
            "dark_sky_weather": self.web_server_response['dark_sky_weather_key'],
        }

        web_server_keys_string = json.dumps(web_server_keys)
        web_server_keys_json = json.loads(web_server_keys_string)

        # Check to see if they differ, if so, save to JSON
        mirror_keys = varloader.get_data_from_json_file(file_paths['key'])
        if mirror_keys != web_server_keys_json:
            varloader.update_keys(web_server_keys_json)

    def update_profile(self):
        '''
        Adjust User Profile preferences if it differs from the one on the web server
        '''
        # Parse response from web server and make it into a JSON
        web_server_profile = {
            "username": self.web_server_response['username'],
            "name": self.web_server_response['name'],
            "mirrorID": self.web_server_response['mirrorID']
        }

        web_server_profile_string = json.dumps(web_server_profile)
        web_server_profile_json = json.loads(web_server_profile_string)

        # Check to see if they differ, if so, save to JSON
        mirror_profile = varloader.get_data_from_json_file(file_paths['profile'])
        if mirror_profile != web_server_profile_json:
            varloader.update_profile(web_server_profile_json)
