from Tkinter import *
import json
import requests
import traceback
from PIL import Image, ImageTk

import src.project.resources.lookup
from datetime import date
from src.project.resources.var import *
import datetime


class CurrentWeather(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.probdrain = ''
        self.sunrise = ''
        self.sunset = ''
        self.locationLbl = Label(self, font=('Helvetica', 28), fg="white", bg="black")
        self.locationLbl.pack(side=TOP, anchor=N)
        self.currentlyLbl = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        self.currentlyLbl.pack(side=TOP, anchor=N)
        self.degreeFrm = Frame(self, bg="black")
        self.degreeFrm.pack(side=TOP, anchor=N)
        self.temperatureLbl = Label(self.degreeFrm, font=('Helvetica', 70), fg="white", bg="black")
        self.temperatureLbl.pack(side=LEFT, anchor=N)
        self.probDrainLbl = Label(self.degreeFrm, font=('Helvetica', 18), fg="white", bg="black")
        self.probDrainLbl.pack(side=TOP, anchor=N)
        self.sunriseLbl = Label(self.degreeFrm, font=('Helvetica', 18), fg="white", bg="black")
        self.sunriseLbl.pack(side=TOP, anchor=N)
        self.sunsetLbl = Label(self.degreeFrm, font=('Helvetica', 18), fg="white", bg="black")
        self.sunsetLbl.pack(side=TOP, anchor=N)
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

        probdrain = weather_obj['daily']['data'][0]['precipProbability']
        self.probDrainLbl.config(text="Chance of Rain: " + str(probdrain) + "%")

        sunrise = self.convert_epoch_time_to_datetime(weather_obj['daily']['data'][0]['sunriseTime'])
        self.sunriseLbl.config(text= "Sunrise Time: " + self.get_time_from_datetime(sunrise))

        sunset = self.convert_epoch_time_to_datetime(weather_obj['daily']['data'][0]['sunsetTime'])
        self.sunsetLbl.config(text="Sunset time: " + self.get_time_from_datetime(sunset))

        if self.currently != currently2:
            self.currently = currently2
            self.currentlyLbl.config(text=currently2)
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

    def refresh_weather_data(self):
        self.update_weather()  # todo Check is this is right

    @staticmethod
    def convert_epoch_time_to_datetime(epoch_time):
        begin_time = datetime.datetime(1970, 1, 1)
        added = datetime.timedelta(seconds=(epoch_time - 28800))
        time = begin_time + added
        return time

    @staticmethod
    def get_time_from_datetime(time):
        finaltime = ''
        hour = ''
        minute = ''
        end=''
        if time.hour > 12:                  # finds out if its AM OR PM
            hour = str(time.hour - 12)      # Adjust time so it's not in military time
            end = 'PM'
        else:
            hour = str(time.hour)
            end = 'AM'

        if len(str(time.minute)) == 1:
            minute +='0'
        minute+=str(time.minute)

        finaltime = hour + ':' + minute + ' ' + end
        return finaltime

