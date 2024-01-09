from math import sqrt
def foo(gutter_height):

    distance_from_wall = gutter_height / 4
    ladder_height = sqrt((gutter_height**2) + (distance_from_wall**2))

    return ladder_height
    