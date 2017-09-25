import varloader
import coordcreator

# Whether background color (for hand gesture) is light color or dark color
wall_light_color = True

# ------------------------------------------------   CONSTANTS  ------------------------------------------------ #
# -------------------- Color, Font Type, Background Color ------------------------ #
selected_off = 'white'
background_color = 'black'
font_style = 'Helvetica'

color_hex_codes = {
    'blue': '#00bfff',
    'green': '#32CD32',
    'orange': '#f7580e',
    'pink': '#f2137f',
    'purple': '#c932ef',
    'red': '#ef1f1f',
    'yellow': '#ffff00'

}

# ------------------ Font Sizes ----------------- #
font_size_large = {
    'giant': 102,
    'bigger': 80,
    'big': 50,
    'title': 38,
    'big_text': 33,
    'text': 28,
    'small': 18,
    'large_icon': (125, 125),
    'medium_icon': (65, 65),
    'small_medium_icon': (50, 50),
    'small_icon': (35, 35),
    'news_length': 70
}

font_size_medium = {
    'giant': 92,
    'bigger': 70,
    'big': 40,
    'title': 28,
    'big_text': 23,
    'text': 18,
    'small': 14,
    'large_icon': (100, 100),
    'medium_icon': (50, 50),
    'small_medium_icon': (40, 40),
    'small_icon': (25, 25),
    'news_length': 100
}

font_size_small = {
    'giant': 64,
    'bigger': 48,
    'big': 32,
    'title': 20,
    'big_text': 17,
    'text': 14,
    'small': 10,
    'large_icon': (75, 75),
    'medium_icon': (40, 40),
    'small_medium_icon': (30, 30),
    'small_icon': (20, 20),
    'news_length': 140
}

file_paths = {
    'location': 'data/info/location.json',
    'weather': 'data/info/weather.json',
    'gmap': 'data/info/gmap.json',
    'travel_data': 'data/info/travel_data.json',
    'last_updated': 'data/info/last_updated.json',
    'news': 'data/info/news.json',
    'other': 'data/info/other.json',
    'preferences': 'data/info/preferences.json',
    'stocks': 'data/info/stocks.json',
    'stock_data': 'data/info/stock_data.json',
    'key': 'data/key/key.json',
    'gcalendar_key': 'data/key/client_secret.json',
    'calendar_data': 'data/info/calendar_data.json',
    'to_do_list': 'data/info/to_do_list.json',
}

# ------------------- Selection Time Constants ----------------------#
selection_time = 2.5  # in seconds (hover with hand gesture for 2.5 seconds
update_time = 15  # in minutes (auto update every 30 minutes)

font_sizes = None

# -------------------- Window Sizing -------------------- #

camera_width = 200
camera_height = 200
tk_cursor_diameter = 25
tk_cursor_outline_thickness = tk_cursor_diameter / 10

# ------------------- Polygon Coordinate ---------------- #

#    0 ----------50-----------100- ... X Axis
#    |
#    |      THIS IS HOW THE
#    |      AXIS WORKS
#    50     NOTE* Y IS UPSIDE DOWN
#    |
#    |
#    |
#    100
#   ...
#    Y Axis

# Four Corners

# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us'
api_tokens = varloader.get_data_from_json_file(file_paths['key'])

# --------------- Setting Hand Gesture Areas --------------- #

bottom_left_rectangle = coordcreator.get_polygon_coord(0, camera_height / 2, camera_width / 2, camera_height / 2)

bottom_right_rectangle = coordcreator.get_polygon_coord(camera_width / 2, camera_height / 2, camera_width / 2,
                                                        camera_height / 2)

top_left_rectangle = coordcreator.get_polygon_coord(0, 0, camera_width / 2, camera_height / 2)

top_right_rectangle = coordcreator.get_polygon_coord(camera_width / 2, 0, camera_width / 2, camera_height / 2)

# --------------------------------------- Loading Data From Files ----------------------------------------------- #

# Loading up Data

weather_data = varloader.get_data_from_json_file(file_paths['weather'])
news_data = varloader.get_data_from_json_file(file_paths['news'])
last_updated = varloader.get_data_from_json_file(file_paths['last_updated'])
location_data = varloader.get_data_from_json_file(file_paths['location'])

# Loading up Preferences
preferences = varloader.get_data_from_json_file(file_paths['preferences'])

# Loading Up Font Size
varloader.update_font_size()

# Loading Up Other Data (manual mode / last update time)
other_data = varloader.get_data_from_json_file(file_paths['other'])

# Loading Up Color Scheme
selected_on = color_hex_codes[preferences['color']]

# Loading Up Stock List
stocks_list = varloader.get_data_from_json_file(file_paths['stocks'])

stock_data = varloader.get_data_from_json_file(file_paths['stock_data'])

# Loading Up Google Map Settings
gmap = varloader.get_data_from_json_file(file_paths['gmap'])

travel_data = varloader.get_data_from_json_file(file_paths['travel_data'])

calendar_data = varloader.get_data_from_json_file(file_paths['calendar_data'])

# to_do_list = varloader.get_data_from_json_file(file_paths['to_do_list'])
to_do_list = ['item1:...', 'item2:...', 'item3:...']
varloader.save_data_to_json_file(to_do_list, file_paths['to_do_list'])

print selected_on
print other_data

# ---------------------- Images ----------------------- #

is_updating = False
update_completed = False
