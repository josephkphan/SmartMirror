
class CursorHandler:

    def __init__(self):
        self.counter = 0;
        self.area_one_bounds = (0,0,0,0)

    def update_cursor(self, cursor):
        # Checks if value is still in the same zone. if it is, increase counter
        if cursor < 100:
            self.counter += 1
        # Else reset counter, and update current zone
        # If counter reaches a certain value, let program know something was selected
