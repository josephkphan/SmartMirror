from Tkinter import *
from PIL import Image, ImageTk
from resources import imagecolor, lookup, var
import datetime


class CurrentWeather(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.degree_frame = Frame(self, bg=background_color)
        self.degree_frame.pack(side=TOP, anchor=N)

        # Initializing text (raw values) for labels (values to be displayed)
        self.temperature_text = ''
        self.icon_path = ''
        self.location_text = ''
        self.currently_text = ''
        self.summary_text = ''
        self.rain_probability_text = ''
        self.forecast_text = ''
        self.sunrise_text = ''
        self.sunset_text = ''

        # Initializing the two photos - white version of icon image and the tinted version
        self.icon_photo_tinted, self.icon_photo, self.image = None, None, None

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initializing Labels
        self.temperature_label = Label(self.degree_frame, font=(font_style, font_sizes['bigger']), fg=selected_off,
                                       bg=background_color)
        self.temperature_label.pack(side=LEFT, anchor=N)
        self.icon_label = Label(self.degree_frame, bg=background_color)
        self.icon_label.pack(side=LEFT, anchor=N, padx=20)
        self.location_label = Label(self, font=(font_style, font_sizes['title']), fg=selected_off, bg=background_color)
        self.location_label.pack(side=TOP, anchor=N)
        self.currently_label = Label(self, font=(font_style, font_sizes['text']), fg=selected_off, bg=background_color)
        self.currently_label.pack(side=TOP, anchor=N)
        self.summary_label = Label(self, font=(font_style, font_sizes['text']), fg=selected_off, bg=background_color)
        self.summary_label.pack(side=TOP, anchor=N)
        self.rain_probability_label = Label(self, font=(font_style, font_sizes['text']), fg=selected_off,
                                            bg=background_color)
        self.rain_probability_label.pack(side=TOP, anchor=N)
        self.sunrise_time_label = Label(self, font=(font_style, font_sizes['text']), fg=selected_off,
                                        bg=background_color)
        self.sunrise_time_label.pack(side=TOP, anchor=N)
        self.sunset_time_label = Label(self, font=(font_style, font_sizes['text']), fg=selected_off,
                                       bg=background_color)
        self.sunset_time_label.pack(side=TOP, anchor=N)

        self.update_now()

    def update_now(self):
        # Gets Location Information
        location_obj = var.location_data
        location = "%s, %s" % (location_obj['city'], location_obj['region_code'])

        # Gets Weather Information
        weather_obj = var.weather_data
        icon_id = weather_obj['daily']['data'][0]['icon']
        icon = None
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
        if self.summary_text != summary:
            self.summary_text = summary
            self.summary_label.config(text=self.summary_text)
        if self.rain_probability_text != prob_rain:
            self.rain_probability_text = prob_rain
            self.rain_probability_label.config(text=self.rain_probability_text)
        if self.sunrise_text != sunrise:
            self.sunrise_text = sunrise
            self.sunrise_time_label.config(text=self.sunrise_text)
        if self.sunset_text != sunset:
            self.sunset_text = sunset
            self.sunset_time_label.config(text=self.sunset_text)
        if self.currently_text != currently:
            self.currently_text = currently
            self.currently_label.config(text=self.currently_text)
        if self.temperature_text != temperature:
            self.temperature_text = temperature
            self.temperature_label.config(text=self.temperature_text)
        if self.location_text != location:
            if location == ", ":
                self.location_text = "Cannot Pinpoint Location"
                self.location_label.config(text="Cannot Pinpoint Location")
            else:
                self.location_text = location
                self.location_label.config(text=self.location_text)

        # Find the corresponding icon in lookup.py
        if icon_id in lookup.icon:
            icon = lookup.icon[icon_id]

        if icon is not None:
            if self.icon_path != icon:
                self.icon_path = icon
                self.image = Image.open(icon)
                self.create_photo()
        else:
            # remove image
            self.icon_label.config(image='')

        if self.icon_photo is not None:
            self.create_photo()

        self.update_font_size()

    def create_photo(self):
        self.image = self.image.resize(var.font_sizes['large_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        photo = ImageTk.PhotoImage(self.image)
        self.icon_photo = photo
        self.icon_photo_tinted = ImageTk.PhotoImage(imagecolor.tint(self.image, var.selected_on))
        self.icon_label.config(image=photo)
        self.icon_label.image = photo
    # --------------------------- Color ------------------------------ #

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            if self.color_all == var.selected_off:
                self.icon_label.config(image=self.icon_photo)

            else:
                self.icon_label.config(image=self.icon_photo_tinted)

            self.temperature_label.config(foreground=self.color_all)
            self.location_label.config(foreground=self.color_all)
            self.currently_label.config(foreground=self.color_all)
            self.summary_label.config(foreground=self.color_all)
            self.rain_probability_label.config(foreground=self.color_all)
            self.sunrise_time_label.config(foreground=self.color_all)
            self.sunset_time_label.config(foreground=self.color_all)

    # --------------------------- Time Methods ------------------------------ #

    @staticmethod
    def convert_epoch_time_to_datetime(epoch_time):
        begin_time = datetime.datetime(1970, 1, 1)
        added = datetime.timedelta(seconds=(epoch_time - 28800))  # todo change to adjust to time zone!!!
        time = begin_time + added  # todo its only set to PST
        return time

    @staticmethod
    def get_time_from_datetime(time):
        minute = ''
        if time.hour > 12:  # finds out if its AM OR PM
            hour = str(time.hour - 12)  # Adjust time so it's not in military time
            end = 'PM'
        else:
            hour = str(time.hour)
            end = 'AM'
        if len(str(time.minute)) == 1:
            minute += '0'
        minute += str(time.minute)
        return hour + ':' + minute + ' ' + end

    def update_font_size(self):
        self.temperature_label.config(font=(var.font_style, var.font_sizes['bigger']))
        self.icon_label.config(font=(var.font_style, var.font_sizes['text']))
        self.location_label.config(font=(var.font_style, var.font_sizes['text']))
        self.currently_label.config(font=(var.font_style, var.font_sizes['text']))
        self.summary_label.config(font=(var.font_style, var.font_sizes['text']))
        self.rain_probability_label.config(font=(var.font_style, var.font_sizes['text']))
        self.sunrise_time_label.config(font=(var.font_style, var.font_sizes['text']))
        self.sunset_time_label.config(font=(var.font_style, var.font_sizes['text']))