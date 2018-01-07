import requests

payload = {'username': 'test', 'mirrorID': 'test'} # TODO: mirrorID & gpg key
r = requests.get('http://localhost:3000/api/get_user_settings', params=payload)
r.json();
print r.text;


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


