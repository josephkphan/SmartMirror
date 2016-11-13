from Tkinter import *
from PIL import Image, ImageTk
from src.project.resources import lookup
from datetime import date
from src.project.resources import var


class WeeklyWeather(Frame):
    def __init__(self, parent, day):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        self.daily_frame = Frame(self, bg=background_color)
        self.daily_frame.pack(side=TOP, anchor=N)
        self.degree_frame = Frame(self.daily_frame, bg=background_color)
        self.degree_frame.pack(side=TOP, anchor=N)

        # Initializing text for labels
        self.min = ''
        self.max = ''
        self.name = ''
        self.day_of_week = ''
        self.icon = ''

        # Initializing Labels
        self.min_label = Label(self.degree_frame, font=(font_style, 14), fg=selected_off, bg=background_color)
        self.min_label.pack(side=RIGHT, anchor=N)
        self.max_label = Label(self.degree_frame, font=(font_style, 14), fg=selected_off, bg=background_color)
        self.max_label.pack(side=LEFT, anchor=N)
        self.icon_label = Label(self.daily_frame, bg=background_color)
        self.icon_label.pack(side=TOP, anchor=N, padx=20)
        self.day_of_week_label = Label(self.daily_frame, font=(font_style, 14), fg=selected_off, bg=background_color)
        self.day_of_week_label.pack(side=TOP, anchor=N)

        self.update_now(day)

    def update_now(self, day):
        # Gathering Daily weather data
        weather_obj = var.saved_data['weather']
        max_txt = str(int(weather_obj['daily']['data'][day]['temperatureMax']))
        min_txt = str(int(weather_obj['daily']['data'][day]['temperatureMin']))
        sunset_time = weather_obj['daily']['data'][day]['sunsetTime']
        day_of_week = WeeklyWeather.convert_epoch_time_to_day_of_the_week(sunset_time)
        day_of_week = day_of_week[:3]  # takes first 3 letters
        icon_id = weather_obj['daily']['data'][day]['icon']
        icon = None

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

        if icon_id in lookup.icon:
            icon = lookup.icon[icon_id]

        if icon is not None:
            if self.icon != icon:
                self.icon = icon
                image = Image.open(icon)
                image = image.resize((50, 50), Image.ANTIALIAS)
                image = image.convert('RGB')
                photo = ImageTk.PhotoImage(image)

                self.icon_label.config(image=photo)
                self.icon_label.image = photo
        else:
            # remove image
            self.icon_label.config(image='')

    @staticmethod
    def convert_epoch_time_to_day_of_the_week(epoch_time_in_seconds):
        d = date.fromtimestamp(epoch_time_in_seconds)
        return d.strftime('%A')
