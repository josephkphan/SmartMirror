from Tkinter import *
import datetime
from PIL import Image, ImageTk
import src.project.resources.lookup
from src.project.resources.var import *


class HourlyWeather(Frame):
    def __init__(self, parent, hour):
        Frame.__init__(self, parent, bg=background_color)

        self.icon = Frame(self, bg=background_color)
        self.icon.pack(side=RIGHT, anchor=N)

        # Initializing Label texts
        self.time = ''
        self.temperature = ''

        # Initializing Labels
        self.temperature_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color, padx=10)
        self.temperature_label.pack(side=RIGHT, anchor=N)
        self.time_label = Label(self, font=(font_style, 14), fg=selected_off, bg=background_color, padx=15)
        self.time_label.pack(side=RIGHT, anchor=N)

        self.update_now(hour)

    def update_now(self, hour):

        # Gathering Data for hourly weather
        weather_obj = saved_data['weather']
        temperature = str(int(weather_obj['hourly']['data'][hour]['apparentTemperature'])) +  u'\N{DEGREE SIGN}'
        time_txt = self.convert_epoch_time_to_datetime(weather_obj['hourly']['data'][hour]['time'])
        time_txt = self.get_time_from_datetime(time_txt)

        # Updates hourly weather if its different
        if self.time != time_txt:
            self.time = time_txt
            self.time_label.config(text=self.time)
        if self.temperature != temperature:
            self.temperature = temperature
            self.temperature_label.config(text=self.temperature)

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
