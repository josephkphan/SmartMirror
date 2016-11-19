from project.resources.var import *
import time


class SelectionHandler:
    def __init__(self):
        self.begin_time, self.current_zone = None, None

    # Keeps track of how long the cursor has been in the zone
    def update(self, zone):
        # cursor not in zone
        if self.current_zone != zone:
            self.current_zone = zone            # update zone
            self.begin_time = time.time()       # update times
            return None
        else:
            # cursor still in zone and has exceeded the selection time
            if (time.time() - self.begin_time) > selection_time:
                self.current_zone = None        # reset the zone
                self.begin_time = time.time()   # reset the timer
                return zone
