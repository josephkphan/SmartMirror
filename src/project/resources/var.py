import json
import time;
# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us' # todo read this from file
weather_api_token = '58017729f3ec5ddf03d2d7a4063cad85'  # todo read this from file

# -------------------- Window Sizing -------------------- #

camera_width = 200
camera_height = 200
tk_cursor_diameter = 25
tk_cursor_outline_thickness = tk_cursor_diameter/10

# ------------------- Polygon Coordinate ---------------- #
bottom_left_rectangle = [(0, camera_height / 2), (0, camera_height), (camera_width / 2, camera_height),
                              (camera_width / 2, camera_height / 2)]

bottom_right_rectangle = [(camera_width / 2, camera_height / 2), (camera_width / 2, camera_height),
                              (camera_width, camera_height), (camera_width / 2, camera_height)]

top_left_rectangle = [(0, 0), (0, camera_height / 2), (camera_width / 2, camera_height / 2),
                              (camera_width / 2, 0)]

top_right_rectangle = [(camera_width / 2, 0), (camera_width / 2, camera_height / 2),
                              (camera_width, camera_height / 2), (camera_width, 0)]

# -------------------- Saved Data -------------------- #

# -------------------- Weather -------------------- #

saved_data = { }
saved_data['last_updated'] = 0;
# Writing JSON data


def write_json_to_file():
    # Open a file for writing
    saved_data['last_updated'] = time.time()
    out_file = open("data.json", "w")
    # Save the data into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(saved_data, out_file, indent=4)
    out_file.close()



# Reading data back
def read_json_from_file():
    global saved_data
    with open('data.json', 'r') as f:
        saved_data = json.load(f)




def update_weather_data(weather_data, location_data):

    # Converting to Json
    saved_data['weather'] = weather_data
    saved_data['location'] = location_data
    write_json_to_file()
    print saved_data


# -------------------- News -------------------- #


# -------------------- Clock -------------------- #
