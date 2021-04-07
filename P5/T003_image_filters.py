# Group  : T003
# Course : ECOR1042G
# Number : 101195221, 101181018, 101178559, 101185138
# Names  : Jacob Ridgway, Mayukh Gautam, Alex Watson, Alexander Christie
from Cimpl import *
from typing import List, Tuple
from point_manipulation import sort_points
from simple_Cimpl_filters import grayscale
import numpy as npy
from string import punctuation


def detect_edges(image: Image, threshold: float) -> Image:  # Alexander Christie
    '''
    Returns a "pencil sketch" image copy of the image input the pencil sketch
    is a black and white version of the original where when two pixels have a
    contrasting brightness exceeding the threshold value they will modify the
    upper pixel to be black if the contrast is less than the threshold value
    the upper pixel will be set to white. The threshold parameter is a positive
    number.
    >>> image = load_image(choose_file())
    >>> show(image)
    >>> edge_image = detect_edges(image, 20)
    >>> show(edge_image)
    '''

    img_copy = copy(image)
    height = get_height(img_copy)
    for pixel in img_copy:
        x, y, (r, g, b) = pixel
        if y == (height - 1):  # this means that it is on the bottom
            new_color = create_color(255, 255, 255)
            set_color(img_copy, x, y, new_color)
        else:
            lower_color = get_color(img_copy, x, y + 1)
            rl = lower_color[0]
            gl = lower_color[1]
            bl = lower_color[2]
            upper_brighness = (r + g + b) / 3
            lower_brighness = (rl + gl + bl) / 3
            contrast = abs(upper_brighness - lower_brighness)
            if contrast > threshold:
                new_color = create_color(0, 0, 0)
                set_color(img_copy, x, y, new_color)
            else:
                new_color = create_color(255, 255, 255)
                set_color(img_copy, x, y, new_color)

    return img_copy


def flip_horizontal(image: Image) -> Image:  # Jacob Ridgway
    """
    Returns the orignal image flipped horizontally about the center axis.
    """

    new_image = copy(image)
    horz_image = new_image

    for pixel in image:
        x, y, (r, g, b) = pixel
        set_color(horz_image, -(x + 1), y, create_color(r, g, b))

    return horz_image


def flip_vertical(image: Image) -> Image:  # Alex Watson
    """
    Returns a copy of the original image flipped vertically.

    >>>file = choose_file()
    >>>image = load_image(file)
    >>>filtered_image = flip_vertical(image)
    >>>show(filtered_image)
    """
    vert_flipped = copy(image)

    for pixel in image:
        x, y, (r, g, b) = pixel
        set_color(vert_flipped, x, -(y + 1), create_color(r, g, b))

    return vert_flipped


def _interpolation(coord_list: List[Tuple[int, int]]) -> List[float]:  # Mayukh Gautam
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


def _exhaustive_search(max_x: int, polycoeff: list, val: int) -> float:  # Mayukh Gautam
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


def _image_border_finding(pixel_x: int, pixel_y: int, polycoeff: List[float]) -> List[Tuple[int, int]]:  # Mayukh Gautam
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
    upper_intersect = (_exhaustive_search(pixel_x, polycoeff, 0))
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
            temp = input(f"Enter coordinate n.{x + 1}. With this format: x,y\n").strip(punctuation).split(",")
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
        return_points.add((round(x), round(y)))
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


