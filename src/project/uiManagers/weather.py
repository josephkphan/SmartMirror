from Tkinter import *
import json
import requests
import traceback
from PIL import Image, ImageTk

import src.project.resources.lookup

from src.project.resources.var import *


class Weather(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.temperatureLbl = Label(self.degreeFrm, font=('Helvetica', 94), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.iconLbl = Label(self.degreeFrm, bg="black")
        self.iconLbl.pack(side=LEFT, anchor=N, padx=20)
        self.currentlyLbl = Label(self, font=('Helvetica', 28), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=W)
        self.forecastLbl = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.forecastLbl.pack(side=TOP, anchor=W)
        self.locationLbl = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=W)
        self.update_weather()

    def update_weather(self):
        location_obj = saved_data['location']

        lat = location_obj['latitude']
        lon = location_obj['longitude']

        # print "Lat : " + str(lat) + "  |  Lon : " + str(lon)

        location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])

        weather_obj = saved_data['weather']

        degree_sign = u'\N{DEGREE SIGN}'
        temperature2 = "%s%s" % (str(int(weather_obj['currently']['temperature'])), degree_sign)
        currently2 = weather_obj['currently']['summary']
        forecast2 = weather_obj["hourly"]["summary"]

        icon_id = weather_obj['currently']['icon']
        icon2 = None

        if icon_id in src.project.resources.lookup.icon:
            icon2 = src.project.resources.lookup.icon[icon_id]

        if icon2 is not None:
            if self.icon != icon2:
                self.icon = icon2
                image = Image.open(icon2)
                image = image.resize((100, 100), Image.ANTIALIAS)
                image = image.convert('RGB')
                photo = ImageTk.PhotoImage(image)

                self.iconLbl.config(image=photo)
                self.iconLbl.image = photo
        else:
            # remove image
            self.iconLbl.config(image='')

        if self.currently != currently2:
            self.currently = currently2
            self.currentlyLbl.config(text=currently2)
        if self.forecast != forecast2:
            self.forecast = forecast2
            self.forecastLbl.config(text=forecast2)
        if self.temperature != temperature2:
            self.temperature = temperature2
            self.temperatureLbl.config(text=temperature2)
        if self.location != location2:
            if location2 == ", ":
                self.location = "Cannot Pinpoint Location"
                self.locationLbl.config(text="Cannot Pinpoint Location")
            else:
                self.location = location2
                self.locationLbl.config(text=location2)

    def change_color_to_yellow(self):
        self.temperatureLbl.config(foreground="yellow")
        self.currentlyLbl.config(foreground="yellow")
        self.forecastLbl.config(foreground="yellow")
        self.locationLbl.config(foreground="yellow")

    def change_color_to_white(self):
        self.temperatureLbl.config(foreground="white")
        self.currentlyLbl.config(foreground="white")
        self.forecastLbl.config(foreground="white")
        self.locationLbl.config(foreground="white")

    def refresh_weather_data(self):
        self.update_weather()  # todo Check is this is right

    @staticmethod
    def convert_kelvin_to_fahrenheit(kelvin_temp):
        return 1.8 * (kelvin_temp - 273) + 32
