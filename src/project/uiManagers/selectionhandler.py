from src.project.resources.var import *


class SelectionHandler:
    def __init__(self):
        self.begin_time, self.current_zone = None, None

    def update(self, zone):
        if self.current_zone != zone:               # cursor not in zone
            self.current_zone = zone                # update zone
            self.begin_time = time.time()           # update times
            return None
        else:                                       # cursor still in zone
            if (time.time() - self.begin_time) > selection_time:
                print "HERE"
                self.current_zone = None
                self.begin_time = time.time()
                return zone
