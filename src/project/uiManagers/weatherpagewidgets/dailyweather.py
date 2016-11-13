from Tkinter import *
from PIL import Image, ImageTk
import src.project.resources.lookup
from datetime import date
from src.project.resources.var import *


class WeeklyWeather(Frame):
    def __init__(self, parent, day):
        Frame.__init__(self, parent, bg=background_color)

        self.day_icon = Frame(self, bg=background_color)
        self.day_icon.pack(side=RIGHT, anchor=N)

        # Initializing text for labels
        self.min = ''
        self.max = ''
        self.name = ''
        self.day_of_week = ''

        # Initializing Labels
        self.min_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color)
        self.min_label.pack(side=RIGHT, anchor=N)
        self.max_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color)
        self.max_label.pack(side=RIGHT, anchor=N)
        self.day_of_week_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color)
        self.day_of_week_label.pack(side=RIGHT, anchor=N)

        self.update_now(day)

    def update_now(self, day):
        # Gathering Daily weather data
        weather_obj = saved_data['weather']
        max_txt = str(int(weather_obj['daily']['data'][day]['temperatureMax']))
        min_txt = str(int(weather_obj['daily']['data'][day]['temperatureMin']))
        sunset_time = weather_obj['daily']['data'][day]['sunsetTime']
        day_of_week = WeeklyWeather.convert_epoch_time_to_day_of_the_week(sunset_time)

        # Updating daily weather if it doesnt match
        if self.max != max_txt:
            self.max = max_txt
            self.max_label.config(text=self.max)
        if self.min != min_txt:
            self.min = min_txt
            self.min_label.config(text=self.min)
        if self.day_of_week != day_of_week:
            self.day_of_week = day_of_week
            self.day_of_week_label.config(text=self.day_of_week)

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




