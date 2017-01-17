import varLoader
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
    'main_page_weather_icon' : (125,125),
    'settings_icon': (65,65),
    'newspaper_icon':(35,35)
}

font_size_medium = {
    'giant': 92,
    'bigger': 70,
    'big': 40,
    'title': 28,
    'text': 18,
    'small': 14,
    'main_page_weather_icon' : (100,100),
    'settings_icon': (50,50),
    'newspaper_icon':(25,25)
}

font_size_small = {
    'giant': 64,
    'bigger': 48,
    'big': 32,
    'title': 20,
    'text': 14,
    'small': 10,
    'main_page_weather_icon' : (75,75),
    'settings_icon': (40,40),
    'newspaper_icon':(20,20)
}

# todo ADD ICON SIZES

font_sizes = None
# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us'  # todo read this from file
f = open('key.txt', 'r')
weather_api_token = f.read()
print weather_api_token
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
update_time = 10  # in minutes

# -------------------- Saved Data -------------------- #

saved_data = {}
varLoader.get_saved_data()

# -------------------- Settings ----------------------- #
preferences = {}
varLoader.get_preferences()

# ------------------- Other Data ---------------------- #

other_data = {}
varLoader.get_other()
selected_on = color_hex_codes[preferences['color']]
varLoader.update_font_size()

print selected_on
print other_data

# ---------------------- Images ----------------------- #
