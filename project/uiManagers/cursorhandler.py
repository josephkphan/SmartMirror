from shapely.geometry import *
from project.resources.page import *
from project.resources import var, zone


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
        self.zone_main_settings = Polygon(var.bottom_right_rectangle)

        # ---------------------------------- WEATHER PAGE ZONES ----------------------------------- #
        self.zone_weather_return = Polygon(var.top_left_rectangle)

        # ---------------------------------- Settings ZONES ----------------------------------- #
        self.zone_settings_return = Polygon(var.top_left_rectangle)


        # ---------------------------------- CLOCK PAGE ZONES ----------------------------------- #


    # Checks which polygon / zone the cursor is in (based on the current page)
    def update_cursor(self, cursor, current_page):
        p = Point(cursor[0], cursor[1])
        # Update Zones for Main Page
        if current_page == Page.main:
            if Polygon(self.zone_main_weather).contains(p):
                self.zoneName = zone.MainPage.weather
            elif Polygon(self.zone_main_clock).contains(p):
                self.zoneName = zone.MainPage.clock
            elif Polygon(self.zone_main_news).contains(p):
                self.zoneName = zone.MainPage.news
            elif Polygon(self.zone_main_settings).contains(p):
                self.zoneName = zone.MainPage.settings
            else:
                self.zoneName = zone.MainPage.none

        # Update Zones for Weather Page
        elif current_page == Page.weather:
            if Polygon(self.zone_weather_return).contains(p):
                self.zoneName = zone.Weather.returnButton
            else:
                self.zoneName = zone.Weather.none

        # Update Zones for Settings Page
        elif current_page == Page.settings:
            if Polygon(self.zone_settings_return).contains(p):
                self.zoneName = zone.Settings.returnButton
            else:
                self.zoneName = zone.Settings.none
        return self.zoneName
