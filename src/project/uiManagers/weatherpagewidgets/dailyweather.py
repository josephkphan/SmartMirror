from Tkinter import *
import json
import requests
import traceback
from PIL import Image, ImageTk

import src.project.resources.lookup
from datetime import date
from src.project.resources.var import *


class WeeklyWeather(Frame):
    def __init__(self, parent, day):
        Frame.__init__(self, parent, bg='black')
        self.day_icon,self.icon, self.day_max, self.day_min, self.day_name = None, None, None, None, None

        self.day_icon = Frame(self, bg="black")
        self.day_icon.pack(side=RIGHT, anchor=N)

        self.day_min = Label(self, font=('Helvetica', 14), fg="white", bg="black")
        self.day_min.pack(side=RIGHT, anchor=N)

        self.day_max = Label(self, font=('Helvetica', 14), fg="white", bg="black")
        self.day_max.pack(side=RIGHT, anchor=N)

        self.day_name = Label(self, font=('Helvetica', 14), fg="white", bg="black")
        self.day_name.pack(side=RIGHT, anchor=N)

        self.fill_text(day)

    def fill_text(self, day):
        weather_obj = saved_data['weather']
        max = str(int(weather_obj['daily']['data'][day]['temperatureMax']))
        min = str(int(weather_obj['daily']['data'][day]['temperatureMin']))
        sunset_time = weather_obj['daily']['data'][day]['sunsetTime']
        day_of_week =  WeeklyWeather.convert_epoch_time_to_day_of_the_week(sunset_time)

        self.day_max.config(text=max)
        self.day_min.config(text=min)
        self.day_name.config(text=day_of_week)

        # icon_id = weather_obj['daily']['data'][day]['icon']    todo add this in
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


    @staticmethod
    def convert_epoch_time_to_day_of_the_week(epoch_time_in_seconds):
        d = date.fromtimestamp(epoch_time_in_seconds)
        return d.strftime('%A')




