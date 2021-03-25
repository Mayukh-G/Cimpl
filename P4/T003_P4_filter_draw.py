# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
# Group  : T003
from typing import List, Tuple
from Cimpl import *
import numpy as npy
import string


def _interpolation():
    return None


def _exhaustive_search():
    return None


def _image_border_finding():
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


def draw_curve(image: Image, col: str, coords: List[Tuple[int, int]] = None) -> Image:
    """
    Takes an Image object, a string that represents one of many colors and an optional list of coordinate tuples.
    This function then draws an interpolated curve with a width of roughly 9 pixels using the coordinates provided.
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
    for colours in COLOURS:
        if colours[0] == col:
            chosen_col = colours[1]

    coord_internal = []
    if not coords:
        num_coords = input("How many coordinates would you like to input?\n")
        for x in range(int(num_coords)):
            temp = input(f"Enter coordinate n.{x+1}. With this format: x,y\n").strip(string.punctuation).split(",")
            for i in range(len(temp)):
                temp[i] = int(temp[i])
            coord_internal.append(temp)
    print(coord_internal)


if __name__ == '__main__':
    draw_curve(Image(width=100, height=100), "black")


