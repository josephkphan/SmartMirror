from Tkinter import *
from PIL import Image, ImageTk
from project.resources import lookup, var, imagecolor
from datetime import date


class DailyWeather(Frame):
    def __init__(self, parent, day):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.daily_frame = Frame(self, bg=background_color)
        self.daily_frame.pack(side=TOP, anchor=N)
        self.degree_frame = Frame(self.daily_frame, bg=background_color)
        self.degree_frame.pack(side=TOP, anchor=N)

        # Initializing text (raw values) for labels (values to be displayed)
        self.min_temperature_text = ''
        self.max_temperature_text = ''
        self.day_of_week_text = ''
        self.icon_path = ''

        # Initializing the two photos - white version of icon image and the tinted version
        self.icon_photo_tinted, self.icon_photo, self.image = None, None, None

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initializing Labels
        self.min_temperature_label = Label(self.degree_frame, font=(font_style, font_sizes['small']), fg=selected_off,
                                           bg=background_color)
        self.min_temperature_label.pack(side=RIGHT, anchor=N)
        self.max_temperature_label = Label(self.degree_frame, font=(font_style, font_sizes['small']), fg=selected_off,
                                           bg=background_color)
        self.max_temperature_label.pack(side=LEFT, anchor=N)
        self.icon_label = Label(self.daily_frame, bg=background_color)
        self.icon_label.pack(side=TOP, anchor=N, padx=20)
        self.day_of_week_label = Label(self.daily_frame, font=(font_style, font_sizes['small']), fg=selected_off,
                                       bg=background_color)
        self.day_of_week_label.pack(side=TOP, anchor=N)

        self.update_now(day)

    def update_now(self, day):
        # Gathering Daily weather data
        weather_obj = var.weather_data
        max_temperature_txt = str(int(weather_obj['daily']['data'][day]['temperatureMax']))
        min_temperature_txt = str(int(weather_obj['daily']['data'][day]['temperatureMin']))
        sunset_time = weather_obj['daily']['data'][day]['sunsetTime']
        day_of_week = DailyWeather.convert_epoch_time_to_day_of_the_week(sunset_time)
        day_of_week = day_of_week[:3]  # takes first 3 letters
        icon_id = weather_obj['daily']['data'][day]['icon']
        icon = None

        # Updating daily weather if it doesnt match
        if self.max_temperature_text != max_temperature_txt:
            self.max_temperature_text = max_temperature_txt
            self.max_temperature_label.config(text=self.max_temperature_text)
        if self.min_temperature_text != min_temperature_txt:
            self.min_temperature_text = min_temperature_txt
            self.min_temperature_label.config(text=self.min_temperature_text)
        if self.day_of_week_text != day_of_week:
            self.day_of_week_text = day_of_week
            self.day_of_week_label.config(text=self.day_of_week_text)

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
        self.image = self.image.resize(var.font_sizes['medium_icon'], Image.ANTIALIAS)
        self.image = self.image.convert('RGB')
        photo = ImageTk.PhotoImage(self.image)
        self.icon_photo = photo
        self.icon_photo_tinted = ImageTk.PhotoImage(imagecolor.tint(self.image, var.selected_on))
        self.icon_label.config(image=photo)
    # --------------------------- Color ------------------------------ #

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            if self.color_all == var.selected_off:
                self.icon_label.config(image=self.icon_photo)
            else:
                self.icon_label.config(image=self.icon_photo_tinted)
            self.min_temperature_label.config(foreground=self.color_all)
            self.max_temperature_label.config(foreground=self.color_all)
            self.day_of_week_label.config(foreground=self.color_all)

    # ------------------------------ Time ---------------------------------- #

    @staticmethod
    def convert_epoch_time_to_day_of_the_week(epoch_time_in_seconds):
        d = date.fromtimestamp(epoch_time_in_seconds)
        return d.strftime('%A')


    def update_font_size(self):
        self.min_temperature_label.config(font=(var.font_style, var.font_sizes['small']))
        self.max_temperature_label.config(font=(var.font_style, var.font_sizes['small']))
        self.icon_label.config(font=(var.font_style, var.font_sizes['small']))
        self.day_of_week_label.config(font=(var.font_style, var.font_sizes['small']))
