from Tkinter import *


# Creates a Calendar Widget
class CalendarEvent(Frame):
    def __init__(self, parent, event_name="Event 1"):
        Frame.__init__(self, parent, bg='black')
        self.event_name = event_name
        self.event_label = Label(self, text=self.event_name, font=('Helvetica', 18), fg="white", bg="black")
        self.event_label.pack(side=TOP, anchor=E)


class Calendar(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.title = 'Calendar Events'
        self.calendar_label = Label(self, text=self.title, font=('Helvetica', 28), fg="white", bg="black")
        self.calendar_label.pack(side=TOP, anchor=E)
        self.calendar_event_container = Frame(self, bg='black')
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
