from Tkinter import *
from PIL import Image, ImageTk
from project.resources import var, lookup


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

        # Initialize color for labels
        self.color_temperature = selected_off
        self.color_forecast = selected_off
        self.color_currently = selected_off
        self.color_location = selected_off

        # Initialize Labels
        self.temperature_label = Label(self.degree_frame, font=(font_style, 94), fg=selected_off, bg=background_color)
        self.temperature_label.pack(side=LEFT, anchor=N)
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
                photo = ImageTk.PhotoImage(image)

                self.icon_label.config(image=photo)
                self.icon_label.image = photo
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
        self.change_color_currently(mode)
        self.change_color_forecast(mode)
        self.change_color_temperature(mode)
        self.change_color_location(mode)

    def change_color_temperature(self, mode):
        if self.color_temperature != mode:
            self.color_temperature = mode
            self.temperature_label.config(foreground = self.color_temperature)

    def change_color_forecast(self, mode):
        if self.color_forecast != mode:
            self.color_forecast = mode
            self.forecast_label.config( foreground=self.color_forecast)

    def change_color_currently(self, mode):
        if self.color_currently != mode:
            self.color_currently = mode
            self.currently_label.config(foreground=self.color_currently)

    def change_color_location(self, mode):
        if self.color_location != mode:
            self.color_location = mode
            self.location_label.config(foreground=self.color_location)

    @staticmethod
    def convert_kelvin_to_fahrenheit(kelvin_temp):          # todo create a settings for user!!! <-- COOL IDEA
        return 1.8 * (kelvin_temp - 273) + 32
