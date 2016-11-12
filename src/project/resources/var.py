import json
import time

# -------------------- Coloring ------------------------ #
selected_off = 'white'
selected_on = 'yellow'
background_color = 'black'
font_style = 'Helvetica'
# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us'  # todo read this from file
f = open('key.txt', 'r')
weather_api_token = f.read().decode('base64', 'strict')
f.close()

# -------------------- Window Sizing -------------------- #

camera_width = 200
camera_height = 200
tk_cursor_diameter = 25
tk_cursor_outline_thickness = tk_cursor_diameter / 10

# ------------------- Polygon Coordinate ---------------- #
bottom_left_rectangle = [(0, camera_height / 2), (0, camera_height), (camera_width / 2, camera_height),
                         (camera_width / 2, camera_height / 2)]

bottom_right_rectangle = [(camera_width / 2, camera_height / 2), (camera_width / 2, camera_height),
                          (camera_width, camera_height), (camera_width / 2, camera_height)]

top_left_rectangle = [(0, 0), (0, camera_height / 2), (camera_width / 2, camera_height / 2),
                      (camera_width / 2, 0)]

top_right_rectangle = [(camera_width / 2, 0), (camera_width / 2, camera_height / 2),
                       (camera_width, camera_height / 2), (camera_width, 0)]

# ------------------- Selection Constants ----------------------#
selection_time = 2.5  # in seconds
update_time = 5  # in minutes

# -------------------- Saved Data -------------------- #

# -------------------- Weather -------------------- #


# Writing JSON data

# -------------------- Read and Write to File -------------------- #

saved_data = {}


def write_json_to_file():
    # Open a file for writing

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


def update_data(weather_data, location_data, news_data):
    # Converting to Json
    read_json_from_file()
    if weather_data is not None:
        saved_data['weather'] = weather_data

    if location_data is not None:
        saved_data['location'] = location_data

    if news_data is not None:
        headlines = {}
        links = {}
        for i in range(0, 5):
            headlines[str(i)] = news_data.entries[i].title
            links[str(i)] = news_data.entries[i].links
        saved_data['news_headlines'] = headlines
        saved_data['news_links'] = links
    saved_data['last_updated'] = time.time()
    write_json_to_file()


read_json_from_file()
print "READING FROM FILE"