def extreme_contrast(image: Image) -> Image:  # Alex Watson
    """
    Returns a copy of an image, where the contrast between each pixel is maximized.

    >>>image = load_image(choose_file())
    >>>extreme_new = extreme_contrast(image)
    >>>show(extreme_new)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        if r <= 127:  # Setting r value
            r = 0
        else:
            r = 255

        if g <= 127:  # Setting g value
            g = 0
        else:
            g = 255

        if b <= 127:  # Setting b value
            b = 0
        else:
            b = 255
        extreme = create_color(r, g, b)
        set_color(new_image, x, y, extreme)
    return new_image


def _adjust_component(value: int) -> int:  # Mayukh Gautam
    """
    Takes an int representing the value of the red, green, or blue component of a pixel. This value must be between 0
    and 255 inclusive.
    It then returns the midpoint of the quadrant the value belongs to, as listed below.

    Q1 : 0-63,      midpoint : 31
    Q2 : 64-127,    midpoint : 95
    Q3 : 128-191,   midpoint : 159
    Q4 : 192-255,   midpoint : 223

    >>> _adjust_component(32)
    31
    >>> _adjust_component(189)
    233
    >>> _adjust_component(113)
    95
    """
    # Checking from largest to smallest. RGB values tend to be larger ie. greater than 100 most of the time
    # This way, odds are, the function returns a value quicker. This function will be called thousands of times,
    # the quicker the better
    return 223 if (191 < value <= 255) \
        else 159 if (127 < value <= 192) \
        else 95 if (63 < value <= 128) \
        else 31


def posterize_filter(img: Image) -> Image:  # Mayukh Gautam
    """
    Takes in an Image object as an argument.
    The function then creates a posterized copy of that image and returns the posterized image.

    Does not modify the original Image object.
    >>> image = Image(filename=choose_file())
    >>> posterized = posterize_filter(image)
    >>> show(posterized)
    """
    fill = Image(width=img.get_width(), height=img.get_height())
    for i, j, (r, g, b) in img:
        fill.set_color(i, j, Color(red=_adjust_component(r),
                                   blue=_adjust_component(b),
                                   green=_adjust_component(g)))
    return fill


def sepia_filter(image: Image) -> Image:  # Jacob Ridgway
    """
    Returns a copy of the original image with the sepia filter applied.

    >>> file = choose_file()
    >>> image = load_image(file)
    >>> filtered_image = sepia_filter(image)
    >>> show(filtered_image)
    """

    new_image = copy(image)
    gray_image = grayscale(new_image)
    for pixel in gray_image:
        x, y, (r, g, b) = pixel
        if r < 63:
            new_colour = create_color(r * 1.1, g, b * 0.9)
            set_color(gray_image, x, y, new_colour)
        elif 63 <= r <= 191:
            new_colour = create_color(r * 1.15, g, b * 0.85)
            set_color(gray_image, x, y, new_colour)
        elif 191 < r <= 255:
            new_colour = create_color(r * 1.08, g, b * 0.93)
            set_color(gray_image, x, y, new_colour)

    return gray_image


BLACK = ('black', 0, 0, 0)
WHITE = ('white', 255, 255, 255)
BLOOD = ('blood', 255, 0, 0)
GREEN = ('green', 0, 255, 0)
BLUE = ('blue', 0, 0, 255)
LEMON = ('lemon', 255, 255, 0)
AQUA = ('aqua', 0, 255, 255)
PINK = ('pink', 255, 0, 255)
GRAY = ('gray', 128, 128, 128)
color_tones = [BLACK, WHITE, BLOOD, GREEN, BLUE, LEMON, AQUA, PINK, GRAY]


def three_tone(colour1: str, colour2: str, colour3: str, image: Image) -> Image:  # Alexander Christie
    '''
    Returns a copie of the input image filtered with all pixles with average
    brightness in range 0-84 as colour defined by colour1, similarly pixles with
    brighness in range 85-170 the pixles have colour defined by the argument
    colour2. Finally, pixles with average brighness in range 171-255 will be
    assigned the colour defined by colour3.

    >>> image = load_image(choose_file())
    >>>show(image)
    >>> three_tone_image = three_tone('black', 'white', 'blue', image)
    >>>show(three_tone_image)
    '''
    duplicate = copy(image)
    for pixel in duplicate:
        x, y, (r, g, b) = pixel
        brightness = round((r + g + b) / 3)
        if brightness <= 84:

            for i in range(len(color_tones)):
                if color_tones[i][0] == colour1:
                    color, r, g, b = color_tones[i]
                    new_colour = create_color(r, g, b)

        elif 85 <= brightness <= 170:

            for i in range(len(color_tones)):
                if color_tones[i][0] == colour2:
                    color, r, g, b = color_tones[i]
                    new_colour = create_color(r, g, b)

        else:

            for i in range(len(color_tones)):
                if color_tones[i][0] == colour3:
                    color, r, g, b = color_tones[i]
                    new_colour = create_color(r, g, b)
        set_color(duplicate, x, y, new_colour)
    return duplicate


def combine(img_1: Image, img_2: Image, img_3: Image) -> Image:  # Mayukh Gautam
    """
    Takes in three Cimpl Image objects of matching dimentions. One filtered red, one filtered green, and one filtered
    blue. Then combines the three filtered images into one final image.

    :returns: The combined image object

    >>> img1 = Image(filename=choose_file())
    >>> img2 = Image(filename=choose_file())
    >>> img3 = Image(filename=choose_file())
    >>> res = combine(img1, img2, img3)
    >>> show(res)
    """
    final_img = Image(height=img_1.get_height(), width=img_1.get_width())

    for i, j, (r, g, b) in img_1:
        colour_2, colour_3 = img_2.get_color(i, j), img_3.get_color(i, j)
        # Since we don't know which image is filtered to which colour
        r = (r + colour_2[0] + colour_3[0]) if (r + colour_2[0] + colour_3[0]) <= 255 else 255
        g = (g + colour_2[1] + colour_3[1]) if (g + colour_2[1] + colour_3[1]) <= 255 else 255
        b = (b + colour_2[2] + colour_3[2]) if (b + colour_2[2] + colour_3[2]) <= 255 else 255
        final_img.set_color(i, j, Color(r, g, b))
    return final_img


def blue_filter(image: Image) -> Image:   # Author: Jacob Ridgway
    """
    Returns a copy of original image with the red and green channels removed,
    leaving only the blue channel.

    >>> file = choose_file()
    >>> image = load_image(file)
    >>> blue_filtered_image = blue_filter(image)
    >>> show(blue_filtered_image)
    """

    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0, 0, b)
        set_color(new_image, x, y, new_colour)

    return new_image


def green_filter(image: Image) -> Image:
    """
    Returns a copy of image; that is, an image that only contains the green
    components of the original image.

    >>> image = load_image(choose_file())
    >>> green_filtered = green_filter(image)
    >>> show(green_filtered)
    """

    new_image = copy(image)
    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)
        set_color(new_image, x, y, green)
    return new_image


def red_channel(image: Image) -> Image:
    '''
    Returns a copy of the image as a new image containing only the red component
    of the original r,g,b color.
    >>> image = choose_file()
    >>>show(image)
    >>> red_image = red_channel(image)
    >>>show(red_image)

    '''
    duplicate = copy(image)
    for pixle in duplicate:
        x, y, (r, g, b) = pixle
        new_color = create_color(r, 0, 0)
        set_color(duplicate, x, y, new_color)
    return duplicate


if __name__ == '__main__':
    # Calls every filter. This should not be run unless testing
    image = Image(filename=choose_file())
    show(detect_edges(image, 15))
    show(flip_horizontal(image))
    show(flip_vertical(image))
    show(draw_curve(image, "lemon")[0])
    show(extreme_contrast(image))
    show(posterize_filter(image))
    show(sepia_filter(image))
    show(three_tone("blood", "lemon", "aqua", image))

    red = red_channel(image)
    show(red)
    blue = blue_filter(image)
    show(blue)
    green = green_filter(image)
    show(green)

    show(combine(red, blue, green))
