from shapely.geometry import *
import numpy as np

class CursorHandler:

    def __init__(self ):
        self.zoneName = None
        self.zone1 = Polygon([(0,0),(0,150), (150,150),(150,0)])
        self.zone2 = Polygon([(0,150),(0,300), (150,300), (150,150)])
        self.zone3 = Polygon([(150,0),(150,150), (300,150), (300,0)])
        self.zone4 = Polygon([(150,150),(150,300), (300,300), (150,300)])

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
