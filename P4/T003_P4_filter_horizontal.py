# Author: Jacob Ridgway
# Student ID: 101195221
# Group No.: T003
#---------------------------------------------------------------------
from Cimpl import *
from unit_testing import check_equal
#---------------------------------------------------------------------
def flip_horizontal(image: Image) -> Image:
    """
    Returns the orignal image flipped horizontally about the center axis.
    """
    
    new_image = copy(image)
    horz_image = new_image
    
    for pixel in image:
        x,y,(r,g,b) = pixel
        set_color(horz_image, -(x+1), y, create_color(r,g,b))
            
    return horz_image
                        
#---------------------------------------------------------------------
# Main Script

if __name__ == "__main__":
    file = choose_file()
    image = load_image(file)
    horz_image = flip_horizontal(image)
    show(horz_image)
       
