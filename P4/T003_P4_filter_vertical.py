"""
Author: Alex Watson
StudentNum: 101178559
Group: T003
"""

from Cimpl import *


def flip_vertical (image: Image) -> Image:
    """
    Returns a copy of the original image flipped vertically. 
    
    >>>file = choose_file()
    >>>image = load_image(file)
    >>>filtered_image = flip_vertical(image)
    >>>show(filtered_image)
    """
    vert_flipped = copy(image)
    
    for pixel in image:
        x,y,(r,g,b)=pixel
        set_color(vert_flipped, x, -(y+1), create_color(r,g,b))
        
        
    return vert_flipped

#Main Script
if __name__ == '__main__':
    file = choose_file()
    image = load_image(file)
    filtered_image = flip_vertical(image)
    show(filtered_image)

        
    




