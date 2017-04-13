import varloader
import coordcreator

wall_light_color = True

# -------------------- Coloring ------------------------ #
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

font_size_large = {
    'giant': 102,
    'bigger': 80,
    'big': 50,
    'title': 38,
    'text': 28,
    'small': 18,
    'large_icon' : (125,125),
    'medium_icon': (65,65),
    'small_medium_icon': (50, 50),
    'small_icon':(35,35),
    'news_length':70
}

font_size_medium = {
    'giant': 92,
    'bigger': 70,
    'big': 40,
    'title': 28,
    'text': 18,
    'small': 14,
    'large_icon' : (100,100),
    'medium_icon': (50,50),
    'small_medium_icon':(40,40),
    'small_icon':(25,25),
    'news_length': 100
}

font_size_small = {
    'giant': 64,
    'bigger': 48,
    'big': 32,
    'title': 20,
    'text': 14,
    'small': 10,
    'large_icon' : (75,75),
    'medium_icon': (40,40),
    'small_medium_icon': (30, 30),
    'small_icon':(20,20),
    'news_length':140
}

# todo ADD ICON SIZES

font_sizes = None
# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us'  # todo read this from file
f = open('key.txt', 'r')
weather_api_token = f.read()
print 'TOKEN:'+str(weather_api_token)
f.close()

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

bottom_left_rectangle = coordcreator.get_polygon_coord(0, camera_height / 2, camera_width / 2, camera_height / 2)

bottom_right_rectangle = coordcreator.get_polygon_coord(camera_width / 2, camera_height / 2, camera_width / 2,
                                                        camera_height / 2)

top_left_rectangle = coordcreator.get_polygon_coord(0, 0, camera_width / 2, camera_height / 2)

top_right_rectangle = coordcreator.get_polygon_coord(camera_width / 2, 0, camera_width / 2, camera_height / 2)

# ------------------- Selection Constants ----------------------#
selection_time = 2.5  # in seconds
update_time = 30  # in minutes

# -------------------- Saved Data -------------------- #

saved_data = {}
varloader.get_saved_data()

# -------------------- Settings ----------------------- #
preferences = {}
varloader.get_preferences()

# ------------------- Other Data ---------------------- #

other_data = {}
varloader.get_other()
selected_on = color_hex_codes[preferences['color']]
varloader.update_font_size()

print selected_on
print other_data

# ---------------------- Images ----------------------- #
