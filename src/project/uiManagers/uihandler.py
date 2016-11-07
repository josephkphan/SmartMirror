from news import *
from weather import *
from cursorhandler import *
from calendarBook import *
from src.project.uiManagers.clock import *
from page import *
from returnButton import *
from src.project.resources.var import *  # todo should change back to regular import


# File Name: UI Handler:
# Purpose: Handles all TKinter widgets and displays them appropriately based on the given inputs from the hardware


class UIManager:
    def __init__(self):
        self.counter = 0
        self.zone = MainPageZone.weather
        self.current_page = Page.main
        self.cursor_handler = CursorHandler()
        self.weather, self.clock, self.news, self.returnButton = None, None, None, None
        self.tk = Tk()
        self.tk2 = Tk()
        self.canvas = Canvas(self.tk2, width=camera_width + tk_cursor_diameter,
                             height=camera_height + tk_cursor_diameter, background='black')
        self.circle_coord = (0, 0)
        self.circle_diameter = tk_cursor_diameter  # todo scale the cursor to match screen size
        self.cursor = self.canvas.create_oval(0, 0, tk_cursor_diameter, tk_cursor_diameter,
                                              fill="blue", outline="#DDD", width=tk_cursor_outline_thickness)
        # Vertical line
        self.line1 = self.canvas.create_line((camera_width / 2 + tk_cursor_diameter / 2, 0),
                                             (camera_width / 2 + tk_cursor_diameter / 2,
                                              camera_height + tk_cursor_diameter), fill="green", )
        # Horizontal line
        self.line2 = self.canvas.create_line((0, camera_height / 2 + tk_cursor_diameter / 2),
                                             (camera_width + tk_cursor_diameter,
                                              camera_height / 2 + tk_cursor_diameter / 2), fill="green", )
        self.canvas.pack()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background='black')
        self.bottomFrame = Frame(self.tk, background='black')
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk.bind("<W>",self.update_page(Page.weather))
        self.tk.bind("<M>", self.update_page(Page.main))    # todo : Doesn't work. please fix

        self.open_new_main_page()
        # calender - removing for now
        # self.calender = Calendar(self.bottomFrame)
        # self.calender.pack(side = RIGHT, anchor=S, padx=100, pady=60)

    # ---------------------------------- Key Binding Functions----------------------------------- #

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


    # ---------------------------------- Pages ----------------------------------- #

    def open_new_main_page(self):
        self.start_clock()
        self.start_new_weather()
        self.start_news()

    def open_loaded_main_page(self):
        self.start_clock()
        self.start_loaded_weather()
        self.start_news()

    def close_main_page(self):
        self.end_news()
        self.end_weather()
        self.end_clock()

    # ---------------------------------- PAGE COMPONENTS ----------------------------------- #

    # ---------------------------------- MAIN PAGE COMPONENTS ----------------------------------- #
    def start_news(self):
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=50, pady=50)

    def end_news(self):
        self.news.destroy()

    def start_loaded_weather(self):
        print "CHECKPOINT"
        print saved_data
        self.weather = Weather(self.topFrame, True)  # todo change this
        self.weather.pack(side=LEFT, anchor=N, padx=50, pady=50)

    # todo only on first time load upif data jsondoesnt exist
    def start_new_weather(self):
        self.weather = Weather(self.topFrame, False)
        self.weather.pack(side=LEFT, anchor=N, padx=50, pady=50)

    def end_weather(self):
        self.weather.destroy()

    def start_clock(self):
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=50, pady=50)

    def end_clock(self):
        self.clock.destroy()

    def new_return_button(self):
        self.returnButton = ReturnButton(self.topFrame)
        self.returnButton.pack(side=LEFT, anchor=N, padx=50, pady=50)

    # ---------------------------------- OTHER COMPONENTS ----------------------------------- #

    def remove_return_button(self):
        self.returnButton.destroy()

    # ---------------------------------- UPDATING UIMANAGER ----------------------------------- #

    def update(self, cursor):
        if self.counter == 50:
            self.change_page(2)
        elif self.counter == 100:
            self.change_page(1)
        self.counter += 1
        self.update_zone(cursor)
        # print str(self.counter)
        # print "X Coord: "  + str(cursor[0]) + "  |  Y Coord: " + str(cursor[1])
        diff_x = cursor[0] - self.circle_coord[0]
        diff_y = cursor[1] - self.circle_coord[1]
        # print "diff X = " + str(diff_x) + "  |  diff y = " + str(diff_y)
        self.canvas.move(self.cursor, diff_x, diff_y)
        # self.canvas.move(self.cursor, cursor[0], cursor[1])
        self.circle_coord = cursor
        # self.canvas.update()
        # self.canvas.update_idletasks()
        self.tk.update_idletasks()
        self.tk.update()
        self.tk2.update_idletasks()
        self.tk2.update()

    def update_page(self,new_page):
        print "UPDATING PAGE!!!!"
        self.current_page = new_page

    def update_zone(self, cursor):
        self.zone = self.cursor_handler.update_cursor(cursor, self.current_page)
        # Updating Zone based on Main Page
        if self.current_page == Page.main:
            if self.zone == MainPageZone.weather:
                self.weather.change_color_to_yellow()
                self.news.change_color_to_white()
                self.clock.change_color_to_white()
            elif self.zone == MainPageZone.news:
                self.weather.change_color_to_white()
                self.news.change_color_to_yellow()
                self.clock.change_color_to_white()
            elif self.zone == MainPageZone.clock:
                self.weather.change_color_to_white()
                self.news.change_color_to_white()
                self.clock.change_color_to_yellow()
        elif self.current_page == Page.weather:
            if self.zone == WeatherZone.returnButton:
                self.returnButton.change_color_to_yellow()
            else:
                self.returnButton.change_color_to_white()

    def change_page(self,newpage, event = None):
        if newpage == 1:  # MAIN PAGE
            self.remove_return_button()
            self.open_loaded_main_page()
            self.current_page = Page.main
        elif newpage == 2:  # BLANK PAGE
            self.close_main_page()
            self.current_page = Page.weather
            self.new_return_button()
