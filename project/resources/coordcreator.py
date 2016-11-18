# This method will will return an array of 4 x,y coordinates of a rectangle
# The given X and Y input should be the bottom left corner of the rectangle


def get_polygon_coord(x, y, width, height):
    return [(x, y), (x, y + height), (x + width, y + height),
            (x + width, y)]
