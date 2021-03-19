""" 
Author: Alex Watson
StudentNum: 101178559
Group: T003
"""

from Cimpl import *
from unit_testing import check_equal

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
  

def test_green_filter() -> None:
    """
    A test function for green_filter.
    
    >>>test_green_filter()
    """
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(1, 10, 5))
    set_color(original, 1, 0, create_color(13, 120, 55))
    set_color(original, 2, 0, create_color(125, 255, 79))
    set_color(original, 3, 0, create_color(179, 135, 210))
    set_color(original, 4, 0, create_color(30, 0, 200))
    set_color(original, 5, 0, create_color(230, 155, 65))
    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 10, 0))
    set_color(expected, 1, 0, create_color(0, 120, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(0, 135, 0))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(0, 155, 0)) 
    green_test = green_filter(original)
    for x, y, col in green_test:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
        
if __name__ == '__main__':

    image = load_image(choose_file())
    green_filtered = green_filter(image)
    show(green_filtered)    
    test_green_filter()




