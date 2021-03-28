'''
Author : Alexander Christie
StudentNum : 101185138
Group : T003
'''
from Cimpl import (get_height, copy, create_color, set_color, get_color,
                   choose_file, get_color, Image, load_image, show)

def detect_edges(image: Image, threshold: float) -> Image:
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
        if y == (height - 1) : #this means that it is on the bottom 
            new_color = create_color(255,255,255)
            set_color(img_copy, x, y, new_color) 
        else:
            lower_color = get_color(img_copy, x, y + 1)
            rl = lower_color[0]
            gl = lower_color[1]
            bl = lower_color[2]
            upper_brighness = (r + g + b)/3
            lower_brighness = (rl + gl +bl)/3
            contrast = abs(upper_brighness - lower_brighness)
            if contrast > threshold :
                new_color = create_color(0,0,0)
                set_color(img_copy, x, y, new_color)
            else:
                new_color = create_color(255,255,255)
                set_color(img_copy, x, y, new_color)
    
    return img_copy

    
                
           
            

