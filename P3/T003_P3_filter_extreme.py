"""
Author: Alex Watson
Group: T003
StudentNum: 101178559
"""

from Cimpl import *
from unit_testing import check_equal

def extreme_contrast(image: Image) -> Image:
    """
    Returns a copy of an image, where the contrast between each pixel is maximized. 
    
    >>>image = load_image(choose_file())
    >>>extreme_new = extreme_contrast(image)
    >>>show(extreme_filtered) 
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        if r <= 127:
            r = 0
        else:
            r = 255
        
        if g <= 127:
            g = 0
        else: 
            g = 255
        
        if b <= 127:
            b = 0
        else: 
            b = 255
        extreme = create_color(r, g, b)
        set_color(new_image, x, y, extreme)
    return new_image


#Main Script

image = load_image(choose_file())
extreme_new = extreme_contrast(image)
show(extreme_filtered) 