def get_polygon_coord(x, y, width, height):
    return [(x, y), (x, y + height), (x + width, y + height),
            (x + width, y)]
