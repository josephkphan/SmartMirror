from shapely.geometry import *
import numpy as np
from src.project.resources.var import *

class CursorHandler:

    def __init__(self ):
        self.zoneName = None
        # MainPage Zones
        self.zone1 = Polygon([(0,0),(0,camera_height/2), (camera_width/2,camera_height/2),
                              (camera_width/2,0)])  # bottom Left
        self.zone2 = Polygon([(0,camera_height/2),(0,camera_height), (camera_width/2,camera_height),
                              (camera_width/2,camera_height/2)])  # top Left
        self.zone3 = Polygon([(camera_width/2,0),(camera_width/2,camera_height/2),
                              (camera_width,camera_height/2), (camera_width,0)])  # bottom right
        self.zone4 = Polygon([(camera_width/2,camera_height/2),(camera_width/2,camera_height),
                              (camera_width,camera_height), (camera_width/2,camera_height)])  # top right

    def update_cursor(self, cursor):
        p = Point(cursor[0], cursor[1])

        if Polygon(self.zone1).contains(p):
            # print "In Zone 1"
            self.zoneName = 1
        elif Polygon(self.zone2).contains(p):
            # print "In Zone 2"
            self.zoneName = 2
        elif Polygon(self.zone3).contains(p):
            # print "In Zone 3"
            self.zoneName = 3
        elif Polygon(self.zone4).contains(p):
            # print "In Zone 4"
            self.zoneName = 4
        return self.zoneName
