from shapely.geometry import *

from src.project.resources.page import *

from src.project.resources import var
from src.project.resources import zone


class CursorHandler:
    def __init__(self, ):
        self.zoneName = None
        # Initialize MainPage Zones by creating Polygons based on coordinates.
        # todo currently in boxes..? Change???

        # ---------------------------------- MAIN PAGE ZONES ----------------------------------- #
        # top Left
        self.zone_main_weather = Polygon(var.top_left_rectangle)
        # top right
        self.zone_main_clock = Polygon(var.top_right_rectangle)
        # bottom Left
        self.zone_main_news = Polygon(var.bottom_left_rectangle)
        # bottom right
        # self.zone_UNAMED = Polygon(var.bottom_right_rectangle)             NOT USED RIGHT NOW

        # ---------------------------------- WEATHER PAGE ZONES ----------------------------------- #
        self.zone_weather_return = Polygon(var.top_left_rectangle)

        # ---------------------------------- NEWS PAGE ZONES ----------------------------------- #

        # ---------------------------------- CLOCK PAGE ZONES ----------------------------------- #

    # Checks which polygon / zone the cursor is in (based on the current page)
    def update_cursor(self, cursor, current_page):
        p = Point(cursor[0], cursor[1])
        if current_page == Page.main:
            if Polygon(self.zone_main_weather).contains(p):
                # print "In Zone 1"
                self.zoneName = zone.MainPage.weather
            elif Polygon(self.zone_main_clock).contains(p):
                # print "In Zone 2"
                self.zoneName = zone.MainPage.clock
            elif Polygon(self.zone_main_news).contains(p):
                # print "In Zone 3"
                self.zoneName = zone.MainPage.news
            else:
                self.zoneName = zone.MainPage.none
        elif current_page == Page.weather:
            if Polygon(self.zone_weather_return).contains(p):
                self.zoneName = zone.Weather.returnButton
            else:
                self.zoneName = zone.Weather.none
        return self.zoneName
