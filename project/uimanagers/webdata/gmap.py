import simplejson
import urllib
from project.resources import varloader, var


def get_travel_time():

    # getting necessary data
    origin = var.gmap['origin']
    destination = var.gmap['destination']
    gmap_settings = var.gmap['settings']

    # Getting Cords for Origin Location
    origin_address = origin['state_address'] + ',+' + origin['city_address'] + ',+' + origin['state_address']
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + origin_address + '&key=' + var.api_tokens[
        'google_geocode']
    result = simplejson.load(urllib.urlopen(url))
    print result
    origin_location = result['results'][0]['geometry']['location']
    print origin_location

    # Getting Coords for Destination Location
    destination_address = destination['state_address'] + ',+' + destination['city_address'] + ',+' + destination[
        'state_address']
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + destination_address + '&key=' + \
          var.api_tokens['google_geocode']
    result = simplejson.load(urllib.urlopen(url))
    print result
    destination_location = result['results'][0]['geometry']['location']
    print destination_location

    # Personal Settings for Origin to Destination
    origins = str(origin_location['lat']) + ',' + str(origin_location['lng'])
    destinations = str(destination_location['lat']) + ',' + str(destination_location['lng'])

    # Getting google map time to get from origin to destination
    print var.api_tokens['google_distance_matrix']
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' + \
          'origins=' + origins + \
          '&destinations=' + destinations + \
          '&departure_time=now' + \
          '&mode=' + gmap_settings['mode'] + \
          '&language=fr-FR' + \
          '&key=' + var.api_tokens['google_distance_matrix']
    # Checks for case that it was Transit
    if gmap_settings['mode'] == 'transit':
        url = url + '&transit_mode' + gmap_settings['transit_mode']

    # Checks for case that it was avoid tolls
    if gmap_settings['avoid_tolls']:
        url += '&avoid=tolls'

    # Display Results
    result = simplejson.load(urllib.urlopen(url))
    print result
    time_to_location = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
    print time_to_location
    var.travel_data['main'] = time_to_location

    # Now Checking Local drive time
    if gmap_settings['avoid_tolls']:
        url += '|highways'
    else:
        url += '&avoid=highways'

    # Display Results
    result = simplejson.load(urllib.urlopen(url))
    print result
    time_to_location_locally = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
    print time_to_location_locally
    var.travel_data['backup'] = time_to_location_locally
    varloader.save_data_to_json_file(var.travel_data, var.file_paths['travel_data'])
