from news import *
from weather import *
from cursorhandler import *
from src.project.uiManagers.clock import *


class UIManager:
    def __init__(self):
        self.counter = 0;
        self.zone = None
        self.cursor_handler = CursorHandler();
        self.weather, self.clock, self.news = None, None, None
        self.tk = Tk()
        self.tk2 = Tk()
        self.canvas = Canvas(self.tk2, width=300, height=300, background='black')
        self.circle_coord = (0,0)
        self.circle_diameter = 10       #todo scale the cursor to match screen size
        # self.cursor = self.canvas.create_oval(self.circle_coord[0], self.circle_coord[1],
        #                                       self.circle_coord[0] + self.circle_diameter,
        #                                       self.circle_coord[1] + self.circle_diameter
        #                                       , fill="blue", outline="#DDD", width=4)
        self.cursor = self.canvas.create_oval(0,0,50,50,fill="blue", outline="#DDD", width=4)
        self.line1 = self.canvas.create_line((150,0), (150,300), fill = "green",)
        self.line2 = self.canvas.create_line((0, 150), (300, 150), fill="green", )
        self.canvas.pack()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # clock
        self.start_clock()
        # weather
        self.start_weather()
        # news
        self.start_news()
        # calender - removing for now
        # self.calender = Calendar(self.bottomFrame)
        # self.calender.pack(side = RIGHT, anchor=S, padx=100, pady=60)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    # ---------------------------------- Starter and Enders ----------------------------------- #

    def start_all(self):
        self.start_clock()
        self.start_news()
        self.start_news()

    def end_all(self):
        self.end_news()
        self.end_weather()
        self.end_clock()

    def start_news(self):
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)

    def end_news(self):
        self.news.pack_forget()

    def start_weather(self):
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=LEFT, anchor=N, padx=100, pady=60)

    def end_weather(self):
        self.weather.pack_forget()

    def start_clock(self):
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)

    def end_clock(self):
        self.clock.pack_forget()

        # ---------------------------------- ----------------------------------- #
    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def update(self, cursor):
        if self.counter > 50:
            self.weather.change_color_to_yellow()
            self.news.change_color_to_yellow()
            self.clock.change_color_to_yellow()
            self.counter= -500
        self.counter += 1;
        self.update_zone(cursor)
        # print str(self.counter)
        # print "X Coord: "  + str(cursor[0]) + "  |  Y Coord: " + str(cursor[1])
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        #print "diff X = " + str(diff_x) + "  |  diff y = " + str(diff_y)
        self.canvas.move(self.cursor, diff_x, diff_y)
        # self.canvas.move(self.cursor, cursor[0], cursor[1])
        self.circle_coord = cursor
        #self.canvas.update()
        #self.canvas.update_idletasks()
        self.tk.update_idletasks()
        self.tk.update()
        self.tk2.update_idletasks()
        self.tk2.update()

    def update_zone(self, cursor):
        self.zone = self.cursor_handler.update_cursor(cursor)
        if self.zone == 1:
            self.weather.change_color_to_yellow()
            self.news.change_color_to_white()
            self.clock.change_color_to_white()
        elif self.zone == 2:
            self.weather.change_color_to_white()
            self.news.change_color_to_yellow()
            self.clock.change_color_to_white()
        elif self.zone == 3:
            self.weather.change_color_to_white()
            self.news.change_color_to_white()
            self.clock.change_color_to_yellow()