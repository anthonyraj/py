from math import *

def light_pixel(x,y):
    print x,y
"""
x = cx + r * cos(a)
y = cy + r * sin(a)
"""
def get_point(angle, radius, centerx, centery):
    print angle, radius, centerx, centery
    x = centerx + radius * cos(angle)
    y = centery + radius * sin(angle)
    return x,y

radius = input("Please enter radius: ")
origin = map(int, raw_input("Enter co-ordinates: ").split())

for angle in range(360):
    x,y = get_point(angle, radius, origin[0], origin[1])
    light_pixel(x,y)
