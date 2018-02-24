from Tkinter import *
from resources import var


# Creates a Calendar Widget
class CalendarEvent(Frame):
    def __init__(self, parent, event_name="Event 1"):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        self.event_name = event_name
        self.event_label = Label(self, text=self.event_name, font=(font_style, 18), fg=selected_off,
                                 bg=background_color)
        self.event_label.pack(side=TOP, anchor=E)


class Calendar(Frame):
    def __init__(self, parent, *args, **kwargs):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        Frame.__init__(self, parent, bg=background_color)
        self.title_text = 'Calendar Events'
        self.calendar_label = Label(self, text=self.title_text, font=(font_style, 28), fg=selected_off, bg=background_color)
        self.calendar_label.pack(side=TOP, anchor=E)
        self.calendar_event_container = Frame(self, bg=background_color)
        self.calendar_event_container.pack(side=TOP, anchor=E)
        self.get_events()

    def get_events(self):
        # TODO: implement this method
        # reference https://developers.google.com/google-apps/calendar/quickstart/python

        # remove all children
        for widget in self.calendar_event_container.winfo_children():
            widget.destroy()

        calendar_event = CalendarEvent(self.calendar_event_container)
        calendar_event.pack(side=TOP, anchor=E)
        pass
