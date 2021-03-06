# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
# Group  : T003
from typing import List, Tuple
from Cimpl import *
from point_manipulation import sort_points
import numpy as npy
import string

def _interpolation(coord_list: List[Tuple[int, int]]) -> List[float]:
    # Helped by Jacob Ridgway
    """
    Returns coefficients of interpolating polynomial as a list, and coefficients of the 
    quadratic regression polynomial (if user entered more than 3 points).
    
    >>> _interpolation([(1,2),(3,4),(5,6)]
    [-4.51257486e-17  1.00000000e+00  1.00000000e+00]
    >>> _interpolation([(7,8),(3,4)])
    [1. 1.]
    """
    degree = 1 if len(coord_list) <= 2 else 2

    x_point = []
    y_point = []
    for point in coord_list:
        x_point.append(point[0])
        y_point.append(point[1])

    return npy.polyfit(x_point, y_point, degree)


def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> float:
    # Helped by Alexander Christie
    '''
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains the
    coefficients of f, using EPSILON of 1 (as we only need ints for pixels).
    Returns None if there is no solution between the bounds.

    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None
    >>>_exhaustive_search(5,[1e+00,-5e+00,4e+00],0)
    1 
    '''

    epsilon = 1
    step = 1
    guess = 0.0
    while abs(npy.polyval(polycoeff, guess) - val) >= epsilon and guess <= max_x:
        guess += step
    if guess > max_x:
        return None
    else:
        return guess 
    

def _image_border_finding(pixel_x: int, pixel_y: int, polycoeff: List[float]) -> List[Tuple[int, int]]:
    # Helped by Alexander Christie
    '''
    Returns an ordered list of the pixels coordinates where the fitted curve 
    given by the coefficient in polycoeff crosses the vertical or horizontal
    boarders of an image with horizontal dimension given by pixel_x and y 
    vertical dimensions given by pixel_y.
    >>>_image_border_finding(10,10,[1e+00,-5e+00,4e+00])
    [(0,4.0),(1.0,0),(6.0,10)]
    
    '''
    border_intersections = []
    upper_intersect = (_exhaustive_search( pixel_x, polycoeff,0))
    # top and bottom intersections
    if upper_intersect is not None:
        border_intersections += [(upper_intersect, 0)]
    lower_intersect = (_exhaustive_search(pixel_x, polycoeff, pixel_y))
    if lower_intersect is not None:
        border_intersections += [(lower_intersect, pixel_y)]
    
    # right and left side intersections
    if 0 < npy.polyval(polycoeff, 0) < pixel_y:
        border_intersections += [(0, npy.polyval(polycoeff, 0))]
    if 0 < npy.polyval(polycoeff, pixel_x) < pixel_y:
        border_intersections += [(pixel_x, npy.polyval(polycoeff, pixel_x))]
    
    border_intersections.sort()
    return border_intersections


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


def draw_curve(image: Image, col: str, coords: List[Tuple[int, int]] = None) -> list:
    # Mayukh Gautam
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
            # Sort points by ascending x values and interpolate
        poly_coefficients = _interpolation(sort_points(coord_internal))
    else:
        poly_coefficients = _interpolation(sort_points(coords))  # Sort points by ascending x values and interpolate
    edge_points = _image_border_finding(image.get_width(), image.get_height(), poly_coefficients)

    return_points = set()  # Making sure duplicate points are not in the list. (If function exits at a corner pixel)
    for (x, y) in edge_points:
        return_points.add((round(x), round(y)))  # Eliminating points with non integer values such as: 1.9999 or 1e-18
    return_points = sort_points(list(return_points))

    # Drawing curve
    for x in range(image.get_width()):
        # This will only draw if the function is within range of the image.
        # For some reason in Wing101 int(5.999999999) is 5. This does not happen on the IDE I use, in that it's 6,
        # round() is there so it works on Wing101.
        # polyval returns a numpy.int32 type. This in incompatible with Cimpl, so the int constructor is used.
        y = int(round(npy.polyval(poly_coefficients, x)))
        if 0 <= y <= image.get_height():
            for j in range(9):  # Adding the thickness of the line. Only if it is within range of the image
                r = y - 4 + j
                if r in range(image.get_height()):
                    img_c.set_color(x, r, chosen_col)
    return [img_c, return_points]


if __name__ == '__main__':
    im = Image(filename=choose_file())
    drawn = draw_curve(im, "pink")
    show(drawn[0])



