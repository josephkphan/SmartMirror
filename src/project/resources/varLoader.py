import src.project.resources.var
import json
import time


# todo Make this work!!!!
def write_json_to_file():
    # Open a file for writing

    out_file = open("data.json", "w")
    # Save the data into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(src.project.resources.var.saved_data, out_file, indent=4)
    out_file.close()


# Reading data back
def read_json_from_file():
    with open('data.json', 'r') as f:
        src.project.resources.var.saved_data = json.load(f)


def update_data(weather_data, location_data, news_data):
    # Converting to Json
    read_json_from_file()
    if weather_data is not None:
        src.project.resources.var.saved_data['weather'] = weather_data

    if location_data is not None:
        src.project.resources.var.saved_data['location'] = location_data

    if news_data is not None:
        headlines = {}
        links = {}
        for i in range(0, 5):
            headlines[str(i)] = news_data.entries[i].title
            links[str(i)] = news_data.entries[i].links
            src.project.resources.var.saved_data['news_headlines'] = headlines
            src.project.resources.var.saved_data['news_links'] = links
        src.project.resources.var.saved_data['last_updated'] = time.time()
    write_json_to_file()
