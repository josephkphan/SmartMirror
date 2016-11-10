from Tkinter import *
import json
import requests
import traceback
from PIL import Image, ImageTk
import datetime
import src.project.resources.lookup
from datetime import date
from src.project.resources.var import *


class HourlyWeather(Frame):
    def __init__(self, parent, day):
        Frame.__init__(self, parent, bg='black')
        self.time = ''
        self.temp = ''

        self.timeLbl = Label(self, font=('Helvetica', 14), fg="white", bg="black")
        self.timeLbl.pack(side=RIGHT, anchor=N)

        self.icon = Frame(self, bg="black")
        self.icon.pack(side=RIGHT, anchor=N)

        self.tempLbl = Label(self, font=('Helvetica', 14), fg="white", bg="black")
        self.tempLbl.pack(side=RIGHT, anchor=N)

        self.fill_text(day)

    def fill_text(self, hour):
        weather_obj = saved_data['weather']
        temperature = str(int(weather_obj['hourly']['data'][hour]['apparentTemperature']))
        time = self.convert_epoch_time_to_datetime(weather_obj['hourly']['data'][hour]['time'])
        self.timeLbl.config(text=self.get_time_from_datetime(time))

        self.tempLbl.config(text=temperature +  u'\N{DEGREE SIGN}')

        # icon_id = weather_obj['daily']['data'][hour]['icon']    todo add this in
        # icon2 = None
        #
        # if icon_id in src.project.resources.lookup.icon:
        #     icon2 = src.project.resources.lookup.icon[icon_id]
        #
        # if icon2 is not None:
        #     if self.icon != icon2:
        #         self.icon = icon2
        #         image = Image.open(icon2)
        #         image = image.resize((100, 100), Image.ANTIALIAS)
        #         image = image.convert('RGB')
        #         photo = ImageTk.PhotoImage(image)
        #
        #         self.day_icon.config(image=photo)
        #         self.day_icon.image = photo
        # else:
        #     # remove image
        #     self.day_icon.config(image='')

    # todo THIS METHOD IS USED TWICE?? PUT IT IN ITS OWN FILE

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
        if time.hour > 12:  # finds out if its AM OR PM
            hour = str(time.hour - 12)  # Adjust time so it's not in military time
            end = 'PM'
        else:
            hour = str(time.hour)
            end = 'AM'

        finaltime = hour + ' ' + end
        return finaltime
