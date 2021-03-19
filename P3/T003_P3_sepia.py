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
    
    >>>
    >>>
    """
    
    new_image = copy(image)
    gray_image = grayscale(new_image)
    for pixel in gray_image:
        x,y, (r,g,b) = pixel
        new_colour = create_color(r*1.15,g,b*0.85)
        set_color(gray_image,x,y,new_colour)
    
    return gray_image


#Main Script
#---------------------------------------------------------------------
show(sepia_filter(load_image(choose_file())))
#print(get_color(sepia_filter(load_image(choose_file())),1,1))

