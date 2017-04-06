import simplejson, urllib

origin_street_address = '1600+Amphitheatre+Parkway'
origin_city_address = 'Mountain+View'
origin_state_address = 'CA'
origin_address = origin_state_address + ',+' + origin_city_address + ',+' + origin_state_address
key_geocode = 'AIzaSyBH-7pbd0vh3VzKSJJ5rkbZYcdhdgC7XCw'
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + origin_address + '&key=' + key_geocode
result = simplejson.load(urllib.urlopen(url))
print result
print '------------------------------'
origin_location = result['results'][0]['geometry']['location']
print origin_location
print origin_location['lat']
print origin_location['lng']

destination_street_address = '500+El+Camino+Real'
destination_city_address = 'Santa+Clara'
destination_state_address = 'CA'
destination_address = destination_state_address + ',+' + destination_city_address + ',+' + destination_state_address
url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + destination_address + '&key=' + key_geocode
result = simplejson.load(urllib.urlopen(url))
print result
print '------------------------------'
destination_location = result['results'][0]['geometry']['location']
print destination_location
print destination_location['lat']
print destination_location['lng']


# orig_coord = orig_lat, orig_lng
# dest_coord = dest_lat, dest_lng
mode = 'driving'
origins = str(origin_location['lat']) + ',' + str(origin_location['lng'])
destinations = str(destination_location['lat']) + ',' + str(destination_location['lng'])
key_distance_matrix = 'AIzaSyDsFMYDBCeSx0BI7wk1wSe-JqPNbDSu1G4'
transit_mode = 'bus'
if mode == 'transit':
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' + \
          'origins=' + origins + \
          '&departure_time=now' + \
          '&destinations=' + destinations + \
          '&mode=' + mode + \
          '&transit_mode' + transit_mode + \
          '&language=fr-FR&' + \
          'key=' + key_distance_matrix
else:
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?' + \
          'origins=' + origins + \
          '&departure_time=now' + \
          '&destinations=' + destinations + \
          '&mode=' + mode + \
          '&language=fr-FR&' + \
          'key=' + key_distance_matrix

result = simplejson.load(urllib.urlopen(url))
print result
time_to_location = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
print time_to_location



# Distance Matrix AIzaSyDsFMYDBCeSx0BI7wk1wSe-JqPNbDSu1G4
# Geocode AIzaSyBH-7pbd0vh3VzKSJJ5rkbZYcdhdgC7XCw
#
# 37.354108, -121.955236 #Santa Clara
# 37.338208, -121.886329 #San Jose
# origins=37.354108, -121.955236|37.338208, -121.886329
#
# #Examples:
# 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=37.354108, -121.955236|37.338208, -121.886329&mode=bicycling&language=fr-FR&key=AIzaSyDsFMYDBCeSx0BI7wk1wSe-JqPNbDSu1G4'
# 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&mode=bicycling&language=fr-FR&key=AIzaSyDsFMYDBCeSx0BI7wk1wSe-JqPNbDSu1G4'

# todo take off my api code when push to github
# todo add in departure time
# add in options to walk bike,transit mode etc, best guess (traffic) etc
#
