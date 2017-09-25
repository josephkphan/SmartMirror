from Tkinter import *
from project.resources import var, zone


class EventList(Frame):
    def __init__(self, parent):
        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        Frame.__init__(self, parent, bg=background_color)
        self.container = Frame(self, bg=background_color)
        self.container.pack(side=TOP)
        self.top = Frame(self.container, bg=background_color)
        self.top.pack(side=TOP, anchor=W)
        self.bottom = Frame(self.container, bg=background_color)
        self.bottom.pack(side=BOTTOM)

        # Initializing a color boolean for all labels
        self.color_all = selected_off

        # Initialize to do JSON data
        self.event_labels = []

        # Initializing Labels
        self.events_title_label = Label(self.top, text="My Events", font=(font_style, font_sizes['big']),
                                        fg=selected_off, bg=background_color)
        self.events_title_label.pack(side=LEFT, anchor=W)
        self.update_now()

    def update_now(self):

        selected_off = var.selected_off
        background_color = var.background_color
        font_style = var.font_style
        font_sizes = var.font_sizes
        if self.event_labels:
            for i in range(0, len(self.event_labels)):
                for j in range(0, 5):
                    self.event_labels[i][j].pack_forget()
        self.event_labels = []

        self.bottom.pack_forget()
        self.bottom = Frame(self.container, bg=background_color)
        self.bottom.pack(side=BOTTOM)

        events = var.calendar_data
        print events
        if events:
            for i in range(0, len(events)):
                event = events[str(i)]
                print '------------------------'
                print event
                event_container = Frame(self.bottom, bg=background_color)
                event_container.pack(side=LEFT, padx=25)
                event_summary_label = Label(event_container, text=event['summary'], font=(font_style, font_sizes['text']),
                                            fg=selected_off, bg=background_color)
                event_description_label = Label(event_container, text=event['description'],
                                                font=(font_style, font_sizes['small']),
                                                fg=selected_off, bg=background_color)
                event_date_label = Label(event_container, text=event['date'], font=(font_style, font_sizes['small']),
                                         fg=selected_off, bg=background_color)
                event_time_label = Label(event_container, text=event['start_time'], font=(font_style, font_sizes['small']),
                                         fg=selected_off, bg=background_color)
                event_location_label = Label(event_container, text=event['location'],
                                             font=(font_style, font_sizes['small']),
                                             fg=selected_off, bg=background_color)
                event_summary_label.pack(side=TOP, anchor=N)
                event_description_label.pack(side=TOP, anchor=N)
                event_date_label.pack(side=TOP, anchor=N)
                event_time_label.pack(side=TOP, anchor=N)
                event_location_label.pack(side=TOP, anchor=N)

                single_event_labels = [event_summary_label, event_description_label, event_date_label, event_time_label,
                                       event_location_label]
                self.event_labels.append(single_event_labels)

        self.update_font_size()

    def update_font_size(self):
        self.events_title_label.config(font=(var.font_style, var.font_sizes['big']))
        for i in range(0, len(self.event_labels)):
            self.event_labels[i][0].config(font=(var.font_style, var.font_sizes['text']))
            for j in range(1, 5):
                self.event_labels[i][j].config(font=(var.font_style, var.font_sizes['small']))

    def change_color_all(self, mode):
        if self.color_all != mode:
            self.color_all = mode
            self.events_title_label.config(foreground=self.color_all)
            for i in range(0, len(self.event_labels)):
                for j in range(0, 5):
                    self.event_labels[i][j].config(foreground=self.color_all)

    def change_color(self, mode, current_zone):
        if self.color_all != mode:
            self.color_all = mode
            if current_zone == zone.PlannerPage.eventlist:
                self.events_title_label.config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event0:
                for j in range(0, 5):
                    self.event_labels[0][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event1:
                for j in range(0, 5):
                    self.event_labels[1][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event2:
                for j in range(0, 5):
                    self.event_labels[2][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event3:
                for j in range(0, 5):
                    self.event_labels[3][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event4:
                for j in range(0, 5):
                    self.event_labels[4][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event5:
                for j in range(0, 5):
                    self.event_labels[5][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event6:
                for j in range(0, 5):
                    self.event_labels[6][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event7:
                for j in range(0, 5):
                    self.event_labels[7][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event8:
                for j in range(0, 5):
                    self.event_labels[8][j].config(foreground=self.color_all)
            if current_zone == zone.PlannerPage.event9:
                for j in range(0, 5):
                    self.event_labels[9][j].config(foreground=self.color_all)