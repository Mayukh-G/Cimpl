# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
# Group  : T003
from typing import List, Tuple
from Cimpl import *
from point_manipulation import sort_points
import numpy as npy
import string


def _interpolation(coord_list: List[Tuple[int, int]]) -> List[int]:
    return None


def _exhaustive_search():
    return None


def _image_border_finding(img_width: int, img_height: int, coefficients: List[int]) -> List[Tuple[int, int]]:
    return None


COLOURS = (
    ("black", Color(0, 0, 0)),
    ("white", Color(255, 255, 255)),
    ("blood", Color(255, 0, 0)),
    ("green", Color(0, 255, 0)),
    ("blue", Color(0, 0, 255)),
    ("lemon", Color(255, 255, 0)),
    ("aqua", Color(0, 255, 255)),
    ("pink", Color(255, 0, 255)),
    ("gray", Color(128, 128, 128))
)

Fx = npy.polyval


def draw_curve(image: Image, col: str, coords: List[Tuple[int, int]] = None) -> Image:
    """
    Takes an Image object, a string that represents one of many colors and an optional list of coordinate tuples.
    This function then draws an interpolated curve with a width of 9 pixels using the coordinates provided.
    This function does not modify the original image.

    :param coords: If this argument is empty or None, this function will ask the user for coordinates. If not, this
    function will use the coordinates passed in and will not ask for user input. The coordinates must not be out of
    bounds of the image and may not be vertically alligned.

    :param col:Must be one of the following: "black", "white", "blood", "green", "blue", "lemon", "aqua", "pink", "gray"

    >>> im = Image(filename=choose_file())
    >>> result = draw_curve(im, "blue")
    >>> show(result)

    or for testing :

    >>> im = Image(width=100, height=100)
    >>> result = draw_curve(im, "blue", [(0, 0), (20, 80), (30, 200)])

    :returns: A copy of the original image passed in but with a curve drawn on it
    """
    img_c = image.copy()
    for colours in COLOURS:  # Select correct Colour
        if colours[0] == col:
            chosen_col = colours[1]

    coord_internal = []
    # UI for getting points
    if not coords:
        num_coords = input("How many coordinates would you like to input?\n")
        for x in range(int(num_coords)):
            # Formats user input into a more tuple friendly format
            temp = input(f"Enter coordinate n.{x+1}. With this format: x,y\n").strip(string.punctuation).split(",")
            # Changing the string to an integer
            for i in range(len(temp)):
                temp[i] = int(temp[i])
            coord_internal.append(tuple(temp))
    coord_internal = sort_points(coord_internal)  # Sort points by ascending x values

    poly_coefficients = _interpolation(coord_internal)
    edge_points = _image_border_finding(image.get_width(), image.get_height(), poly_coefficients)

    border_x = []   # Only the x values of the border points
    for point in edge_points:
        border_x.append(point[0])

    # Drawing curve
    allow = True
    for x in range(image.get_width()):
        if (x not in border_x) and allow:  # This will only draw if the function is within range of the image
            y = int(Fx(poly_coefficients, x))  # polyval returns a numpy.int32 type. This in incompatible with Cimpl
            for j in range(9):  # Adding the thickness of the line. Only if it is within range of the image
                r = y - 4 + j
                if r in range(image.get_height()):
                    img_c.set_color(x, r, chosen_col)
        else:
            # Checking if the next point is within range of the image
            allow = 0 < Fx(poly_coefficients, x+1) < image.get_height()
    return img_c


if __name__ == '__main__':
    im = Image(filename=choose_file())
    drawn = draw_curve(im, "black")
    show(drawn)



