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
        # Init Frames
        Frame.__init__(self, parent, bg=background_color)
        self.degree_frame = Frame(self, bg=background_color)
        self.degree_frame.pack(side=TOP, anchor=N)

        # Initializing text for labels
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.prob_rain = ''
        self.sunrise = ''
        self.sunset = ''
        self.summary = ''

        # Initializing Labels
        self.temperature_label = Label(self.degree_frame, font=(font_style, 70), fg=selected_off, bg=background_color)
        self.temperature_label.pack(side=LEFT, anchor=N)
        self.icon_label = Label(self.degree_frame, bg=background_color)
        self.icon_label.pack(side=LEFT, anchor=N, padx=20)

        self.location_label = Label(self, font=(font_style, 28), fg=selected_off, bg=background_color)
        self.location_label.pack(side=TOP, anchor=N)
        self.currently_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.currently_label.pack(side=TOP, anchor=N)
        self.summary_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.summary_label.pack(side=TOP, anchor=N)
        self.prob_rain_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.prob_rain_label.pack(side=TOP, anchor=N)
        self.sunrise_time_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.sunrise_time_label.pack(side=TOP, anchor=N)
        self.sunset_time_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.sunset_time_label.pack(side=TOP, anchor=N)
        self.update_weather()

    def update_weather(self):
        # Gets Location Information
        location_obj = saved_data['location']
        location = "%s, %s" % (location_obj['city'], location_obj['region_code'])

        # Gets Weather Information
        weather_obj = saved_data['weather']
        icon_id = weather_obj['daily']['data'][0]['icon']
        icon2 = None
        degree_sign = u'\N{DEGREE SIGN}'
        temperature = "%s%s" % (str(int(weather_obj['currently']['temperature'])), degree_sign)
        currently = weather_obj['currently']['summary']
        currently = "Current Weather: " + currently
        summary = weather_obj['daily']['data'][0]['summary']
        summary = 'Day Summary: ' + summary
        prob_rain = weather_obj['daily']['data'][0]['precipProbability']
        prob_rain = "Chance of Rain: " + str(prob_rain) + "%"
        sunrise = self.convert_epoch_time_to_datetime(weather_obj['daily']['data'][0]['sunriseTime'])
        sunrise = "Sunrise Time: " + self.get_time_from_datetime(sunrise)
        sunset = self.convert_epoch_time_to_datetime(weather_obj['daily']['data'][0]['sunsetTime'])
        sunset = "Sunset time: " + self.get_time_from_datetime(sunset)

        # Updates information if different
        if self.summary != summary:
            self.summary = summary
            self.summary_label.config(text=self.summary)
        if self.prob_rain != prob_rain:
            self.prob_rain = prob_rain
            self.prob_rain_label.config(text=self.prob_rain)
        if self.sunrise != sunrise:
            self.sunrise = sunrise
            self.sunrise_time_label.config(text=self.sunrise)
        if self.sunset != sunset:
            self.sunset = sunset
            self.sunset_time_label.config(text=self.sunset)
        if self.currently != currently:
            self.currently = currently
            self.currently_label.config(text=self.currently)
        if self.temperature != temperature:
            self.temperature = temperature
            self.temperature_label.config(text=self.temperature)
        if self.location != location:
            if location == ", ":
                self.location = "Cannot Pinpoint Location"
                self.location_label.config(text="Cannot Pinpoint Location")
            else:
                self.location = location
                self.location_label.config(text=self.location)

        if icon_id in src.project.resources.lookup.icon:
            icon2 = src.project.resources.lookup.icon[icon_id]

        if icon2 is not None:
            if self.icon != icon2:
                self.icon = icon2
                image = Image.open(icon2)
                image = image.resize((100, 100), Image.ANTIALIAS)
                image = image.convert('RGB')
                photo = ImageTk.PhotoImage(image)

                self.icon_label.config(image=photo)
                self.icon_label.image = photo
        else:
            # remove image
            self.icon_label.config(image='')


    def refresh_weather_data(self):
        self.update_weather()  # todo Check is this is right

    @staticmethod
    def convert_epoch_time_to_datetime(epoch_time):
        begin_time = datetime.datetime(1970, 1, 1)
        added = datetime.timedelta(seconds=(epoch_time - 28800))  # todo change to adjust to time zone!!!
        time = begin_time + added  # todo its only set to PST
        return time

    @staticmethod
    def get_time_from_datetime(time):
        finaltime = ''
        hour = ''
        minute = ''
        end = ''
        if time.hour > 12:  # finds out if its AM OR PM
            hour = str(time.hour - 12)  # Adjust time so it's not in military time
            end = 'PM'
        else:
            hour = str(time.hour)
            end = 'AM'
        if len(str(time.minute)) == 1:
            minute += '0'
        minute += str(time.minute)

        finaltime = hour + ':' + minute + ' ' + end
        return finaltime
