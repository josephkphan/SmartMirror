from shapely.geometry import *
import numpy as np
from src.project.resources.var import *
from page import *
from zone import *
from src.project.resources.var import *


class CursorHandler:
    def __init__(self, ):
        self.zoneName = None
        # Initialize MainPage Zones by creating Polygons based on coordinates.
        # todo currently in boxes..? Change???

        # ---------------------------------- MAIN PAGE ZONES ----------------------------------- #
        # top Left
        self.zone_main_weather = Polygon(top_left_rectangle)
        # top right
        self.zone_main_clock = Polygon(top_right_rectangle)
        # bottom Left
        self.zone_main_news = Polygon(bottom_left_rectangle)
        # bottom right
        self.zone_UNAMED = Polygon(bottom_right_rectangle)

        # ---------------------------------- WEATHER PAGE ZONES ----------------------------------- #
        self.zone_weather_return = Polygon(top_left_rectangle)

        # ---------------------------------- NEWS PAGE ZONES ----------------------------------- #

        # ---------------------------------- CLOCK PAGE ZONES ----------------------------------- #

    # Checks which polygon / zone the cursor is in (based on the current page)
    def update_cursor(self, cursor, current_page):
        p = Point(cursor[0], cursor[1])
        if current_page == Page.main:
            if Polygon(self.zone_main_weather).contains(p):
                # print "In Zone 1"
                self.zoneName = MainPageZone.weather
            elif Polygon(self.zone_main_clock).contains(p):
                # print "In Zone 2"
                self.zoneName = MainPageZone.clock
            elif Polygon(self.zone_main_news).contains(p):
                # print "In Zone 3"
                self.zoneName = MainPageZone.news
            elif Polygon(self.zone_UNAMED).contains(p):
                # print "In Zone 4"
                self.zoneName = 4  # todo change this or remove it later
            else:
                self.zoneName = MainPageZone.none
        elif current_page == Page.weather:
            if Polygon(self.zone_weather_return).contains(p):
                self.zoneName = WeatherZone.returnButton
            else:
                self.zoneName = WeatherZone.none
        return self.zoneName
