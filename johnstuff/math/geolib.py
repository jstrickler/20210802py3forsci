"""
A simple geometry library
"""

from math import pi

def circle_area(diameter=1):
    """
    Calculate the area of a circle from its diameter

    :param diameter: Diameter of the circle as a float or int
    :return: Area of circle as a float
    """
    return pi * ((diameter / 2) ** 2)


def rectangle_area(length, width):
    """
    Calculate the area of a rectangle. Returns float.

    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Area of rectangle as float
    """
    return float(length * width)


def pyramid_volume(length, width, height):
    """
    Calculate volume of pyramid

    :param length: Length of base
    :param width: Width of base
    :param height: Height of pyramid
    :return: Volume as float
    """
    return (length * width * height) / 3


def cylinder_volume(diameter, height):
    radius = diameter / 2
    return pi * (radius ** 2) * height

if __name__ == '__main__':  # if main script, not imported
    print("HI MOM!")
