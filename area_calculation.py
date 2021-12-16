

import math
# Holds all the mathematical functions which are used in area calculation of each shape 
def circle_area(radius):
    c_area = math.pi * radius ** 2
    return round(c_area, 2)

def square_area(length):
    s_area = length ** 2
    return round(s_area, 2)

def triangle_area(base):
    t_area = (3 ** 0.5 * base ** 2) / 4
    return round(t_area, 2)
