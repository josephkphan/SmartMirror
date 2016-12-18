from Tkinter import *
from PIL import Image, ImageTk
from project.resources import imagecolor, lookup, var
import datetime


class HourlyWeather(Frame):
    def __init__(self, parent, hour):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)

        self.icon = Frame(self, bg=background_color)
        self.icon.pack(side=RIGHT, anchor=N)

        # Initializing text (raw values) for labels (values to be displayed)
        self.time_text = ''
        self.temperature_text = ''
        self.rain_probability_text = ''

        # Initializing the two photos - white version of icon image and the tinted version
        self.icon_photo_tinted, self.icon_photo = None, None

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initializing Labels
        self.rain_probability_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color, padx=10)
        self.rain_probability_label.pack(side=RIGHT, anchor=N)
        self.temperature_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color, padx=10)
        self.temperature_label.pack(side=RIGHT, anchor=N)
        self.time_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color, padx=15)
        self.time_label.pack(side=RIGHT, anchor=N)

        self.update_now(hour)

    def update_now(self, hour):

        # Gathering Data for hourly weather
        weather_obj = var.saved_data['weather']
        temperature = str(int(weather_obj['hourly']['data'][hour]['apparentTemperature'])) +  u'\N{DEGREE SIGN}'
        time_txt = self.convert_epoch_time_to_datetime(weather_obj['hourly']['data'][hour]['time'])
        time_txt = self.get_time_from_datetime(time_txt)
        prob_rain = weather_obj['hourly']['data'][hour]['precipProbability']
        if prob_rain == 0:
            prob_rain = '0'     # todo change to '' if there isnt any rain
        else:
            prob_rain = str(prob_rain) + '%'            # todo IF > lets say 30, then ADD A RAINDROP ONTO THE HOUR <---

        # Updates hourly weather if its different
        if self.time_text != time_txt:
            self.time_text = time_txt
            self.time_label.config(text=self.time_text)
        if self.temperature_text != temperature:
            self.temperature_text = temperature
            self.temperature_label.config(text=self.temperature_text)
        if self.rain_probability_text != prob_rain:
            self.rain_probability_text = prob_rain
            self.rain_probability_label.config(text=self.rain_probability_text)

        # icon_id = weather_obj['daily']['data'][hour]['icon']    todo add this in. This is the icon per hour?
        # icon2 = None                                           #todo maybe only show rain? since we only have rain %
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

    # --------------------------- Color ------------------------------ #

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode

            self.rain_probability_label.config(foreground=self.color_all)
            self.temperature_label.config(foreground=self.color_all)
            self.time_label.config(foreground=self.color_all)

    # --------------------------- Time Methods ------------------------------ #


    @staticmethod
    def convert_epoch_time_to_datetime(epoch_time):
        begin_time = datetime.datetime(1970, 1, 1)
        added = datetime.timedelta(seconds=(epoch_time - 28800))  # todo change to adjust to time zone!!!
        time = begin_time + added  # todo its only set to PST
        return time

    @staticmethod
    def get_time_from_datetime(d_time):
        spaces = ' '
        if d_time.hour > 12:  # finds out if its AM OR PM
            hour = str(d_time.hour - 12)  # Adjust time so it's not in military time
            if len(hour) == 1:
                spaces = '   '
            end = 'PM'
        else:
            hour = str(d_time.hour)
            if len(hour) == 1:
                spaces = '   '
            end = 'AM'
        return hour + spaces + end
