from resources.var import *
import time


class SelectionHandler:
    def __init__(self):
        self.begin_time, self.current_zone = None, None

    # Keeps track of how long the cursor has been in the zone
    def update(self, zone, camera_select_mode):
        # cursor not in zone
        if camera_select_mode:
            # Camera Select Mode is on
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
        else:
            # Camera Select mode is off
            self.current_zone = None
            self.begin_time = time.time()  # update times
