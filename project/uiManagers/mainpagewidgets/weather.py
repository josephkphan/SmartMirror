from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, lookup, imagecolor


class Weather(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        self.degree_frame = Frame(self, bg=background_color)  # creates a sub Frame so icon can be on left or right
        self.degree_frame.pack(side=TOP, anchor=W)

        # Initialize text for labels
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''

        # Initialize boolean color variable for all labels
        self.color_all = selected_off

        # Initialize Labels
        self.temperature_label = Label(self.degree_frame, font=(font_style, 94), fg=selected_off, bg=background_color)
        self.temperature_label.pack(side=LEFT, anchor=N)
        self.photo, self.photo_on = None, None
        self.icon_label = Label(self.degree_frame, bg=background_color)
        self.icon_label.pack(side=LEFT, anchor=N, padx=20)

        self.currently_label = Label(self, font=(font_style, 28), fg=selected_off, bg=background_color)
        self.currently_label.pack(side=TOP, anchor=W)
        self.forecast_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.forecast_label.pack(side=TOP, anchor=W)
        self.location_label = Label(self, font=(font_style, 18), fg=selected_off, bg=background_color)
        self.location_label.pack(side=TOP, anchor=W)
        self.update()

    def update(self):
        print "UPDATING WEATHER INFO ON SCREEN"

        # Getting location related data
        location_obj = var.saved_data['location']
        location = "%s, %s" % (location_obj['city'], location_obj['region_code'])

        # Getting weather related data
        weather_obj = var.saved_data['weather']
        degree_sign = u'\N{DEGREE SIGN}'
        temperature = "%s%s" % (str(int(weather_obj['currently']['temperature'])), degree_sign)
        currently = weather_obj['currently']['summary']
        forecast = weather_obj["hourly"]["summary"]
        icon_id = weather_obj['currently']['icon']
        icon = None

        # Looking up icon
        if icon_id in lookup.icon:
            icon = lookup.icon[icon_id]
        if icon is not None:
            if self.icon != icon:
                self.icon = icon
                image = Image.open(icon)
                image = image.resize((100, 100), Image.ANTIALIAS)
                image = image.convert('RGB')
                self.photo = ImageTk.PhotoImage(image)
                self.photo_on = ImageTk.PhotoImage(imagecolor.tint(image, var.selected_on))
                self.icon_label.config(image=self.photo)
                self.icon_label.image = self.photo

        else:
            # remove image
            self.icon_label.config(image='')

        # Updating weather data
        if self.currently != currently:
            self.currently = currently
            self.currently_label.config(text=self.currently)
        if self.forecast != forecast:
            self.forecast = forecast
            self.forecast_label.config(text=self.forecast)
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

    # -------------------------- Coloring --------------------------- #

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            if self.color_all == var.selected_on:
                self.icon_label.config(image=self.photo_on)
            else:
                self.icon_label.config(image=self.photo)
            self.temperature_label.config(foreground=self.color_all)
            self.forecast_label.config(foreground=self.color_all)
            self.currently_label.config(foreground=self.color_all)
            self.location_label.config(foreground=self.color_all)

    @staticmethod
    def convert_kelvin_to_fahrenheit(kelvin_temp):  # todo create a settings for user!!! <-- COOL IDEA
        return 1.8 * (kelvin_temp - 273) + 32
