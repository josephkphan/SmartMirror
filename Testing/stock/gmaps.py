import simplejson
import urllib

# Api Keys
key_distance_matrix = 'AIzaSyDsFMYDBCeSx0BI7wk1wSe-JqPNbDSu1G4'
key_geocode = 'AIzaSyBH-7pbd0vh3VzKSJJ5rkbZYcdhdgC7XCw'

# Origin Location
origin_street_address = '1600+Amphitheatre+Parkway'
origin_city_address = 'Mountain+View'
origin_state_address = 'CA'

# Destination Location
destination_street_address = '500+El+Camino+Real'
destination_city_address = 'Santa+Clara'
destination_state_address = 'CA'

# Getting Cords for Origin Location
origin_address = origin_state_address + ',+' + origin_city_address + ',+' + origin_state_address
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + origin_address + '&key=' + key_geocode
result = simplejson.load(urllib.urlopen(url))
print result
origin_location = result['results'][0]['geometry']['location']
print origin_location

# Getting Coords for Destination Location
destination_address = destination_state_address + ',+' + destination_city_address + ',+' + destination_state_address
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + destination_address + '&key=' + key_geocode
result = simplejson.load(urllib.urlopen(url))
print result
destination_location = result['results'][0]['geometry']['location']
print destination_location

# Personal Settings for Origin to Destination
mode = 'driving'
origins = str(origin_location['lat']) + ',' + str(origin_location['lng'])
destinations = str(destination_location['lat']) + ',' + str(destination_location['lng'])
is_avoid_tolls = False
transit_mode = 'bus'

# Getting google map time to get from origin to destination
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' + \
      'origins=' + origins + \
      '&destinations=' + destinations + \
      '&departure_time=now' + \
      '&mode=' + mode + \
      '&language=fr-FR' + \
      '&key=' + key_distance_matrix
# Checks for case that it was Transit
if mode == 'transit':
    url = url + '&transit_mode' + transit_mode
# Checks for case that it was avoid tolls
if is_avoid_tolls:
    url += '&avoid=tolls'

# Display Results
result = simplejson.load(urllib.urlopen(url))
print result
time_to_location = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
print time_to_location

# Now Checking Local drive time
if is_avoid_tolls:
    url += '|highways'
else:
    url += '&avoid=highways'

# Display Results
result = simplejson.load(urllib.urlopen(url))
print result
time_to_location_locally = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
print time_to_location_locally
