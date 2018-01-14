import var
import json


# ----------------------- Saved Web Data ----------------------- #
def save_data_to_json_file(data,file_path):
    out_file = open(file_path, "w")
    json.dump(data, out_file, indent=4)
    out_file.close()


# ----------------------- Mirror User Interface ----------------------- #
def change_main_page_top(new_widget):
    if not var.preferences[new_widget]:
        var.preferences['weather'], var.preferences['time'] = var.preferences['time'], var.preferences['weather']
    save_data_to_json_file(var.preferences,var.file_paths['preferences'])


def change_main_page_bottom(new_widget):
    var.preferences[var.preferences['show_this_on_bottom_of_main_page']] = False  # turns old color off
    var.preferences[new_widget] = True  # Turns new color on
    var.preferences['show_this_on_bottom_of_main_page'] = new_widget  # updates new color
    save_data_to_json_file(var.preferences,var.file_paths['preferences'])


# ----------------------- Preferences ----------------------- #
def change_color_scheme(new_color):
    var.preferences[var.preferences['color']] = False  # turns old color off
    var.preferences[new_color] = True  # Turns new color on
    var.preferences['color'] = new_color  # updates new color
    var.selected_on = var.color_hex_codes[new_color]  # PROBLEM
    save_data_to_json_file(var.preferences,var.file_paths['preferences'])


def change_font_size(new_size):
    var.preferences[var.preferences['font_size_current']] = False  # turns old color off
    var.preferences[new_size] = True  # Turns new color on
    var.preferences['font_size_current'] = new_size  # updates new color
    update_font_size()
    save_data_to_json_file(var.preferences,var.file_paths['preferences'])


def update_font_size():
    if var.preferences['font_size_current'] == 'small':
        var.font_sizes = var.font_size_small
    elif var.preferences['font_size_current'] == 'medium':
        var.font_sizes = var.font_size_medium
    else:
        var.font_sizes = var.font_size_large


# ----------------------- Stocks ----------------------- #
def update_stocks(new_stocks):
    save_data_to_json_file(new_stocks,var.file_paths['stocks'])


# ----------------------- To Do List ----------------------- #
def update_to_do_list(new_to_do_list):
    save_data_to_json_file(new_to_do_list,var.file_paths['to_do_list'])


# ----------------------- Maps Settings ----------------------- #
def update_maps(new_maps):
    save_data_to_json_file(new_maps,var.file_paths['gmap'])


# -------------------- API Keys -------------------- #
def update_keys(new_keys):
    save_data_to_json_file(new_keys,var.file_paths['key'])


# -------------------- User Profile -------------------- #
def update_profile(new_profile_data):
    save_data_to_json_file(new_profile_data,var.file_paths['profile'])


# ------------------------ Other Data -------------------------- #
def change_other_data(key, val):
    var.other_data[key] = val
    save_data_to_json_file(var.other_data, var.file_paths['other'])


# ------------------------ Miscellaneous Functions -------------------------- #
def get_data_from_json_file(file_name):
    try:
        with open(file_name) as f:
            return json.load(f)
    except IOError as e:
        print 'ERROR: Could not read ' + file_name
        if file_name == 'other.json':
            var.other_data['manual_mode'] = True
            save_data_to_json_file(var.other_data, var.file_paths['other'])
        elif file_name == 'preferences.json':
            reset_preferences_to_default()


def reset_preferences_to_default():
    var.preferences['color'] = 'yellow'
    var.preferences['blue'] = False
    var.preferences['green'] = False
    var.preferences['orange'] = False
    var.preferences['pink'] = False
    var.preferences['purple'] = False
    var.preferences['red'] = False
    var.preferences['yellow'] = True
    # Font Size Preferences
    # Only one of these choices can be true at a time
    var.preferences['font_size_current'] = 'medium'
    var.preferences['small'] = False
    var.preferences['medium'] = True
    var.preferences['large'] = False

    save_data_to_json_file(var.preferences,var.file_paths['preferences'])  # Saves to File
