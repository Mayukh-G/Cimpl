#Author: Jacob Ridgway
#Student ID: 101195221
#Group No.: T003
#---------------------------------------------------------------------
from Cimpl import *
from unit_testing import check_equal
from simple_Cimpl_filters import grayscale
#---------------------------------------------------------------------
def sepia_filter(image: Image) -> Image:
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
        x,y, (r,g,b) = pixel
        if r < 63: 
            new_colour = create_color(r*1.1,g,b*0.9)
            set_color(gray_image,x,y,new_colour)
        elif 63 <= r <= 191:
            new_colour = create_color(r*1.15,g,b*0.85)
            set_color(gray_image,x,y,new_colour)
        elif 191 < r <= 255:
            new_colour = create_color(r*1.08,g,b*0.93)
            set_color(gray_image,x,y,new_colour)            
            
    return gray_image




