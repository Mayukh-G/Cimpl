"""
Author: Jacob Ridgway
Student ID: 101195221
Group No.: T003
"""
#-------------------------------------------------------------------------
from Cimpl import *
from unit_testing import check_equal
#-------------------------------------------------------------------------
def blue_filter(image: Image) -> Image:
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
        x,y, (r,g,b) = pixel
        new_colour = create_color(0,0,b)
        set_color (new_image,x,y,new_colour)
    
    return new_image
#------------------------------------------------------------------------
def test_blue_filter() -> None:
    """
    Tests the blue_filter function.
    
    >>> test_blue_filter()
    """
    
    original = create_image(3,1)
    set_color(original,0,0,create_color(90,120,60))
    set_color(original,1,0,create_color(234,250,255))
    set_color(original,2,0,create_color(255,80,210))
    
    expected = create_image(3,1)
    set_color(expected,0,0,create_color(0,0,60))
    set_color(expected,1,0,create_color(0,0,255))
    set_color(expected,2,0,create_color(0,0,210))
    
    actual_filtered_image = blue_filter(original)
    
    for x,y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
#-------------------------------------------------------------------------
#Main Script:

#show(blue_filter(load_image(choose_file())))

file = choose_file()
image = load_image(file)
blue_filtered_image = blue_filter(image)
show(blue_filtered_image)

test_blue_filter()
