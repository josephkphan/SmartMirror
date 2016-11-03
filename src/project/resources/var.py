# -------------------- For Web Parsing -------------------- #

ip = '<IP>'
country_code = 'us' # todo read this from file
weather_api_token = '58017729f3ec5ddf03d2d7a4063cad85'  # todo read this from file

# -------------------- Window Sizing -------------------- #

camera_width = 200
camera_height = 200
tk_cursor_diameter = 25
tk_cursor_outline_thickness = tk_cursor_diameter/10

# -------------------- Saved Data -------------------- #

# -------------------- Weather -------------------- #
saved_weather_icon = None
saved_weather_forecast = None
saved_weather_currently = None
saved_weather_location = None
saved_weather_temperature = None


def update_weather_data(icon,forecast,currently, location, temperature):
    global saved_weather_forecast, saved_weather_icon, saved_weather_location
    global saved_weather_currently, saved_weather_temperature
    saved_weather_icon = icon
    saved_weather_forecast= forecast
    saved_weather_currently = currently
    saved_weather_location = location
    saved_weather_temperature = temperature

# -------------------- News -------------------- #


# -------------------- Clock -------------------- #
