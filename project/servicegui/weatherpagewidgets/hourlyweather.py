from Tkinter import *
from PIL import Image, ImageTk
from resources import imagecolor, lookup, var
import datetime


class HourlyWeather(Frame):
    def __init__(self, parent, hour):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.hourly_temperature_frame = Frame(self, bg=background_color)
        self.hourly_temperature_frame.pack(side=LEFT, anchor=N)

        self.icon = Frame(self, bg=background_color)
        self.icon.pack(side=RIGHT, anchor=N)

        # Initializing text (raw values) for labels (values to be displayed)
        self.time_text = ''
        self.temperature_text = ''
        self.rain_probability_text = ''
        self.icon_path = ''

        # Initializing the two photos - white version of icon image and the tinted version
        self.icon_photo_tinted, self.icon_photo, self.image = None, None, None

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initializing Labels
        self.icon_label = Label(self, bg=background_color)
        self.icon_label.pack(side=RIGHT, anchor=N, padx=20)
        self.temperature_label = Label(self.hourly_temperature_frame, font=(font_style,  font_sizes['small']), fg=selected_off, bg=background_color, padx=10)
        self.temperature_label.pack(side=RIGHT, anchor=N)
        self.time_label = Label(self.hourly_temperature_frame, font=(font_style, font_sizes['small']), fg=selected_off, bg=background_color, padx=15)
        self.time_label.pack(side=RIGHT, anchor=N)

        self.update_now(hour)

    def update_now(self, hour):

        # Gathering Data for hourly weather
        weather_obj = var.weather_data
        temperature = str(int(weather_obj['hourly']['data'][hour]['apparentTemperature'])) +  u'\N{DEGREE SIGN}'
        time_txt = self.convert_epoch_time_to_datetime(weather_obj['hourly']['data'][hour]['time'])
        time_txt = self.get_time_from_datetime(time_txt)
        prob_rain = weather_obj['hourly']['data'][hour]['precipProbability']
        icon_id = weather_obj['hourly']['data'][hour]['icon']
        icon = None

        # ---------- Precipitation Code -----
        # if prob_rain == 0:
        #     prob_rain = '0'
        # else:
        #     prob_rain = str(prob_rain) + '%'

        # Updates hourly weather if its different
        if self.time_text != time_txt:
            self.time_text = time_txt
            self.time_label.config(text=self.time_text)
        if self.temperature_text != temperature:
            self.temperature_text = temperature
            self.temperature_label.config(text=self.temperature_text)

        # ----- Precipitation Code -----
        # if self.rain_probability_text != prob_rain:
        #     self.rain_probability_text = prob_rain
        #     self.rain_probability_label.config(text=self.rain_probability_text)

        # Find the corresponding icon in lookup.py
        if icon_id in lookup.icon:
            icon = lookup.icon[icon_id]

        if icon is not None:
            if self.icon_path != icon:
                self.icon_path = icon
                self.image = Image.open(icon)
                self.create_photo()
        else:
            # Remove Image
            self.icon_label.config(image='')

        if self.icon_photo is not None:
            self.create_photo()
        self.update_font_size()

    def create_photo(self):
        self.image = self.image.resize(var.font_sizes['small_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        photo = ImageTk.PhotoImage(self.image)
        self.icon_photo = photo
        self.icon_photo_tinted = ImageTk.PhotoImage(imagecolor.tint(self.image, var.selected_on))
        self.icon_label.config(image=photo)

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            if self.color_all == var.selected_off:
                self.icon_label.config(image=self.icon_photo)
            else:
                self.icon_label.config(image=self.icon_photo_tinted)
            # self.rain_probability_label.config(foreground=self.color_all)
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

    def update_font_size(self):
        self.temperature_label.config(font=(var.font_style, var.font_sizes['small']))
        self.time_label.config(font=(var.font_style, var.font_sizes['small']))