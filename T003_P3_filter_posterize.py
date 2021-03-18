# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
# Group  : T003
from Cimpl import Image, Color, show, choose_file


def _adjust_component(value: int) -> int:
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


def posterize_filter(img: Image) -> Image:
    """
    Takes in an Image object as an argument. Then it cycles through every pixel of the image and reduces the color
    variance by running the _adjust_component function on the red value, the blue value, and the green value of each
    pixel and then assigns the returned value to that same pixel.

    Does not modify the original Image object.

    >>> posterize_filter(img)
    <Image object at (Memory Address)>

    :returns: A posturized image
    """
    fill = Image(width=img.get_width(), height=img.get_height())
    for i, j, (r, g, b) in img:
        fill.set_color(i, j, Color(red=_adjust_component(r),
                                   blue=_adjust_component(b),
                                   green=_adjust_component(g)))
    return fill
